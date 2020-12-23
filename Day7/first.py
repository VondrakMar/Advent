# I am not proud of this
f = open("data.t","r")
rules = {}
for line in f:
    a = line.split("contain")
    rules[a[0]] = a[1][:-1]

IsPossible = []
new = ["shiny gold bag"]
new2 = []
old = 0
while True:
    for k,v in rules.items():
        for a in new:
            if a in v:
                if k not in IsPossible:
                    IsPossible.append(k)
                if k[-2] == "s":
                    new2.append(k[:-2])
                else:
                    new2.append(k)
    if len(new2) == 0:
        break
    new = new2
    new2 = []

print(len(IsPossible))
