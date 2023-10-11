import datetime as dt

def with_current_date(function):
    def modified_function(message: str, current_date=None):
        if current_date is None:
            current_date = dt.date.today()

        return function(message, current_date)
    
    return modified_function