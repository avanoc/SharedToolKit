import csv
import inquirer
import re
import sys


# List of tools available
tools = [
    "Drill",
    "Hammer",
    "Ladder",
    "Airbrush",
    "Shovel",
]

# Define max tries
TRIES = 10


def main():
    # Get user's name email address, and what they want to do (add or search for a tool)
    username = name()
    email_address = mail()
    user = usage()

    # If user wants to add a tool, ask if it will be for free or for a fee, and append result to list of dict.
    if "add" in user:
        free = rent()
        with open("contacts.csv", "a") as contact_file:
            if free:
                writer = csv.DictWriter(
                    contact_file, fieldnames=["name", "email", "tool", "fee"]
                )
                writer.writerow(
                    {
                        "name": username,
                        "email": email_address,
                        "tool": user[0],
                        "fee": 0,
                    }
                )

                # Print the confirmation message
                print(
                    f"So kind of you! {user[0]} has been added to your toolkit. Users may borrow it for free."
                )
            else:
                fee = price()
                writer = csv.DictWriter(
                    contact_file, fieldnames=["name", "email", "tool", "fee"]
                )
                writer.writerow(
                    {
                        "name": username,
                        "email": email_address,
                        "tool": user[0],
                        "fee": fee,
                    }
                )

                # Print the confirmation message
                print(
                    f"Great! {user[0]} has been added to your toolkit. Users may rent it for USD {fee} per day."
                )

    # Search for a tool
    else:
        # If no user has that tool, exit program, explaining what happened
        try:
            c = contact(user)
            if c == None:
                raise ValueError("No user has that tool")
            else:
                loaner, tool, forprice, email = c
        except ValueError:
            sys.exit("Sorry, no user has that tool in their toolkit.")

        # Else, print the list of users that currently have that tool in their toolkit
        if forprice == "0":
            print(f"{loaner} will loan you a {tool} for free. Contact info: {email}.")
        else:
            print(
                f"{loaner} will loan you a {tool} for {forprice} USD per day. Contact info: {email}."
            )


def name():
    # Get user's name, only if it's in the required format
    n = 0
    while n < TRIES:
        try:
            un = str(input("What's your name? "))
            n += 1
            if not un.isalpha():
                raise ValueError
        except ValueError:
            if n < TRIES:
                continue
            else:
                sys.exit("Sorry, can't validate your name.")
        break
    return un.capitalize()


def mail():
    # Get user's email address, only if it's in the required format
    n = 0
    while n < TRIES:
        try:
            email = input("Please enter your email address: ")
            n += 1
            if not re.match(
                r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$",
                email,
            ):
                raise ValueError
        except ValueError:
            if n < TRIES:
                continue
            else:
                sys.exit("Sorry, can't validate your email address.")
        break
    return email


def usage():
    # Ask the user to Add or Search for a tool.
    q1 = [
        inquirer.List(
            "choice",
            message="Would you like to",
            choices=["add a new tool to your toolkit?", "search for a tool to rent?"],
        )
    ]
    wannado = inquirer.prompt(q1)

    # If user wants to add a tool to their toolkit
    if "add" in wannado["choice"]:
        q2 = [inquirer.List("tool", message="Do you want to add", choices=tools)]
        add_tool = inquirer.prompt(q2)
        print(add_tool)
        return add_tool["tool"], "add"

    # If user wants to search for a tool to rent
    elif "search" in wannado["choice"]:
        q3 = [inquirer.List("tool", message="Are you searching for", choices=tools)]
        search_tool = inquirer.prompt(q3)
        return search_tool["tool"]


def rent():
    # Ask user if wants to rent for free or for a fee
    q4 = {
        inquirer.List(
            "rent",
            message="Do you want to",
            choices=["loan it (for free)?", "rent it (for a fee)?"],
        )
    }
    rental = inquirer.prompt(q4)
    if "loan" in rental["rent"]:
        return True


def contact(t):

    # Check if there's a user with the required tool in their toolkit
    contacts = []
    contact_names = []
    with open("contacts.csv") as contact_file:
        for line in contact_file:
            if t in line:
                name, email, tool, fee = line.rstrip().split(",")
                contacts.append(
                    {"name": name, "email": email, "tool": tool, "fee": fee}
                )
    for contact_name in contacts:
        contact_names.append(f"{contact_name['name']} = {contact_name['fee']} USD")
    if contact_names == []:
        return None

    # Select a user from all users with the tool in their toolkit, to contact and rent their tool
    else:
        q5 = {
            inquirer.List(
                "contact",
                message=f'This is a list of users that own "{t}". Who would you like to contact?',
                choices=contact_names,
            )
        }
        user, _ = inquirer.prompt(q5)["contact"].split(" = ")
        for match in contacts:
            if user == match["name"]:
                return [match["name"], t, match["fee"], match["email"]]


def price():

    # If not for free, define a price for "one day rent", in the required format
    n = 0
    while n < TRIES:
        try:
            q6 = input("How much would you like to charge for one day rent?: USD ")
            n += 1

            # Check if input is currency formatted
            if not re.match(r"^\d+(\.\d\d?)?$", q6):
                raise ValueError
        except ValueError:
            if n < TRIES:
                continue
            else:
                sys.exit("Sorry, you need to enter a valid amount.")
        break
    return q6


if __name__ == "__main__":
    main()
