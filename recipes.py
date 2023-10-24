    def create_recipe(name, persons, ingredients):
    if len(name) > 150: 
        raise ValueError("Title is too long")
    if persons is None or persons == 0 or persons > 50:
        raise ValueError("Invalid persons number")
    if not ingredients:
        raise ValueError("This recipe has no ingredients")

    recipe_data = {
        'title': name,
        'persons': persons,
        'ingredients': ingredients
        }

    return recipe_data

def create_recipe_v2(title, persons, *ingredients, **tags):
    recipe = {
        'title': title,
        'persons': persons,
        'ingredients': ingredients,
        'tags': tags
    }
    if len(recipe['title'])>150:
        raise ValueError("Title is too long")
    if recipe['persons']==False or recipe['persons']>50:
        raise ValueError("Invalid persons number")
    if not len(recipe['ingredients']):
        raise ValueError("This recipe has no ingredients")
    return recipe