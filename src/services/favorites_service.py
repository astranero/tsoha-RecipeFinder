from repositories.favorites_repository import (
    favorites_repository as default_favorites_repository)


class FavoriteService:
    def __init__(self, repository=default_favorites_repository):
        self._repository = repository

    def add_to_favorites(self, user_id, recipe_id):
        if not self.check_if_favorite(user_id, recipe_id):
            return self._repository.add_to_favorites(user_id, recipe_id)
        return False

    def get_user_favorites(self, user_id):
        return self._repository.get_user_favorites(user_id)

    def remove_from_favorites(self, user_id, recipe_id):
        return self._repository.remove_from_favorites(user_id, recipe_id)

    def check_if_favorite(self, user_id, recipe_id):
        return bool(self._repository.check_if_favorite(user_id, recipe_id))


favorite_service = FavoriteService()