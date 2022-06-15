from repositories.recipe_ingredients_repository import (
    recipe_ingredients_repository as default_recipe_ingredients_repository)

class RecipeIngredientsService:
    def __init__(self, repository=default_recipe_ingredients_repository):
        self._repository = repository

    def add_ingredient_to_recipe(self, recipe_id, ingredient_id):
        return self._repository.add_ingredient_to_recipe(recipe_id, ingredient_id)

    def check_if_ingredient_added_to_recipe(self):
        pass

    def get_all_recipes_with_ingredient_id(self):
        pass

    def get_all_ingredients_with_recipe_id(self):
        pass

recipe_ingredients_service = RecipeIngredientsService()