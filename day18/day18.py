def readFile(input_name): 
    with open(input_name) as f:
        return [[int(c) if c.isdigit() else c for c in l.strip().replace(" ", "")] for l in f.readlines()]

def getParenthes(line):
    for i in range(len(line)):
        if line[i] == "(": first = i
        elif line[i] == ")": return (first, i)
    return (0, i)

def calculateSlice(part):
    value = part[0] if isinstance(part[0], int) else part[1]
    for i in range(len(part)):
        if part[i] == "*": value *= part[i + 1]
        elif part[i] == "+": value += part[i + 1]
    return value

def additionFirst(part, i = 1):
    while "+" in part:
        if part[i] == "+":
            add = part.pop(i - 1) + part.pop(i)
            part.pop(i - 1), part.insert(i - 1, add)
            i -= 1
        i += 1
    return calculateSlice(part)

def calculateLine(line1):
    line2 = line1.copy()
    while len(line1) > 1:
        i, j = getParenthes(line1)
        part_value1 = calculateSlice([line1.pop(i) for k in range(j + 1 - i)])
        part_value2 = additionFirst([line2.pop(i) for k in range(j + 1 - i)])
        line1.insert(i, part_value1), line2.insert(i, part_value2)
    return line1[0], line2[0]

def main():
    data = readFile("day18.txt")
    part1, part2 = 0, 0
    for line in data:
        temp = calculateLine(line)
        part1 += temp[0]
        part2 += temp[1]
    print(part1, part2)

if __name__ == "__main__":
    main()
