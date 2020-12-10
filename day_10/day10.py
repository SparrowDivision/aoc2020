def readFile(input_name):
    return [int(l) for l in open(input_name, "r").readlines()]

def addDevice(d):
    d.append(max(d) + 3)
    d.sort()
    return d

def part1(d):
    prev, j1, j3 = 0, 0, 0
    for x in d:
        if x - prev == 1: j1 += 1
        if x - prev == 3: j3 += 1
        prev = x
    return j1 * j3

def part2(d):
    ways = {0:1}
    for x in d:
        ways[x] = 0
        if x - 1 in ways: ways[x] += ways[x-1]
        if x - 2 in ways: ways[x] += ways[x-2]
        if x - 3 in ways: ways[x] += ways[x-3]
    return ways[x]

def main():
    data = addDevice(readFile("day10.txt"))
    print(part1(data))
    print(part2(data))

if __name__ == "__main__":
    main()
