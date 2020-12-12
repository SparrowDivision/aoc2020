def readFile(input_name):
    return [l.strip() for l in open(input_name, "r").readlines()]

def bagRules(d):
    rules = {}
    for x in d:
        bag_type, content = x.split(" bags contain ")
        rules[bag_type] = []
        if "no" not in content:
            in_bagtype = content.split(", ")
            for y in in_bagtype:
                count, attr, col, temp = y.split(" ")
                rules[bag_type] += ([attr + " " + col] * int(count))
    return rules

def part1(r, lf = "shiny gold"):
    contain = set()
    for bag_type, content in r.items():
        if lf in content:
            contain.add(bag_type)
            contain.update(part1(r, bag_type))
    return contain

def part2(r, lf = "shiny gold"):
    counter = 0
    for x in r[lf]:
        counter += 1 + part2(r, x)
    return counter

def main():
    rules = bagRules(readFile("day7.txt"))
    print(len(part1(rules)))
    print(part2(rules))

if __name__ == "__main__":
    main()
