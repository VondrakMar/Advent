f = open ("Day2.t","r")
seznam = []
for line in f:
    if line[-1] == "\n":
        seznam.append(line[:-1])
    else:
        seznam.append(line)

new = []
for a in seznam:
    new.append(a.split())

for a in range(len(new)):
    new[a][1] = new[a][1][:-1]

sum = 0
for i in new:
    numbers = i[0].split("-")
    if ((i[2][int(numbers[0])-1] == i[1] and i[2][int(numbers[1])-1] != i[1]) or 
    (i[2][int(numbers[0])-1] != i[1] and i[2][int(numbers[1])-1] == i[1])):
        sum += 1

print(sum)


