def readFile(input_name): 
    return [l.strip() for l in open(input_name, "r").readlines()]

def shouldChange(limit, seat, adj):
    if seat == "#" and adj.count("#") >= limit: return "L"
    if seat == "L" and not "#" in adj: return "#"
    return seat

# Could be more than 2x faster. Was lazy to do it
def part1(d):
    rlength = len(d[0]) + 2
    prev = ["*" * rlength] * 2
    for x in d:
        prev.insert(-1, "*" + x + "*")
    
    change = True
    while change:
        actuall, occupied = ["*" * rlength] * 2, 0
        for i in range(1, len(prev) - 1):
            row = "*"
            for j in range(1, rlength - 1):
                row += shouldChange(4, prev[i][j], [prev[i+1][j],   prev[i-1][j],
                                                     prev[i][j+1],   prev[i][j-1],
                                                     prev[i+1][j+1], prev[i-1][j-1],
                                                     prev[i+1][j-1], prev[i-1][j+1]])

            row += "*"
            occupied += row.count("#")
            actuall.insert(-1, row)
        if prev == actuall: change = False
        prev = actuall
    return occupied

def notEmpty(seat):
    return seat == "L" or seat == "#" or seat == "*"

#In Hungary, this what's called a lumberjack solution.. It's not a positive saying
def part2(d):
    rlength = len(d[0]) + 2
    prev = ["*" * rlength] * 2
    for x in d:
        prev.insert(-1, "*" + x + "*")
    
    change = True
    while change:
        actuall, occupied = ["*" * rlength] * 2, 0
        for i in range(1, len(prev) - 1):
            row = "*"
            for j in range(1, rlength - 1):
                can_see = []
                for r in range(j+1, rlength):
                    if notEmpty(prev[i][r]):
                        can_see.append(prev[i][r])
                        break
                for l in range(j-1, 0, -1):
                    if notEmpty(prev[i][l]):
                        can_see.append(prev[i][l])
                        break
                for d in range(i+1, len(prev)):
                    if notEmpty(prev[d][j]):
                        can_see.append(prev[d][j])
                        break
                for u in range(i-1, 0, -1):
                    if notEmpty(prev[u][j]):
                        can_see.append(prev[u][j])
                        break
                se = i
                for rd in range(j+1, rlength):
                    se += 1
                    if notEmpty(prev[se][rd]):
                        can_see.append(prev[se][rd])
                        break
                se = i 
                for ru in range(j+1, rlength):
                    se -= 1
                    if notEmpty(prev[se][ru]):
                        can_see.append(prev[se][ru])
                        break
                se = i
                for ld in range(j-1, 0, -1):
                    se += 1
                    if notEmpty(prev[se][ld]):
                        can_see.append(prev[se][ld])
                        break
                se = i
                for lu in range(j-1, 0, -1):
                    se -= 1
                    if notEmpty(prev[se][lu]):
                        can_see.append(prev[se][lu])
                        break
                row += shouldChange(5, prev[i][j], can_see)
            row += "*"
            occupied += row.count("#")
            actuall.insert(-1, row)
        if prev == actuall: change = False
        prev = actuall
    return occupied

def main():
    data = readFile("day11.txt")
    print(part1(data))
    print(part2(data))

if __name__ == "__main__":
    main()
