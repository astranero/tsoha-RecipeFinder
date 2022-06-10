
class IngredientCategory:
    def __init__(self, category_id=None, category_name=str):
        self.category_id = category_id
        self.category_name = category_name

    def format(self):
        category = []
        if self.category_id:
            category.append(f'{self.category_id}')
        if self.category_name:
            word = str(self.category_name)
            word2 = word.replace("(", "")
            word3 = word2.replace(")", "")
            word4 = word3.replace("'", "")
            word5 = word4.replace(",", "")
            category.append(f'{word}')
        return ", ".join(category)

    def __repr__(self):
        return self.format()