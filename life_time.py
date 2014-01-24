import datetime

today = datetime.date.today()
birthdat = datetime.date(1990,4,27)
life = today - birthdat
print(life.days)
