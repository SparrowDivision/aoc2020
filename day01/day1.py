def readFile(input_name):
    with open(input_name, "r") as f:
        return list(map(int, f.readlines()))

def part1(d):
    for x in d:
        for y in d:
            if x + y == 2020:
                return x * y

def part2(d):
    for x in d:
        for y in d:
            for z in d:
                if x + y + z == 2020:
                    return x * y * z

def main():
    data = readFile("day1.txt")
    print(part1(data))
    print(part2(data))

if __name__ == "__main__":
    main()
