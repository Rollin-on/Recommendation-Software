# Recommendation-Software
This program is designed to allow the user to search for a recipe they would like to cook based on their desired cuisine in our Cookbook.

The purpose of this program technically was to demonstrate usage and understanding of the following skills/data structures; Trie Data Structure, DFS, DictReader, Iteration, Dictionaries, Lists, Parsing, User Input, Print statement formating, and readability.

recipes_data.csv
________________
Holds the data for Cookbook project in CSV format

recipe_book.py
______________

This file holds the Trie structure, in this case the Trie structure saves the first character from the "Cuisine" value as a branch of the root node. Each following character in each word continues in a horizontal fashion until the last letter of the word has been reached. The final node of each branch holds a list of dictionaries that contain the associated cuisine spelled out by its branch. At this point a full cuisine name must be entered for the search.

A DFS algorithm is used to complete the prefix search. The DFS function takes over from where the search left off, traverses to the end of the branch, and appends the found data to the end of the result list located within the search function. 

The last function in this file parses the data in our recipes_data.csv, and instantiates a Trie to load the data into

user_interface.py
_________________

Contained within this file is a greeting that is initialized when the file is ran.

Additional user inputs are placed within two functions, one being the initial cuisine request.
After cuisine is requested a search is done on the trie data structure using the Search() and DFS() functions.
Following the search user is given a list of recipes that coincide with their choice of cuisine. Then user is offered a chance to view the details of one of the recipes previously listed by typing the recipe they would like to view. The final portion of this program prompts the user to either search again, or to conclude their search. This prompt serves the purpose of repeating the cookbook search process, or ending the program with a farewell message. 

