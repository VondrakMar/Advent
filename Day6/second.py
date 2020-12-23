abeceda = "abcdefghijklmnopqrstuvwxyz"
f = open("data.t","r").read()
b = f.split("\n")
groups = [""]
numbers = []
gc = 0
line = 0
for a in b:
    if a == "":
        groups.append("")
        numbers.append(line)
        gc += 1
        line = 0
    else:
        groups[gc] += a
        line += 1
count = 0
groups = groups[:-1]
print(groups)
print(numbers)
for letter in abeceda:
    for group in range(len(groups)):
            number = 0
            for let in groups[group]:
                if let == letter:
                    number += 1
            if number == numbers[group]:
                count += 1

print(count)