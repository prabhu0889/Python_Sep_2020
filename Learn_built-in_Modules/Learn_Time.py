# datatime - date, time, datetime and timedelta

import datetime

print(datetime.datetime.now()) # format YYYY-MM-DD HH:MM:SS:MS

print(datetime.date.today())

dt = datetime.datetime(2019, 10, 7)
print(dt)

print(dt.day)
print(dt.month)
print(dt.year)

print(dt.isocalendar())
print(dt.isoweekday())

print('*'*20)
# timedelta:- Manipulate with date and time
td = datetime.date.today()
tdel = datetime.timedelta(days=5)
print(td)
print(td + tdel)    # yyyy/MM/DD

# find no. of days passed in this year
ny = datetime.date(2020, 1, 1)
print('no. of days passed: ',(td - ny).days )

# Date : yy/mm/dd
# time : h : m : s : ms

