cookbook = {
    "sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}


def print_recipe(recipe):
    try:
        print(f"\nRecipe for {recipe}:")
        print(f"Ingredients list: {cookbook[recipe]['ingredients']}")
        print(f"To be eaten for {cookbook[recipe]['meal']}.")
        print(f"Takes {cookbook[recipe]['prep_time']} minutes of cooking.")
    except KeyError:
        print("Recipe not found on the cookbook.")


def delete_recipe(recipe):
    try:
        del cookbook[recipe]
        print(f"\nRecipe {recipe} removed from the cookbook.")
    except KeyError:
        print(f"Recipe not found on this cookbook.")


def add_recipe(name, ingredients, meal, prep_time):
    try:
        new_recipe = {
            "ingredients": ingredients,
            "meal": meal,
            "prep_time": prep_time
        }
        cookbook[name] = new_recipe
    except TypeError:
        print("Something is missing to input your recipe.")


def print_all_recipes():
    print(*cookbook.keys(), sep=", ")


if __name__ == "__main__":
    option = ''
    while option != '5':
        print("Please select an option by typing the corresponding number:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")
        option = input()
        if option == '1':
            print("\nTo add a new recipe input its name,")
            print("its ingredients (separated by commas),")
            print("which meal and its preparation time.\n")
            name = input("Name: ")
            ingredients = input("List of ingredients: ")
            ingredients = ingredients.split(',')
            meal = input("Meal: ")
            prep_time = input("Preparation time (min): ")
            add_recipe(name, ingredients, meal, prep_time)
        elif option == '2':
            print("\nEnter the recipe's name you want to remove:")
            delete_recipe(input())
        elif option == '3':
            print("\nPlease enter the recipe's name to get its details:")
            print_recipe(input())
        elif option == '4':
            print_all_recipes()
        elif option == '5':
            print("\nCookbook closed.")
        else:
            print("\nInvalid option.")
            print("Please select a number option from the list.")
            print("To exit, press 5.")
        input()
