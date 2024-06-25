def create_christmas(height, interval):
	print(' ' * (height - 1) + 'X')   # line 1
	print(' ' * (height - 1) + '^')   # line 2
	decor_index = 0
	for branch in range(height - 1):
		spaces = (height - 2 - branch) * ' '
		num_stars = (branch * 2 + 1)
		stars = []
		for index in range(1, num_stars + 1):
			if index % 2 == 0:
				if decor_index % interval == 0:
					stars.append('O')
				else:
					stars.append('*')
				decor_index += 1
			else:
				stars.append('*')
		stars = ''.join(stars)
		row = spaces + '/' + stars + '\\'
		print(row)
	print(' ' * (height - 2) + '| |')   # last line
	return None


def check_input(height, interval):
	if height < 3:
		print('The height must be at least 3.')
		return False
	if interval <= 0:
		print('The interval must be greater than zero.')
		return False
	return True


if __name__ == '__main__':
	check_input_result = None
	while check_input_result is not True:
		user_input = input().split()
		height, interval = int(user_input[0]), int(user_input[1])
		check_input_result = check_input(height, interval)
	create_christmas(height, interval)



