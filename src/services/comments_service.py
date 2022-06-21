from repositories.comments_repository import (
    comments_repository as default_comments_repository)

class CommentsService:
    def __init__(self, repository=default_comments_repository):
        self._repository = repository

    def add_comment(self):
        pass

    def delete_comment(self):
        pass

    def get_comments(self):
        pass

comments_service = CommentsService()