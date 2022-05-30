DROP TABLE IF EXISTS Users CASCADE;
DROP TABLE IF EXISTS Recipes CASCADE;
DROP TABLE IF EXISTS IngredientCategory CASCADE;
DROP TABLE IF EXISTS Ingredients CASCADE;
DROP TABLE IF EXISTS RecipeIngredients CASCADE;
DROP TABLE IF EXISTS Quantity CASCADE;
DROP TABLE IF EXISTS Measurements CASCADE;
DROP TABLE IF EXISTS Favorites CASCADE;

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
    cook_time TIME,
    instructions TEXT,
);

CREATE TABLE IF NOT EXISTS Favourites (
    user_id INTEGER REFERENCES Users (id),
    recipe_id INTEGER REFERENCES Recipes (id)
    UNIQUE(user_id, recipe_id)
);

CREATE TABLE IF NOT EXISTS IngredientCategory (
    id SERIAL PRIMARY KEY,
    category_name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS Ingredients (
    id INTEGER PRIMARY KEY,
    ingredient_name TEXT UNIQUE,
    category_id INTEGER REFERENCES IngredientCategory (id)
);

CREATE TABLE IF NOT EXISTS RecipeIngredients (
    recipe_id INTEGER REFERENCES Recipes,
    ingredient_id INTEGER REFERENCES Ingredients (id),
    UNIQUE(recipe_id, ingredient_id)
);

CREATE TABLE IF NOT EXISTS Quantity (
    quantity_id PRIMARY KEY,
    recipe_id INTEGER REFERENCES Recipes (id),
    ingredient_id INTEGER REFERENCES Ingredients (id),
    measurement_id INTEGER REFERENCES Measurements (id),
    ingredient_quantity FLOAT
);

CREATE TABLE IF NOT EXISTS Measurements (
    id PRIMARY KEY,
    measurement_name TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS Favorites (
    user_id INTEGER REFERENCES Users (id)
    recipe_id INTEGER REFERENCES Recipes (id)
)


