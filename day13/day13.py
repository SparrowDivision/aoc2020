def readFile(input_name): 
    l = open(input_name, "r").readlines()
    return int(l[0]), [int(x) if x.isdigit() else x for x in l[1].split(",")]

def part1(target_time, buses):
    buses.discard("x")
    current_time, busID = target_time - 1, 0
    while not busID:
        current_time += 1
        for x in buses:
            if current_time % x == 0: busID = x
    return (current_time - target_time) * busID

def part2(buses):
    modBus = {}
    for i, b in enumerate(buses):
        if b != "x": modBus[b] = -i % b
    buses = list(modBus.keys())
    i = time = buses[0]
    for x in buses[1:]:
        while time % x != modBus[x]:
            time += i
        i *= x
    return time

def main():
    time, buslist = readFile("day13.txt")
    print(part1(time, set(buslist)))
    print(part2(buslist))

if __name__ == "__main__":
    main()
