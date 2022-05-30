from db import (db as default_db)
from entities.tag import Tag


class TagRepository:
    """All database operations related to Tags
    """

    def __init__(self, db=default_db):
        self._db = db

    def create_tag(self, tag_name):
        sql = "INSERT INTO Tags (Tag_name) VALUES (:tag_name)"

    def check_if_tag_exists(self, tag_name):
        sql = "SELECT tag_name FROM Tags WHERE tag_name =:tag_name"

    def get_all_tags(self):
        sql =  "SELECT tag_name FROM Tags"

    def create_tag_from_result(self, result_row):
        return Tag(tag_name=result_row[0])

    def create_tags_from_results(self, result_row):
        tags = []
        for row in result_row:
            tags.append(self.create_tag_from_result(row))
        return tags

tags_repository = TagsRepository()