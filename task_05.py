from datetime import datetime, timedelta

def date_in_future(days):
    if not isinstance(days,int):
        return datetime.now().strptime('%d-%m-%Y %H:%M:%S')

    now = datetime.now() # date now

    future_date = now + timedelta(days = days)
    return future_date.strftime('%d-%m-%Y %H:%M:%S')


print(date_in_future(2))