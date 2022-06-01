from repositories.favorites_repository import (
    favorites_repository as default_favorites_repository)


class FavoriteService:
    def __init__(self, repository=default_favorites_repository):
        self._repository = repository

favorite_service = FavoriteService()