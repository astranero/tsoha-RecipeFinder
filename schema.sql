DROP TABLE IF EXISTS Users CASCADE;
DROP TABLE IF EXISTS Recipes CASCADE;
DROP TABLE IF EXISTS IngredientCategory CASCADE;
DROP TABLE IF EXISTS FoodCategory CASCADE;
DROP TABLE IF EXISTS Tags CASCADE;
DROP TABLE IF EXISTS RecipeTags CASCADE;

CREATE TABLE IF NOT EXISTS Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE CHECK(username IS NOT NULL AND length(username) > 3),
    password TEXT CHECK(password IS NOT NULL AND length(password) > 7),
    role INTEGER,
    phone_number TEXT,
    email TEXT
);

CREATE TABLE IF NOT EXISTS Recipes (
    id SERIAL PRIMARY KEY,
    recipe_name TEXT UNIQUE,
    description TEXT,
    instructions TEXT,
    prep_time TIME,
    cook_time TIME,
    food_category INTEGER REFERENCES FoodCategory (id)
);

CREATE TABLE IF NOT EXISTS IngredientCategory (
    id SERIAL PRIMARY KEY,
    category_name TEXT
);

CREATE TABLE IF NOT EXISTS FoodCategory (
    id SERIAL PRIMARY KEY,
    category_name TEXT
);

CREATE TABLE IF NOT EXISTS Tags (
    Tag_id INTEGER PRIMARY KEY,
    Tag_name TEXT CHECK(Tag_name IS NOT NULL AND length(Tag_name) > 1),
    ingredient_category INTEGER REFERENCES IngredientCategory (id)
);

CREATE TABLE IF NOT EXISTS RecipeTags (
    Recipe_id INTEGER REFERENCES Recipes,
    Tag_id INTEGER REFERENCES Tags,
    UNIQUE(Recipe_id, Tag_id)
);

