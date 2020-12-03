f = open('input.txt', 'r')

content = f.read()

grid = content.split()
row_length = len(grid[0])

trees_count = 0

for i in range(len(grid)):
	if grid[i][3 * i % row_length] == '#':
		trees_count += 1

print(trees_count)