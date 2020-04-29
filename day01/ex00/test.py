#!/usr/bin/python3

from book import Book
from recipe import Recipe


pie = Recipe("pie",
             3,
             45,
             ["flour", "eggs", "milk"],
             "dessert")
pasta = Recipe("pasta",
               1,
               20,
               ["flour", "eggs"],
               "lunch")
sandwich = Recipe("sandwich",
                  1,
                  5,
                  ["bread", "ham", "cheese"],
                  "lunch")
mybook = Book("Cool Recipes")
mybook.add_recipe(pie)
mybook.add_recipe(pasta)
mybook.add_recipe(sandwich)
mybook.get_recipe_by_name("pasta")
mybook.get_recipes_by_type("lunch")
