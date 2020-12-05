import re

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def is_valid(passport):
	for field in fields:
		if not re.search(field + ':', passport):
			return 0
	return 1

content = open('input.txt', 'r').read()
passports = re.split('\n\n',content)
count = 0

for passport in passports:
	if is_valid(passport):
		print(passport + '\n')
		count += 1	

print(count)
