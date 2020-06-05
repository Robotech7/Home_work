from datetime import datetime, time

local_datetime = datetime.today()
print(local_datetime)
times = time(hour=7)

result = datetime.combine(local_datetime.date(), times)
print(result)