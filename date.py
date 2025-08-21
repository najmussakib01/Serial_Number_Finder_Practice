from datetime import datetime
def realtime_date():
    current_date = datetime.now()
    day = current_date.day
    month = current_date.month
    year = current_date.year
    print(f"{day:02d}-{month:02d}-{year}")