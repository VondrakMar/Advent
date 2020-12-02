f = open("Day11.t", "r")
numbers = []
for line in f:
    numbers.append(int(line))

for a in numbers:
    for b in numbers:
        if a != b:
            if (a + b) == 2020:
                print(a*b)