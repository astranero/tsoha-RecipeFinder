from repositories.review_repository import (
    review_repository as default_review_repository)

class ReviewService:
    def __init__(self, repository=default_review_repository):
        self._repository = repository

    def create_review(self, review, comment, user_id, recipe_id):
        if self.check_if_user_already_reviewed_recipe(recipe_id, user_id):
            return False
        return self._repository.create_review(review, comment, user_id, recipe_id)

    def get_recipe_reviews(self, recipe_id):
        return self._repository.get_recipe_reviews(recipe_id)

    def get_average_for_reviews(self, recipe_id):
        return self._repository.get_average_for_reviews(recipe_id)

    def check_if_user_already_reviewed_recipe(self, recipe_id, user_id):
        return bool(self._repository.check_if_user_already_reviewed_recipe(recipe_id, user_id))

review_service = ReviewService()
