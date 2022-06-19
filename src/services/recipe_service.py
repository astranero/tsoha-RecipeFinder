from repositories.recipe_repository import (
    recipe_repository as default_recipe_repository)

class RecipeService:
    def __init__(self, repository=default_recipe_repository):
        self._repository = repository

    def create_recipe_name_and_id(self, recipe_name):
        return self._repository.create_recipe_name_and_id(recipe_name)

    def add_details_to_recipe(self, description, cook_time, instructions, recipe_id ):
        return self._repository.add_details_to_recipe(description, cook_time, instructions, recipe_id)

    def add_ingredient_to_recipe(self, ingredient_id, recipe_id, ):
        return self._repository.add_ingredient_to_recipe(ingredient_id, recipe_id)
    
    def get_recipe_id(self, recipe_name):
        return self._repository.get_recipe_id(recipe_name)

    def get_recipe(self):
        return self._repository.get_recipe()

    def delete_recipe(self, id):
        return self._repository.delete_recipe(id)

recipe_service = RecipeService()