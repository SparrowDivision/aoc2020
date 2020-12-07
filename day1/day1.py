def readFile(input_name): 
    with open(input_name, "r") as f:
        adat = list(map(int, f.readlines()))
    return adat

def part1(a):
    for x in a:
        for y in a:
            if (int(x) + int(y) == 2020):
                return x*y

def part2(a):          
    for x in a:
        for y in a:
            for z in a:
                if (x + y + z == 2020):
                    return x*y*z
    
def main():
    adat = readFile("day1.txt")
    print(part1(adat))
    print(part2(adat))

if __name__ == "__main__":
    main()
