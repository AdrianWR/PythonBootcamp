#!/usr/bin/python3


class InputError(Exception):
    def __init__(self, description):
        self.description = description


class Recipe(object):
    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, recipe_type, description=""):
        self.name = name
        if cooking_lvl not in range(1, 5):
            raise InputError("Cooking level not in available range.")
        self.cooking_lvl = cooking_lvl
        if cooking_time < 0:
            raise InputError("Negative cooking times aren't accepted.")
        self.cooking_time = cooking_time
        if not isinstance(ingredients, list) or not all(
               isinstance(i, str) for i in ingredients):
            raise InputError("Ingredients must be input by string list.")
        self.ingredients = ingredients
        if recipe_type not in ["starter", "lunch", "dessert"]:
            raise InputError("Recipe type not available.")
        self.recipe_type = recipe_type
        self.description = description

    def __str__(self):
        """Returns the recipe information to be used as
           a string. Can be used to print purposes.
        """
        s = f"\nRecipe for {self.name}:\n"
        s += f"Difficulty level: {self.cooking_lvl} out of 5.\n"
        s += f"Takes {self.cooking_time} minutes of cooking.\n"
        s += f"Ingredients list: {self.ingredients}.\n"
        if (len(self.description)):
            s += f"Description : {self.description}\n"
        s += f"To be eaten for {self.recipe_type}."
        return s
