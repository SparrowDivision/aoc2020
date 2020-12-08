def readFile(input_name):
    return [l.strip() for l in open(input_name, "r").readlines()]

def findNum(i):
    value = ""
    for x in i:
        if x.isdigit(): value +=x
    if value == "": return -1
    return int(value)

def checkHgt(hgt):
    val = findNum(hgt)
    if "cm" in hgt and 150 <= val and val <= 193:
        return True
    elif "in" in hgt and 59 <= val and val <= 76:
        return True
    return False

def checkHcl(col):
    allowed = ("a", "b", "c", "d", "e", "f")
    if col[0] != "#" or len(col) != 7: return False
    for x in col[1:]:
        if not x.isdigit() and not x in allowed: return False
    return True

def checkPid(pid):
    if len(pid) == 9 and pid.isdigit():
        return True
    return False

def checkEcl(col):
    if col in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"): return True
    return False

def matchGroup(pp):
    pp = pp + " "
    tmp1, tmp2 = "", ""
    fields = {}
    for x in pp[1:]:
        if x == ":":
            tmp1 = tmp2
            tmp2 = ""
        elif x == " ":
            fields[tmp1] = tmp2
            tmp2 = ""
        else: tmp2 += x   
    return fields

def validFields(pp):
    pp_r = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": lambda x: checkHgt(x),
    "hcl": lambda x: checkHcl(x),
    "ecl": lambda x: checkEcl(x),
    "pid": lambda x: checkPid(x)
    }
    for field, rule in pp_r.items():
        if not rule(pp[field]): return False        
    return True

def checkFields(pp):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in fields:
        if field not in pp: return False
    return True

def day1(d):
    counter, passp = 0, ""
    for x in d:
        if x == "" and checkFields(passp):
            counter += 1
            passp = ""
        else: passp += x
    return counter

def day2(d):
    counter, passp = 0, ""
    for x in d:
        if x == "" and checkFields(passp):
            if validFields(matchGroup(passp)): counter += 1
            passp = ""
        else: passp += " " + x
    return counter

def main():
    data = readFile("day4.txt")
    print(day1(data))
    print(day2(data))

if __name__ == "__main__":
    main()
