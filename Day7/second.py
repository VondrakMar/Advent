# I am not proud of this
f = open("try2.t","r")
rules = {}
for line in f:
    a = line.split("contain")
    rules[a[0]] = a[1][:-1]

current = ["shiny gold bag"]
zkusit = [[],[]]
for k,v in rules.items():
    spl1 = v.split(",")
    for a in spl1:
        b = a.split()
        for i in b:
            try:
                zkusit[0].append(int(i))
            except:
                zkusit[1].append(i)

print(zkusit)

