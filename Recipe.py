class Recipe:
    ID = "000-aaa-000-aaa"
    name = "dev_recipe"
    description = "Lorem Impus"
    ingredients = ["Test_ingredient1"]
    author = "dev"

    def __init__(self, ID, name, description, ingredients, author):
        self.ID = ID
        self.name = name
        self.description = description
        self.ingredients = ingredients
        self.author = author

    def add_ingredient(self, ingredient):
        if ingredient not in self.ingredients:
            self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)

    def update_ingredient(self, old_ingredient, new_ingredient):
        if old_ingredient in self.ingredients:
            index = self.ingredients.index(old_ingredient)
            self.ingredients[index] = new_ingredient

    @property
    def full_recipe(self):
        return f"{self.name}\n{self.description}\n{', '.join(self.ingredients)}\n{self.author}"  # noqa: E501

    @full_recipe.setter
    def full_recipe(self, new):
        self.name, self.description, self.ingredients, self.author = new.split('\n')

recipes =[
Recipe("000-aaa-000-aaa", "dev_recipe", "Lorem Impus", ["Test_ingredient1"], "dev"), # noqa: E501
Recipe("000-aaa-000-aab", "dev_recipe", "Lorem Impus", ["Test_ingredient1"], "dev"),# noqa: E501
Recipe("000-aaa-000-aac", "dev_recipe", "Lorem Impus", ["Test_ingredient1"], "dev"),# noqa: E501
Recipe("000-aaa-000-aad", "dev_recipe", "Lorem Impus", ["Test_ingredient1"], "dev")] # noqa: E501

def add_recipe():
    ID = input("Введите ID: ")
    name = input("Введите название рецепта: ")
    description = input("Введите описание: ")
    ingredients = input("Введите ингредиенты (через запятую): ").split(", ")
    author = input("Введите автора: ")

    recipes.append(Recipe(ID, name, description, ingredients, author))


def show_recipes():
    for i, recipe in enumerate(recipes, start=1):
        print(f"\nРецепт {i}:\n{recipe}\n{'-' * 30}")


def update_recipe():
    show_recipes()
    index = int(input("Введите номер рецепта для обновления: ")) - 1
    if 0 <= index < len(recipes):
        recipes[index].name = input("Введите новое название: ")
        recipes[index].description = input("Введите новое описание: ")
        recipes[index].ingredients = input("Введите новые ингредиенты (через запятую): ").split(", ")
        recipes[index].author = input("Введите нового автора: ")
        print("Рецепт обновлен!")
    else:
        print("Некорректный номер.")

def delete_recipe():
    show_recipes()
    index = int(input("Введите номер рецепта для удаления: ")) - 1
    if 0 <= index < len(recipes):
        del recipes[index]
    else:
        print("Некорректный номер.")





#recipes[1].add_ingredient("New_ingredient")
#recipes[3].update_ingredient("Test_ingredient1", "Updated_ingredient")
#recipes[0].remove_ingredient("New_ingredient")

