import re

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def is_valid(passport):
	for field in fields:
		match = re.search(field + ':.+?\s|' + field + ':.+$', passport)
		if match:
			entry = match.group()[4:].strip()
			if field == 'byr':
				if int(entry) < 1920 or int(entry) > 2002:
					return 0
			if field == 'iyr':
				if int(entry) < 2010 or int(entry) > 2020:
					return 0
			if field == 'eyr':
				if int(entry) < 2020 or int(entry) > 2030:
					return 0
			if field == 'hgt':
				measurement = entry[-2:]
				amount = int(entry[:-2])
				if not ((measurement == 'in' and 59 <= amount <= 76) or (measurement == 'cm' and 150 <= amount <= 193)):
					return 0
			if field == 'hcl':
				if not re.search('^#[0-9a-f]{6}$', entry):
					return 0
			if field == 'ecl':
				colors = ['amb', 'blu', 'brn', 'gry' ,'grn' ,'hzl' ,'oth']
				if not colors.count(entry):
					return 0
			if field == 'pid':
				if not re.search('^\d{9}$', entry):
					return 0
		else:
			return 0		 
	return 1

content = open('input.txt', 'r').read()
passports = re.split('\n\n',content)
count = 0

for passport in passports:
	if is_valid(passport):
		count += 1	

print(count)
