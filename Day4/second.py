f = open("data.t")
def checkValid(passport):
    try:
        if int(passport["byr"]) >= 1920 and int(passport["byr"]) <= 2002:
            if int(passport["iyr"]) >= 2010 and int(passport["iyr"]) <= 2020:
                if int(passport["eyr"]) >= 2020 and int(passport["eyr"]) <= 2030:  
                    if ((passport["hgt"][-2:] == "cm" and int(passport["hgt"][:-2]) <= 193 and int(passport["hgt"][:-2]) >= 150) or 
                    (passport["hgt"][-2:] == "in" and int(passport["hgt"][:-2]) <= 76 and int(passport["hgt"][:-2]) >= 59)):
                        if passport["hcl"][0] == "#" and len(passport["hcl"]) == 7:
                            if passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                                if len(passport["pid"]) == 9:
                                    return True
        else:
            return False
    except:
        return False
ide = {}
count = 0
for line in f:
        now = line.split()
        if now == []:
            if checkValid(ide):
                count += 1
            ide = {}
        else:
            for a in now:
                b = a.split(":")
                ide[b[0]] = b[1]
        
print(count)

