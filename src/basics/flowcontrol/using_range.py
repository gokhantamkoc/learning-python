# range function can generate numbers. range(10)  will generate numbers from 0 to 9.

num = range(10)

for a in num:
	print(a)

# range can be used like range(start, stop, step_size)

entry = 0
last = 20
step_size = 2

for count in range(entry, last, step_size):
	print(count)

# great range example

food = ['sushi', 'pizza', 'pasta']

for index in range(len(food)):
	print('I love', food[index])

# for loop with else and the break statement

# when a for loop exhausts(finishes), else statement will be executed.

for index in range(len(food)):
	print('I love', food[index])
else:
	print('with sauce')
	print('and nothing else')

# break statement prevents to execute the else statement.

for index in range(len(food)):
	break
	print('I love', food[index])
else:
	print('with sauce')
	print('and nothing else')
