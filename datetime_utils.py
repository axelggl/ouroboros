import datetime as dt

def parse_time(time_str: str) -> dt.datetime:
    return dt.datetime.strptime(time_str, "%d/%m/%Y")

def format_date(date: dt.date) -> str:
    return dt.date.strftime(date, "%A %d %B %Y")
