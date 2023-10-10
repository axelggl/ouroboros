def day_from_number(day_number):
    day_names = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    if day_number not in day_names:
        return None
    
    return day_names[day_number]

def day_to_number(day):
    day_number = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7
    }

    if day not in day_number:
        return None
    
    return day_number[day]