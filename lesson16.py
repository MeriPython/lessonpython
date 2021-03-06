# import random
# python_team = ['Meri','Albert','Arsho','Sargis','Razmik','Arnak']

# random.shuffle(python_team)

# count = 1
# for i,j in zip(python_team[:3],python_team[3:]):
# 	print(count, i,j)
# 	count += 1





# thisdict = {'name':'Meri','year':2000}
# print(thisdict)


# thisdict = {'name':'Aram','year':1994}
# thisdict['year'] = 2014
# print(thisdict)



# thisdict = {'name':'Aram','year':1994}
# thisdict['age'] = 20
# print(thisdict)


# thisdict = {'name':'Aram','year':1994}
# del thisdict['year']
# print(thisdict)



# person = dict(name='Sargis',year=17,color='white',country='Vagharshapat')

# for i in person:
# 	print(person[i])

# for i in person:
# 	print(i)

# for i,j in person.items():
# 	print(i,j)

# for i in person.values():
# 	print(i)




# import datetime

# person = {'name':'Meri','year':20,'color':'white','village':'Argavand'}

# x = datetime.datetime.now()

# print(x.year-person['year'])



# person = {'name':'Meri','year':20,'color':'white','village':'Argavand'}

# count=0

# for i in person:
# 	count+=1
# print(count)




# person = {'name1':'Meri','name2':'Arsen','name3':'Miki','name4':'Arsen'}
# count=0

# if 'Arsen' in person.values():
# 	for i in person.values():
# 		if i == 'Arsen':
# 			count+=1

# 	print('yes',count)
# else:
# 	print('No')





# my_list = ['Ani','Ani','Aram']
# c = []
# for i in my_list:
# 	if my_list.count(i)>1:
# 		pass
# 	else:
# 		c.append(i)
# print(c)



''' Validators '''
login = input('Login: ')
print('Ok, this will be your login')


chars = ('!','@','#','$','%','&','*')


while True:
	password = input('Password: ')
	num_count = 0
	char_count = 0
	if len(password) < 8:
		print('Your password is less than 8')
		continue

	for i in password:
		if i in chars:
			char_count+=1
		elif i.isdigit():
			num_count+=1

	if char_count<3:
		print('Password must have 3 chars')
		continue
	elif num_count<4:
		print('Password must have 4 numbers')
		continue

	else:
		print('Ok, Your password is safe')
		break


while True:
	phonnum = input('Phon number: ')
	
	if len(phonnum)<9:
		print('Input correct phone number')
		continue
	for x in phonnum:
		if x.isalpha():
			print('Input only numbers')
			continue

	else:
		print('Your phone is true')
		break



while True:
	email = input('Mail: ')

	if len(email) < 10:
		print('Enter correct mail')
		continue

	for y in email:
		



