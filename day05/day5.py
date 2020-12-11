def readFile(input_name): 
    return [l.strip() for l in open(input_name, 'r').readlines()]

def getID(r,c):
    return r*8+c

def getRowOrCol(rc,mode):
    if mode == "r":
        rc, i, j, lf = rc[:7], 0, 127, "B"
    else:
        rc, i, j, lf = rc[7:], 0, 7, "R"
        
    for x in rc:
        if x == lf:
            i = (j+(i+1))//2
        else:
            j = (i+j)//2
    return i
    
def part1(d):
    maxID = 0
    for x in d:
        currentID = getID(getRowOrCol(x,"r"), getRowOrCol(x,"c"))    
        if maxID < currentID:
            maxID = currentID
    return maxID  

def part2(d):
    seatIDs = []
    for x in d:
        currentID = getID(getRowOrCol(x,"r"), getRowOrCol(x,"c"))    
        seatIDs.append(currentID)
    seatIDs.sort()

    for i in range(0,len(seatIDs)-1):
        if seatIDs[i+1] - seatIDs[i] == 2:
            return seatIDs[i]+1
 
def main():
    data = readFile("day5.txt")
    print(part1(data))
    print(part2(data))

if __name__ == "__main__":
    main()
