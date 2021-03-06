# names = ['Razmik','Albert','Meri','Sargis','Arsh']

# res = [i for i in names if len(i) == max([len(i) for i in names])]
# print(', '.join(res))


# c = []
# for i in names:
# 	c.append(len(i))
# max_l = max(c)

# for i in names:
# 	if len(i) == max_l:
# 		print(i)



# my_list = [3,3.5,'Meri',True,('Ab',3),['25','ghuj']]
# print(my_list)




# my_list = ['HP','ASUS','DELL','MAC','LENOVO','HP']
# user = input('Model: ').upper()


# if user in my_list:
# 	my_list.count(user)
# 	print('Yes',my_list.count(user))

# else:
# 	print('No')









# chars = ('!','@','#','$','%','&','*')

# while  True:
# 	parol = input('Password:  ')

# 	if len(parol) < 8:
# 		print('Your password length is less than 8')
# 		continue

# 	chars_count = 0	
# 	numbers_count = 0	

# 	for i in parol:
# 		if i in chars:
# 			chars_count+=1
# 		elif i.isdigit():
# 			numbers_count+=1

# 	if chars_count < 2:
# 		print('Your password must be have two chars')
# 		continue

# 	if numbers_count < 2:
# 		print('Your password must be have two numbers')
# 		continue


# 	if parol[0].isalpha() and parol[0].islower():
# 		print('First letter must be upper')
# 		continue

# 	print('Strong password')
# 	break




# link = 'https://www.youtube.com/watch?v=FG60e3tkWF4'

# print(link[link.index('=')+1:])


# count = 0
# for i in link:
# 	count+=1
# 	if i == '=':
# 		break

# print(link[count:])







# word = input('Input a word: ')
# if word == word [::-1]:
# 	print('open')
# else:
# 	print('no')







# list1 = ['Meri','Abo','Abo','Meri']
# list2 = []

# for i in list1:
# 	if i not in list2:
# 		list2.append(i)
# print(list2)






# list1 = [4,3,2,1]
# list2 = []

# for i in list1:
# 	if i %2 == 0:
# 		list2.append(i)
# print(list2)


# for i in list1:
# 	if i%2 == 1:
# 		list1.remove(i)
# print(list1)







