abeceda = "abcdefghijklmnopqrstuvwxyz"
f = open("data.t","r").read()
b = f.split("\n")
groups = [""]

gc = 0
for a in b:
    if a == "":
        groups.append("")
        gc += 1
    else:
        groups[gc] += a

count = 0
for letter in abeceda:
    for group in groups:
        if letter in group:
            count += 1

print(count)