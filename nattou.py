import datetime
today = datetime.datetime.now()
print(today)

if today.weekday() < 5:
	print('Fight!')
elif today.weekday() == 4:
	print('do slowlly')
else:
	print('holyday')
