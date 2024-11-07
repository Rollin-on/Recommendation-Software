
#Greets user and directs user input
import recipe_book 

def greeting():
    print('______________________________________________________________')
    print("**************************************************************")
    print("**                                                          **")     
    print("**                Welcome To The Recipe Book!               **")   
    print("**                                                          **")
    print("**************************************************************")
    print("______________________________________________________________")

    print("This Recipe Book will give you recipes based upon what cuisine you would like to eat.")
    print("At any time press '' to close the search")
    
            


def cuisine_type():
    food = input("Please enter the type of cuisine you would like to cook. This can be the full word, or the first few letters, or you may also press enter to view all recipes: ").lower()
    return food

 #Display Recipes, then display recipes based upon search
def display_recipes(cuisine_recipes):
    if not cuisine_recipes:
        print("Sorry there are no recipes that match your choice.")
        return True
    else:
        print("Here are the recipes that our cookbook has under that cuisine:")
        recipe_name = [recipe["Recipe"] for recipe in cuisine_recipes]
        for name in recipe_name:
            print(name)

        choice = input("Which recipe would you like to see? ")
        if choice in recipe_name:
            for recipe in cuisine_recipes:
                if choice in recipe.values():
                    print_recipes_details(recipe)
                
                

def print_recipes_details(recipe):
    print(f"\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"{recipe["Recipe"]}")
    print(f"Cook Time: {recipe["Cook Time"]}")
    print(f"Servings: {recipe["Servings"]}")
    print(f"Ingredients: {recipe["Ingredients"]}")
    print(f"\nInstructions: {recipe["Instructions"]}")
    print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def second_search():
    again = input("Would you like to search another cuisine? ").lower()
    if again == "yes":
        return True
    elif again == "no":
        print("Thank you for using the cookbook! Goodbye!")
        return False
    else:
        print("Invalid Input. Redirecting to main search")
        
    


def main():
    greeting()
    recipe_book.cookbook("recipes_data.csv")
    
    while True:
        cuisine = cuisine_type()
        cuisine_recipes = recipe_book.trie.search(cuisine)
        display_recipes(cuisine_recipes)
        if not second_search():
            break
if __name__ == "__main__":
    main()