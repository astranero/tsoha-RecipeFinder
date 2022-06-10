DROP TABLE IF EXISTS Users CASCADE;
DROP TABLE IF EXISTS IngredientCategory CASCADE;
DROP TABLE IF EXISTS Ingredients CASCADE;
DROP TABLE IF EXISTS Recipes CASCADE;
DROP TABLE IF EXISTS Favorites CASCADE;
DROP TABLE IF EXISTS RecipeIngredients CASCADE;

CREATE TABLE IF NOT EXISTS Users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE CHECK(username IS NOT NULL AND length(username) > 3),
    password TEXT CHECK(password IS NOT NULL AND length(password) > 7),
    role INTEGER,
    phone_number TEXT,
    email TEXT
);

CREATE TABLE IF NOT EXISTS IngredientCategory (
    id SERIAL PRIMARY KEY,
    category_name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS Ingredients (
    id SERIAL PRIMARY KEY,
    ingredient_name TEXT UNIQUE,
    category_id INTEGER REFERENCES IngredientCategory (id)
);

CREATE TABLE IF NOT EXISTS Recipes (
    id SERIAL PRIMARY KEY,
    recipe_name TEXT UNIQUE,
    decription TEXT,
    cook_time TEXT,
    instructions TEXT
);

CREATE TABLE IF NOT EXISTS RecipeIngredients (
    recipe_id INTEGER REFERENCES Recipes,
    ingredient_id INTEGER REFERENCES Ingredients (id),
    UNIQUE(recipe_id, ingredient_id)
);

CREATE TABLE IF NOT EXISTS Favorites (
    user_id INTEGER REFERENCES Users (id),
    recipe_id INTEGER REFERENCES Recipes (id),
    UNIQUE(user_id, recipe_id)
);

CREATE TABLE IF NOT EXISTS Basket (
    user_id INTEGER REFERENCES Users (id),
    ingredient_id INTEGER REFERENCES Ingredients (id),
    UNIQUE(user_id, ingredient_id)
);