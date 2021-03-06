''' 21 game '''

import random
comp_point = 0
user_point = 0

while True:
	point = 0
	ch = random.choice('uc')
	if ch == 'u':
		print('Start User')
		while True:
			while True:
				end = 4
				if point > 18:
					end = 22 - point
				user = input("please input number (1-3): ")

				if user.isdigit():
					user = int(user)
					if 0<user<end:
						print('User',point,'+',user,'=',point+user)
						point+=user
						break
					else:
						print('gri 1 -',end-1)	

				else:
					print('gri tiv')	

			if point == 21:
				comp_point += 1
				print('Comp Win')
				break
			comp = 4 - point % 4	
			print('Comp',point,'+',comp,'=',point+comp)
			point+=comp
	else:
		print('Start Comp')


		while True:	
			if point % 4 == 0:
				comp = random.randint(1,3)	
			else:	
				comp = 4 - point % 4	
			if point == 20:
				comp = 1	
			print('Comp',point,'+',comp,'=',point+comp)
			point+=comp
			if point == 21:
				user_point += 1
				print('Win User')
				break

			while True:
				end = 4
				if point > 18:
					end = 22 - point
				user = input("please input number (1-3): ")

				if user.isdigit():
					user = int(user)
					if 0<user<end:
						print('User',point,'+',user,'=',point+user)
						point+=user
						break
					else:
						print('gri 1 -',end-1)	

				else:
					print('gri tiv')

			if point == 21:
				print('Comp Win')
				comp_point += 1
				break
	if comp_point == 3:
		print('Finish Win Comp','Comp',comp_point,'User',user_point)
		break
	elif user_point == 3:
		print('Finish Win User','Comp',comp_point,'User',user_point)
		break