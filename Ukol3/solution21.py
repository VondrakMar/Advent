import re

def is_valid(line):
	arr = re.split("-|:*\s", line)
	minimum = int(arr[0])
	maximum = int(arr[1])
	count = arr[3].count(arr[2])
	return 1 if minimum <= count <= maximum else 0

f = open('input.txt', 'r')

valid_count = 0
for line in f:
	if is_valid(line):
		valid_count += 1

print(valid_count)