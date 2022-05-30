from thefuzz import fuzz
from database import (db as default_db)
from entities.recipe import Recipe

class RecipeRepository:
    def __init__(self, db=default_db):
        self._db = db

    def create_recipe(self, reading_tip_object):
        pass

    def get_all_recipes(self):
        sql = "SELECT * FROM Recipes"

    def modify_recipe(self):
        pass

    def delete_recipe(self):
        pass

    def create_recipe_from_result(self, result_row):
        pass

    def create_recipes_from_results(self, result_rows):
        pass

    def search_by_title(self, query):
        pass
recipe_repository = RecipeRepository()