f = open("Day11.t", "r")
numbers = []
for line in f:
    numbers.append(int(line))

for a in numbers:
    for b in numbers:
        for c in numbers:
            if (a != b and a != c and b != c):
                if (a + b + c) == 2020:
                    print(a*b*c)
                    break