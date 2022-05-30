from repositories.recipe_repository import (
    recipe_repository as default_recipe_repository)

from entities.recipe import Recipe

class RecipeService:
    def __init__(self, repository=default_recipe_repository):
        self._repository = repository

    def create_recipe(self):
        pass

    def check_if_recipe_name_exists(self):
        pass

    def delete_recipe(self):
        pass

    def get_all_recipes(self):
        pass

    def search_by_recipe_name(self, recipe_name):
        pass

    def modify_recipe(self):
        pass

recipe_service = RecipeService()