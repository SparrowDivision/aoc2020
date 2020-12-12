def readFile(input_name):
    return [l.strip() for l in open(input_name, "r").readlines()]

def part1(d):
    sumchar, group = 0, ""
    for x in d:
        if x == "":
            sumchar += len(set(group))
            group = ""
        else:
            group += x
    return sumchar    

def part2(d):
    group_size, sumyes, group = 0, 0, ""
    for x in d:
        if x == "":
            for y in set(group):
                occurrence = 0
                for z in (group):
                    if y == z: occurrence += 1
                if occurrence == group_size: sumyes += 1
            group_size, group = 0, ""
        else:
            group_size += 1
            group += x
    return sumyes

def main():
    data = readFile("day6.txt")
    data.append("")
    print(part1(data))
    print(part2(data))

if __name__ == "__main__":
    main()
