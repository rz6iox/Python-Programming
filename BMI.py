#coding:utf-8

while True:
	height = raw_input('身長(m)?:')
	if len(height) == 0:
		break
	height = float(height)
	weight = float(raw_input('体重(kg)?:'))
	bmi = weight / pow(height,2)

	print('BMI値は%0.1f です。'% bmi)
	if bmi < 18.5:
		print('少し痩せすぎです')
	elif 18.5 <= bmi <25.0:
		print('普通です')
	elif 25 <= bmi < 30:
		print('少し太ってます')
	else:
		print('肥満です')
