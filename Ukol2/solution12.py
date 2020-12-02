f = open('input.txt', 'r')
r = open('output2.txt', 'w')
content = f.read()

arr = list(map(int,content.split()))	
len_arr = len(arr)

for i in range(len_arr):
	for j in range(i + 1, len_arr):
		for k in range(j + 1, len_arr):
			if arr[i] + arr[j] + arr[k] == 2020:
				print(arr[i] * arr[j] * arr[k])
