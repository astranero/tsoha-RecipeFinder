DROP TABLE IF EXISTS Users CASCADE;
DROP TABLE IF EXISTS Recipes CASCADE;
DROP TABLE IF EXISTS Favorites CASCADE;
DROP TABLE IF EXISTS Ingredients CASCADE;
DROP TABLE IF EXISTS RecipeDetails CASCADE;

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
    cook_time TEXT,
    instructions TEXT
);

CREATE TABLE IF NOT EXISTS Ingredients (
    id SERIAL PRIMARY KEY,
    ingredient_name TEXT,
    recipe_id INTEGER REFERENCES Recipes (id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Favorites (
    user_id INTEGER REFERENCES Users (id) ON DELETE CASCADE,
    recipe_id INTEGER REFERENCES Recipes (id) ON DELETE CASCADE,
    UNIQUE(user_id, recipe_id)
);

CREATE TABLE IF NOT EXISTS Comments (
    id SERIAL PRIMARY KEY,
    comment TEXT,
    user_id INTEGER REFERENCES Users(id) ON DELETE CASCADE,
    recipe_id INTEGER REFERENCES Recipes (id) ON DELETE CASCADE,
    sent_at TIMESTAMP
);