import re

def is_valid(line):
	arr = re.split("-|:*\s", line)
	first_char = arr[3][int(arr[0]) - 1]
	second_char = arr[3][int(arr[1]) - 1]
	char = arr[2]
	return 0 if (first_char == char and second_char == char
				 or first_char != char and second_char != char) \
		   	 else 1

f = open('input.txt', 'r')

valid_count = 0
for line in f:
	if is_valid(line):
		valid_count += 1

print(valid_count)