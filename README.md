# Three-Ships

Quick Notes:

1. you can run the program stand-alone by downloading the main.exe file in the dist folder, otherwise, you can run it in your python ide from main.py
2. virus scan may take issue with the .exe, I promise this is not a virus

3. the user can create a character from the create button
4. to edit or delete a character, highlight it in the table then press edit or delete.
5. to play a match press "play match" and select two different characters, the wins and losses will be updated on submit and all matches can be viewed in the "past matches" section

Known limitations/bugs:
due to the time constraint, some areas and design decisions are  not where I want them to be, below are things I noticed in testing that I did not have time to fix
1. the edit and create function will allow you to put characters in the attack and defense stat despite them being declared as integers in the database
2. you can make characters play themselves, they will receive both a win and a loss. Most of my debug time was spent trying to make a way to block out the selected option from the other box without making two separate pop-out windows.
3. edits made to the starting 4 characters will not persist, but all newly created characters will persist

Biggest challenge:

The biggest challenge for me planning out the tech stack. My initial plan was to build out a react app with a springboot framework, but I would also need to include some form of web hosting to make it easy for the reviewer to experience, and did not want to add unnecessary complexity that I may have to trade off functionality for if there were any unexpected bugs. I also no longer had my preferred IDE since my student license expired. I took some time to plan it out and decided to sacrifice UI in exchange for a database setup. 

Before this, I had never used these particular libraries together so I also had to learn a bit as I went. it was fun to build, but if I were to continue it I would probably end up adding game functionality and more stats for complexity and leaving the UI as is.
