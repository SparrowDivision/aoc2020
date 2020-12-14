def readFile(input_name, output = []):
    for line in open(input_name, "r").readlines():
        x, y = line.strip().split(" = ")
        if y.isdigit(): x, y = int(x[4:-1]), "{0:036b}".format(int(y))
        output.append((x, y))
    return output

def maskValue(mask, value, mode, masked = ""):
    for m, v in zip(mask, value):
        masked += v if m == mode else m
    return masked

def getVariations(m):
    xcount = m.count("X")
    length = "{0:0" + str(xcount) + "b}"
    return [(length.format(i)) for i in range(2 ** xcount)]

def part1(d):
    memory = {}
    for address, value in d:
        if address == "mask": mask = value
        else: memory[address] = int(maskValue(mask, value, "X"), 2)
    return sum(memory.values())

def part2(d):
    memory = {}
    for address, value in d:
        if address == "mask": mask = value
        else:
            masked = maskValue(mask, "{0:036b}".format(address), "0")
            for var in getVariations(masked):
                idx, newaddress = 0, ""
                for m in masked:
                    if m.isdigit(): newaddress += m
                    else:
                        newaddress += var[idx]
                        idx += 1
                memory[int(newaddress, 2)] = int(value, 2)
    return sum(memory.values())

def main():
    data = readFile("day14.txt")
    print(part1(data))
    print(part2(data))

if __name__ == "__main__":
    main()
