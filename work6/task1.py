from datetime import datetime, time

local_datetime = datetime.now()
print(local_datetime)
times = time(hour=7)
result = datetime.combine(local_datetime.date(), times, tzinfo=local_datetime.tzinfo)
a = datetime.today().date()
print(a)
print(result)