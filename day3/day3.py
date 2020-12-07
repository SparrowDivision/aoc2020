def readFile(input_name):
    return [l.strip() for l in open(input_name, 'r').readlines()]

def day1(d):
    x, y, tree_count = 0, 0, 0
    while x + 1 < len(d):
        x += 1
        y += 3
        check_point = d[x][y % len(d[x])]
        if check_point == "#": tree_count += 1
    return tree_count
    
def day2(d):
    slope = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    multip = 1
    for s in slope:
        x, y, tree_count = 0, 0, 0
        while x + 1 < len(d):
            x += s[1]
            y += s[0]
            check_point = d[x][y % len(d[x])]
            if check_point == '#':
                tree_count += 1  
        multip *= tree_count
    return multip
    
def main():
    data = readFile('day3.txt')  
    print(day1(data))
    print(day2(data))

if __name__ == "__main__":
    main()
    
