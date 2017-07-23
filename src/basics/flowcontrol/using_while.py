# while [test expression]
#	[Body of while]

numbers = [1, 56, 19, 27]
sum = 0

count = 0
while count < len(numbers):
	sum += numbers[count]
	count += 1

print('sum: ', sum)

# with else

counter = 0

while counter < 3:
	print('Inside while')
	counter += 1
else:
	print('Inside else')

