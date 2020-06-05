import datetime as dt

def get_datetime(just_datetime):
    if just_datetime.date() == dt.datetime.now().date():
        time = just_datetime - dt.timedelta(days=1, hours=3, minutes=15)
        return time
    else:
        return just_datetime