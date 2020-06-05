from datetime import date, timedelta

dt = date.today() + timedelta(days=time_shift)
result = dt.isocalendar()[1]
print(result)
