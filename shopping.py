def remember_the_milk(shopping_list):
    if not shopping_list:
        return []
    
    if 'milk' not in shopping_list:
        shopping_list.append('milk')
    return shopping_list

def clean_list(shopping_list):
    final_list = []

    if not shopping_list:
        return []

    for index, item in enumerate(shopping_list, start=1):
        if 'milk' not in shopping_list:
            shopping_list.append('milk')
        cleaned_item = item.strip().rstrip().capitalize()
        formatted_item = f"{index}/ {cleaned_item}"
        final_list.append(formatted_item)

    return final_list