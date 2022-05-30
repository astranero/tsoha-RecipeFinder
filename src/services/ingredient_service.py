from repositories.ingredient_repository import (
    ingredient_repository as default_ingredient_repository)

class IngredientService:
    def __init__(self, repository:default_ingredient_repository):
        self._repository = repository

    def create_ingredient(self, ingredient_name):
        if self.check_if_ingredient_exists(ingredient_name):
            return False
        return self._repository.create_ingredient(ingredient_name)

    def check_if_ingredient_exists(self, ingredient_name):
        return self._repository.check_if_ingredient_exists(ingredient_name)

    def get_all_ingredients_in_category(self, category_name):
        return self._repository.get_all_ingredients_in_category(category_name)

