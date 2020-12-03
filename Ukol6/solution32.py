f = open('input.txt', 'r')

content = f.read()

grid = content.split()
row_length = len(grid[0])

trees_count = [0,0,0,0,0]

for i in range(len(grid)):
	if grid[i][i % row_length] == '#':
		trees_count[0] += 1
	if grid[i][3 * i % row_length] == '#':
		trees_count[1] += 1
	if grid[i][5 * i % row_length] == '#':
		trees_count[2] += 1
	if grid[i][7* i % row_length] == '#':
		trees_count[3] += 1
	if i%2 == 0 and grid[i][int(i / 2 % row_length)] == '#':
		trees_count[4] += 1

result = 1

for count in trees_count:
	result *= count

print(result)