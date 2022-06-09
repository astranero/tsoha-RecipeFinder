from repositories.ingredient_category_repository import (
    ingredient_category_repository as default_ingredient_category_repository)


class IngredientCategoryService:
    def __init__(self, repository=default_ingredient_category_repository):
        self._repository = repository

    def create_category(self, category_name):
        print(self.get_all_categories())
        return self._repository.create_ingredient_category(category_name)

    def get_all_categories(self):
        return self._repository.get_all_categories()

ingredient_category_service = IngredientCategoryService()