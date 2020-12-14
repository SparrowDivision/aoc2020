def readFile(input_name):
    output = []
    for line in open(input_name, "r").readlines():  
        x, y = line.strip().split(" = ")
        if y.isdigit(): x, y = int(x[4:-1]), f'{int(y):036b}'
        output.append((x, y))
    return output

def part1(d):
    memory = {}
    for address, value in d:
        if address == "mask": mask = value
        else:
            masked = ""
            for m, v in zip(mask, value):
                if m.isdigit(): masked += m
                else: masked += v
            memory[address] = int(masked,2)
    return sum(memory.values())      

def part2(d):
    pass

def main():
    data = readFile("day14.txt")
    print(part1(data))

if __name__ == "__main__":
    main()
