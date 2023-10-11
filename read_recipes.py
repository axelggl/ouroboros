import json

def get_recipes(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            recipes_data = json.load(file)
        return recipes_data
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON in '{file_name}'.")
    except OSError:
        print(f"File '{file_name} not found.'")
    return []