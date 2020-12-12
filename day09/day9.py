def readFile(input_name):
    return [int(l) for l in open(input_name, "r").readlines()]

def checkPreamble(pr, x):
    for i in range(len(pr)):
        for j in range(len(pr)):
            if pr[i] + pr[j] == x and i != j: return True
    return False

def part1(d):
    pr1 = 0
    for pr2 in range(25, len(d)):
        preamble = d[pr1:pr2]
        if not checkPreamble(preamble,d[pr2]):
            return d[pr2]
        pr1 += 1
    return "No solution!"

def part2(d, lf):
    size = 2
    while size < len(d) - 2:
        for i in range(len(d)):
            cont_set = d[i:i + size]
            if sum(cont_set) == lf:
                return min(cont_set) + max(cont_set)
        size += 1
    return "No solution!"

def main():
    data = readFile("day9.txt")
    p1 = part1(data)
    p2 = part2(data, p1)
    print(p1)
    print(p2)

if __name__ == "__main__":
    main()
