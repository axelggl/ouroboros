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
    if len(title) > 50:
        raise ValueError("Title is too long")
    if len(title) is None:
        raise ValueError('Invalid title')
    if persons <= 0:
        raise ValueError("Invalid persons number")
    if persons > 20:
        raise ValueError("Too many persons")
    if persons is None:
        raise ValueError('Invalid number of people')
    if not ingredients:
        raise ValueError("Ingredient list cannot be empty")
    
    return {
        'title': title,
        'persons': persons,
        'ingredients': ingredients,
        'tags': tags
    }
