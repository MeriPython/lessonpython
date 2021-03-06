# num1 = int(input('Number: '))
# num2 = int(input('Number: '))

# if num1 >= num2:
# 	start = num1
# else:
# 	start = num2

# while True:
# 	if start%num1 == 0 and start%num2==0:
# 		print(start)
# 		break
# 	start+=1





# even = 0
# odd = 0

# for i in range(1,102):
# 	if i%2==0:
# 		evem+=1
# 	else:
# 		odd+=1

# print(evem,odd)




# x,y = 0,1

# while x<40:
# 	print(x)
# 	x,y = y,x+y


# tiv = 0
# tar = 0
# string = 'python 3.99'

# for i in string:
# 	if i.isdigit():
# 		tiv+=1
# 	elif i.isalpha():
# 		tar+=1

# print(tiv,tar)






# num = int(input('Number: '))
# count = 0

# for i in str(num):
# 	count+=int(i)
# print(count)



# num = int(input('Number: '))
# count = 1

# for i in range(1,num+1):
# 	count*=i
# print(count)


import math
import time
x=int(input('Number: '))
start = time.time()



for i in range(2,math.ceil(x**0.5)):
	if x%2==0:
		print('No')
		break
else:
	print('Parz e')


end = time.time()

print(end-start)








