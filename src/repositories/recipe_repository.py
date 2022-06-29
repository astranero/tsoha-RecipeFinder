
from db import (db as default_db)

class RecipeRepository:
    def __init__(self, db=default_db):
        self._db = db

    def create_recipe(self, recipe_name, description, cook_time, instructions):
        try:
            values_to_db = {"recipe_name":recipe_name,
                            "description":description,
                            "cook_time": cook_time,
                            "instructions":instructions,
                            }
            sql = """INSERT INTO Recipes (recipe_name,
                                            description,
                                            cook_time,
                                            instructions)
                    VALUES (:recipe_name, :description, :cook_time, :instructions)"""
            self._db.session.execute(sql, values_to_db)
            self._db.session.commit()
            return True
        except:
            return False

    def check_if_recipe_name_exist(self, recipe_name):
        sql = """SELECT recipe_name
                FROM Recipes
                WHERE recipe_name=:recipe_name"""
        return bool(self._db.session.execute(sql,
                    {"recipe_name":recipe_name}).fetchall())

    def get_recipe_id(self, recipe_name):
        try:
            sql = """SELECT id
                    FROM Recipes
                    WHERE recipe_name=:recipe_name"""
            return self._db.session.execute(sql,
                    {"recipe_name":recipe_name}).fetchone()[0]
        except:
            return False

    def add_ingredient_to_recipe(self, ingredient_name, recipe_id):
        try:
            values_to_db = {"ingredient_name":ingredient_name,
                        "recipe_id":recipe_id}
            sql = """INSERT INTO Ingredients (ingredient_name, recipe_id)
                        VALUES (:ingredient_name, :recipe_id)"""
            self._db.session.execute(sql, values_to_db)
            self._db.session.commit()
            return True
        except:
            return False

    def get_recipes_for_search(self):
        sql = """SELECT Recipes.id, Recipes.recipe_name, Recipes.cook_time,
                            Recipes.description, Recipes.instructions, ROUND(COALESCE(AVG(Review.rating), 0), 1)
                    FROM Recipes
                    LEFT JOIN Review ON Review.recipe_id = Recipes.id
                    GROUP BY Recipes.id"""
        return self._db.session.execute(sql).fetchall()

    def get_recipe_order_by_oldest(self):
        sql = """SELECT Recipes.id, Recipes.recipe_name, Recipes.cook_time,
                            Recipes.description, Recipes.instructions, ROUND(COALESCE(AVG(Review.rating), 0), 1)
                    FROM Recipes
                    LEFT JOIN Review ON Review.recipe_id = Recipes.id
                    GROUP BY Recipes.id 
                    ORDER BY Recipes.id ASC"""
        return self._db.session.execute(sql).fetchall()

    def get_recipe_order_by_newest(self):
        sql = """SELECT Recipes.id, Recipes.recipe_name, Recipes.cook_time,
                            Recipes.description, Recipes.instructions, ROUND(COALESCE(AVG(Review.rating), 0), 1)
                    FROM Recipes
                    LEFT JOIN Review ON Review.recipe_id = Recipes.id
                    GROUP BY Recipes.id 
                    ORDER BY Recipes.id DESC"""
        return self._db.session.execute(sql).fetchall()


    def get_recipe_order_by_review(self):
        sql = """SELECT Recipes.id, Recipes.recipe_name, Recipes.cook_time,
                            Recipes.description, Recipes.instructions, ROUND(COALESCE(AVG(Review.rating), 0), 1)
                    FROM Recipes
                    LEFT JOIN Review ON Review.recipe_id = Recipes.id
                    GROUP BY Recipes.id 
                    ORDER BY ROUND(COALESCE(AVG(Review.rating), 0), 1) DESC"""
        return self._db.session.execute(sql).fetchall()


    def get_recipe_order_by_name(self):
        sql = """SELECT Recipes.id, Recipes.recipe_name, Recipes.cook_time,
                            Recipes.description, Recipes.instructions, ROUND(COALESCE(AVG(Review.rating), 0), 1)
                    FROM Recipes
                    LEFT JOIN Review ON Review.recipe_id = Recipes.id
                    GROUP BY Recipes.id
                    ORDER BY Recipes.recipe_name ASC"""
        return self._db.session.execute(sql).fetchall()

    def get_recipe_details(self):
        sql = """SELECT Recipes.id, Recipes.recipe_name, COUNT(Review.comment),
                        ROUND(COALESCE(AVG(Review.rating), 0), 1)
                    FROM Recipes
                    LEFT JOIN Review ON Review.recipe_id = Recipes.id
                GROUP BY Recipes.id"""
        return self._db.session.execute(sql).fetchall()


    def get_recipe_with_id(self, recipe_id):
        try:
            sql = """SELECT id, recipe_name, cook_time,
                        description, instructions
                    FROM Recipes
                    WHERE Recipes.id=:recipe_id"""
            return self._db.session.execute(sql,
                        {"recipe_id":recipe_id}).fetchone()
        except:
            return False

    def get_recipe_ingredients(self, recipe_id):
        sql = """SELECT Ingredients.ingredient_name
                FROM Ingredients, Recipes
                WHERE Ingredients.recipe_id = Recipes.id
                AND Recipes.id=:recipe_id"""
        return self._db.session.execute(sql,
                        {"recipe_id":recipe_id}).fetchall()

    def delete_recipe(self, id):
        try:
            sql = """DELETE FROM Recipes WHERE id=:id"""
            self._db.session.execute(sql, {"id":id})
            self._db.session.commit()
        except:
            return False

    def modify_recipe(self, recipe_id, recipe_name, cook_time, description, instructions):
        values_to_db = {"recipe_id":recipe_id,
                        "recipe_name":recipe_name,
                        "cook_time":cook_time,
                        "description": description,
                        "instructions":instructions}
        sql = """UPDATE Recipes
                SET recipe_name=:recipe_name,
                    cook_time=:cook_time,
                    description=:description,
                    instructions=:instructions
                WHERE id=:recipe_id"""
        self._db.session.execute(sql, values_to_db)
        self._db.session.commit()

    def check_if_ingredient_in_recipe(self, recipe_id):
        sql = """SELECT ingredient_name
                FROM Ingredients
                WHERE recipe_id=:recipe_id"""
        return bool(self._db.session.execute(sql,
                        {"recipe_id":recipe_id}).fetchall())

    def modify_recipe_ingredients(self, recipe_id, ingredient_name):
        values_to_db = {"recipe_id":recipe_id,
                        "ingredient_name":ingredient_name}
        sql = """UPDATE Ingredients
                SET ingredient_name=:ingredient_name
                WHERE recipe_id=:recipe_id"""
        self._db.session.execute(sql, values_to_db)
        self._db.session.commit()

recipe_repository = RecipeRepository()

