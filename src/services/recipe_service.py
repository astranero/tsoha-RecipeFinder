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
        return self._repository.add_ingredient_to_recipe(ingredient_id, recipe_id)

    def get_recipe_id(self, recipe_name):
        return self._repository.get_recipe_id(recipe_name)

    def get_recipe_order_by_oldest(self):
        return self._repository.get_recipe_order_by_oldest()

    def get_recipe_order_by_newest(self):
        return self._repository.get_recipe_order_by_newest()

    def get_recipe_order_by_review(self):
        return self._repository.get_recipe_order_by_review()
    
    def get_recipe_order_by_name(self):
        return self._repository.get_recipe_order_by_name()
    
    def get_recipe_details(self):
        return self._repository.get_recipe_details()

    def get_recipe_with_id(self, recipe_id):
        return self._repository.get_recipe_with_id(recipe_id)

    def get_recipe_ingredients_with_id(self, recipe_id):
        return self._repository.get_recipe_ingredients(recipe_id)

    def delete_recipe(self, id):
        return self._repository.delete_recipe(id)

    def search_by_name(self, query):
        min_ratio = 80
        results = []
        for recipe in self._repository.get_recipes_for_search():
            if fuzz.WRatio(query, recipe.recipe_name) >= min_ratio:
                results.append(recipe)
        return results

    def modify_ingredients(self, recipe_id, ingredient_name):
        self._repository.modify_recipe_ingredients(recipe_id, ingredient_name)

    def modify_recipe(self, recipe_id, recipe_name, cook_time, description, instructions):
        return self._repository.modify_recipe(recipe_id, recipe_name, cook_time, description, instructions)

recipe_service = RecipeService()