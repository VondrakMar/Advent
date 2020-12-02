f = open('input.txt', 'r')
r = open('output2.txt', 'w')
content = f.read()

arr = list(map(int,content.split()))	

lower = [ num for num in arr if num < 1010 ]
higher = [ num for num in arr if num > 1010 ]

for num1 in lower:
	for num2 in higher:
		if num1 + num2 == 2020:
			print(num1 * num2)
