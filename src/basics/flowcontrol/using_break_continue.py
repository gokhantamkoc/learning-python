counter = 1

while counter < 20:
	print('check value')
	print(counter)
	counter += 1
	if counter % 5 == 4:
		continue
	if counter % 15 == 0:
		break
else:
	print('Hooray!!')
