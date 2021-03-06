def readFile(input_name):
    return [l.strip() for l in open(input_name, "r").readlines()]

def part1(d):
    valid = 0
    for x in d:
        x = x.split(" ")
        minc, maxc = x[0].split("-")
        lf = x[1].strip(":")
        pw = x[2].strip("\n")
        actual = 0
        for y in pw:
            if (y == lf):
                actual += 1
        if (int(minc) <= actual and actual <= int(maxc)):
            valid += 1
    return valid

def part2(d):
    valid = 0
    for x in d:
        x = x.split(" ")
        i, j = x[0].split("-")
        lf = x[1].strip(":")
        pw = x[2].strip("\n")
        i, j = int(i) - 1, int(j) - 1
        if ((pw[i] == lf or pw[j] == lf) and not (pw[i] == lf and pw[j] == lf)):
            valid += 1
    return valid

def main():
    data = readFile("day2.txt")
    print(part1(data))
    print(part2(data))

if __name__ == "__main__":
    main()
