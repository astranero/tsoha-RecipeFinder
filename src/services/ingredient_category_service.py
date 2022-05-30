from repositories.ingredient_category_repository import (
    ingredient_category_repository as default_ingredient_category_repository)


class IngredientCategoryService:
    def __init__(self, repository=default_ingredient_category_repository):
        self._repository = repository

    def create_category(self, category_name):
        return self._repository.create(category_name)

    def get_categories(self):
        return self._reading_tip_repository.get_all_categories()

ingredient_category_service = IngredientCategoryService()