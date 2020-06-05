import datetime as dt
import pytz

# tz = pytz.timezone('Europe/Moscow')

tz = dt.timezone(dt.timedelta(hours=+3))
just_datetime = dt.datetime.now()
result = just_datetime.astimezone(tz)
print(result)