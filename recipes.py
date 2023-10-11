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
    if len(title) > 60:
        raise ValueError("Title is too long")
    if persons > 10 or persons == None:
        raise ValueError("Too many people")
    if not ingredients:
        raise ValueError("There are no ingredients")
    
    return {
        'title': title,
        'persons': persons,
        'ingredients': ingredients,
        'tags': tags
    }