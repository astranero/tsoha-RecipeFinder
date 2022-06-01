from repositories.basket_repository import (
    basket_repository as default_basket_repository)

class BasketService:
    def __init__(self, repository=default_basket_repository):
        self._repository = repository

    def add_to_basket(self, user_id, ingredient_id):
        return self._repository.add_to_basket(user_id, ingredient_id)

    def remove_ingredient_from_basket(self, user_id, ingredient_id):
        self._repository.remove_ingredient_from_basket(user_id, ingredient_id)

    def get_all_ingredients_in_basket_with_user_id(self, user_id):
        pass


basket_service = BasketService()