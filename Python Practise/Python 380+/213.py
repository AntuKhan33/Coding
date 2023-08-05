import datetime

d1=datetime.date(2021,1,1)
print(d1)
t1=datetime.time(12,0,0 )
print(t1)
dt1 = datetime.datetime(2020, 7, 20, 11, 30, 0)
print(dt1)
d2=datetime.date(2020,7,21)
diff=(d2-d1).days
print(diff)
from datetime import datetime
dt1 = datetime(2021, 4, 20, 11, 30, 00)
print(dt1.strftime('%Y-%d-%m'))
import datetime
today = datetime.date.today()
end_of_year=datetime.date(today.year,12,31)
print((today-end_of_year).days)
dt = datetime.datetime(2020, 1, 1)

print(dt + datetime.timedelta(days=7))

dt = datetime.datetime(2020, 1, 1)
delta = datetime.timedelta(hours=8)

dates = [dt + i * delta for i in range(12)]

for date in dates:
    print(date)


