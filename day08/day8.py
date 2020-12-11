def readFile(input_name):
    return [l.strip() for l in open(input_name, "r").readlines()]

def part1(d):
    visited_lines = []
    acc, i = 0, 0
    while i not in visited_lines and i < len(d):
        visited_lines.append(i)
        op, arg = d[i].split(" ")
        if op == "acc":
            acc += int(arg)
            i += 1
        elif op == "jmp":
            i += int(arg)
        else:
            i += 1
    if i == len(d):
        return True, acc
    return False, acc

def part2(d):
    fullrun, i = (False, 0), 0
    while not fullrun[0]:
        s = []
        for j in range(len(d)):
            if j == i:    
                op, arg = d[i].split(" ")
                if op == "jmp":
                    s.append("nop " + arg)
                elif op == "nop":
                    s.append("jmp " + arg)
                else:
                    s.append(d[j])
            else:
                s.append(d[j])
        fullrun = part1(s) 
        i += 1
    return fullrun

def main():
    data = readFile("day8.txt")
    print(part1(data)[1])
    print(part2(data)[1])

if __name__ == "__main__":
    main()
