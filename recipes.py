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
    # Check title length
    if len(title) > 40 or title is None:
        raise ValueError("Title is too long")

    # Check persons
    if persons is None or persons <= 0 or persons > 20:
        raise ValueError("Invalid persons number")

    # Check ingredients
    if not ingredients or ingredients[0] is None:
        raise ValueError("This recipe has no ingredient")
    
    # Return the recipe as a dictionary
    return {
        'title': title,
        'persons': persons,
        'ingredients': ingredients,
        'tags': tags
    }
