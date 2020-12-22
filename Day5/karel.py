content = open('data.t', 'r').read()

passes = content.split()
biggest_ID = 0

for code in passes:
	pass_ID = 0
	for i in range(10):
		if code[i] == "B" or code[i] == 'R':
			pass_ID += pow(2, 9-i)
	if pass_ID > biggest_ID:
		biggest_ID = pass_ID

print(biggest_ID)