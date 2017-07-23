# if [test expression]
# 	statement(s)

count = 10

if count < 1:
	print('count is less than 1')
else:
	print('count is equal or greater than 1')

# Python interprets non-zero values as True. 'None' and zero(0) are interpreted as false.

if None:
	print('testing None')
else:
	print('In Python, None is by default false')

if 0:
	print('testing zero')
else:
	print('In Python, zero(0) is by default false')


# 'elif' is 'else if'.

if None:
	print('testing None')
elif count < 1:
	print('count is less than 1')
else:
	print('count is equal or greater than 1')

# if-elif statements can have inner if-elif statements



