
class Recipe:
    def __init__(self, recipe_id=None, recipe_name=str, description=str, cook_time=str, instructions=str):
        self.recipe_id = recipe_id
        self.recipe_name = recipe_name
        self.description = description
        self.cook_time = cook_time,
        self.instructions = instructions

    def format(self):
        recipe = []
        if self.recipe_id:
            recipe.append(f'{self.recipe_id}')
        if self.recipe_name:
            recipe.append(f'{self.recipe_name}')
        if self.description:
            recipe.append(f'{self.description}')
        if self.cook_time:
            recipe.append(f'{self.cook_time}')
        if self.instructions:
            recipe.append(f'{self.instructions}')
        return ", ".join(recipe)

    def __str__(self):
        return self.format()
