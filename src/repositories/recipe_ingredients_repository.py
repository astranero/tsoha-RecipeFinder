from db import (db as default_db)

class RecipeIngredientsRepository:
    """All database operations related to TipTags table
    """

    def __init__(self, db=default_db):
        self._db = db

    def add_ingredient_to_recipe(self, recipe_id, tag_id):
        sql = "INSERT INTO RecipeTags (recipe_id, tag_id) VALUES (:recipe_id, :tag_id)"

    def check_if_ingredient_added_to_recipe(self, recipe_id, tag_id):
        sql = "SELECT * FROM TipTags WHERE recipe_id=:tip_id AND tag_id=:tag_id", (recipe_id, tag_id)

    def get_all_recipe_ingredient_pairs(self):
        sql = "SELECT * FROM RecipeTags"

    def get_all_recipes_with_ingredient_id(self, tag_id):
        tag_sql = "SELECT * FROM RecipeTags WHERE tag_id=:tag_id"
        recipe_sql = "SELECT * FROM ReadingTip WHERE recipe_id=:recipe_id"

    def get_all_ingredients_with_recipe_id(self, recipe_id):
        recipe_sql = "SELECT * FROM RecipeTags WHERE recipe_id=recipe_id"
        tag_sql = "SELECT * FROM Tags WHERE tag_id=:tag_id"

recipe_tags_repository = RecipeIngredientsRepository()