import datetime as dt

now = dt.datetime.now()
year = now.year
print(now)
wd = now.weekday()
print(f"Day in week {wd}")
print(f"Week in Year {now.isocalendar().week}")
birth_date = dt.datetime(year=1964, month=8, day=5)
print(birth_date)



