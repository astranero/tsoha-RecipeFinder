from thefuzz import fuzz
from repositories.recipe_repository import (
    recipe_repository as default_recipe_repository)

class RecipeService:
    def __init__(self, repository=default_recipe_repository):
        self._repository = repository

    def create_recipe(self, recipe_name, description, cook_time, instructions):
        if not self._repository.check_if_recipe_name_exist(recipe_name):
            return self._repository.create_recipe(recipe_name, description, cook_time, instructions)
        return False

    def add_ingredient_to_recipe(self, ingredient_id, recipe_id):
        if not self._repository.check_if_ingredient_in_recipe(recipe_id):
            return self._repository.add_ingredient_to_recipe(ingredient_id, recipe_id)
        return False

    def get_recipe_id(self, recipe_name):
        return self._repository.get_recipe_id(recipe_name)

    def get_recipe(self):
        return self._repository.get_recipe()

    def get_recipe_with_id(self, recipe_id):
        return self._repository.get_recipe_with_id(recipe_id)

    def get_recipe_ingredients_with_id(self, recipe_id):
        return self._repository.get_recipe_ingredients(recipe_id)

    def delete_recipe(self, id):
        return self._repository.delete_recipe(id)

    def search_by_name(self, query):
        """Returns reading tips that contain title similar to given query from db.
        """
        min_ratio = 80
        results = []
        for recipe in self._repository.get_recipe():
            if fuzz.WRatio(query, recipe.recipe_name) >= min_ratio:
                results.append(recipe)
        return results

recipe_service = RecipeService()