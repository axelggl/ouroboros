import datetime as dt

def build_menu(recipes: list[dict], start_date: dt.date) -> list[tuple[dt.date, str]]:
    menu = []
    current_date = start_date
    
    for recipe in recipes:
        title = recipe['title']
        menu.append((current_date, title))
        current_date += dt.timedelta(days=1)

    return menu