#!/usr/bin/python3

from datetime import datetime
from recipe import Recipe


class InputError(Exception):
    def __init__(self, description):
        self.description = description


class Book(object):
    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {"starter": [],
                             "lunch": [],
                             "dessert": []}
        pass

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        all_recipes = sum(self.recipes_list.values(), [])
        result = [i for i in all_recipes if name == i.name]
        if len(result) == 0:
            print("No results found.")
        else:
            for i in result:
                print(str(i))
        pass

    def get_recipes_by_type(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        try:
            for i in self.recipes_list[recipe_type]:
                print(str(i))
        except KeyError:
            print("Recipe type not available.")
        pass

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        try:
            if not isinstance(recipe, Recipe):
                raise InputError("Not a valid recipe.")
            self.recipes_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()
        except InputError as e:
            print(e)
        pass
