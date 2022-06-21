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

    def get_recipe_ingredients(self):
        for item in recipe_ids:
            ingredients = self._repository.get_recipe_ingredients(item[0])
        value = []
        for ingredient in ingredients:
            value.append(ingredient[0])
        return ", ".join(value)

    def get_recipe_ingredients_with_id(self, recipe_id):
        return self._repository.get_recipe_ingredients(recipe_id)

    def delete_recipe(self, id):
        return self._repository.delete_recipe(id)

recipe_service = RecipeService()