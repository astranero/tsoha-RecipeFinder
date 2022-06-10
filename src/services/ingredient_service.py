from repositories.ingredient_repository import (
    ingredient_repository as default_ingredient_repository)

class IngredientService:
    def __init__(self, repository=default_ingredient_repository):
        self._repository = repository

    def create_ingredient(self, ingredient_name, category_id):
        print("moi")
        return self._repository.create_ingredient(ingredient_name, category_id)

    def check_if_ingredient_exists(self, ingredient_name):
        return self._repository.check_if_ingredient_exists(ingredient_name)

    def get_all_ingredients(self):
        return self._repository.get_all_ingredients()
    
    def get_all_ingredients_with_categories(self):
        return self._repository.get_all_ingredients_with_categories()

ingredient_service = IngredientService()


