from repositories.ingredient_category_repository import (
    ingredient_category_repository as default_ingredient_category_repository)

from entities.ingredient_category import IngredientCategory

class IngredientCategoryService:
    def __init__(self, repository=default_ingredient_category_repository):
        self._repository = repository

    def create_category(self, category_name:str):
        category = IngredientCategory(category_name=category_name)
        return self._repository.create(category)

    def get_categories(self):
        return self._reading_tip_repository.get_all_categories()

ingredient_category_service = IngredientCategoryService()