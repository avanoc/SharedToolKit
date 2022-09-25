# Shared Tool Kit
#### Video Demo:  <https://youtu.be/jDCwzsNmIU0>
#### Description:
Shared Tool Kit was born at a family lunch, when we were discusing how useless is to have several tools that are really expensive and bearly used. My brother-in-law came up with this idea of a community of people who are willing to share or rent their tools, so I’m trying to make his wish come true. I wrote this basic python code hopping it can grow further on.

#### Here’s how it works:
First, it calls 2 functions: **name** and **mail**, to prompt every user to input their name and email address. These functions validate that the name contains only alphabetic characters by calling isalpha on the input, and that the email is a valid address, by the means of a well-known regular expression.

Then, it can go 2 ways, by calling the function **usage**:

1. if the user wants to * *add* * a tool to their own toolkit to rent/share it, it would ask which tool and if they want to share it for free or rent it for a fee. This information gets stored in a csv file, along with their name and email address.
To achieve this, the program calls 2 additional functions: **rent** and **price**. 

2. if the user wants to * *search* * for a tool, it would ask which tool they need and loop through the csv file to return all proper matches with their prices. Then the user only has to decide who they want to contact, and the program would return the contact information.
In this case, the only function that’s needed to be called is **contact**.

File input/output is managed by standard techniques and * *CSV library* *.

I profit from the * *inquirer library* * to make the user choose from a list in several functions, in order to simplify input validation.

All but main functions were tested with pytest.
I had to learn how to mock input, and to recreate all functions with inquirer methods, to be able to run pytest on them.


#### Design choices:
I had to narrowed the list of tools available to a 5 items list, because I didn't want to make it more complicated than it needed to be for this "Final Project" task. 
My original idea was to make a list of dictionaries in a separate file, with every tool I could find, each with the category it belongs to as a key. 
```[{"hand tool": "hammer"}, {"painting tool": "airbrush"}, etc]```

Another thing I struggled with was that at first I made all my while loops as "while True", but testing them with pytest, I realised that incorrect input would never break out of the loop, so I decided to give it a * *TRIES* * tries (in this case 10) to get a correct input, before exiting explaining what went wrong.

I used **black** to format both * *project.py* * and *test_project.py* *.


#### Conclusion:
This may be a very basic code, but it's a starting point to what I think, will become something great.
I'm confident this small program will someday grow into a very useful app.
I hope you enjoy reading and playing with it. :hugs:
