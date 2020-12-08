def readFile(input_name): 
    with open(input_name, "r") as f:
        return list(map(int, f.readlines()))
    
def day1(a):
    for x in a:
        for y in a:
            if (x + y == 2020):
                return x*y

def day2(a):          
    for x in a:
        for y in a:
            for z in a:
                if (x + y + z == 2020):
                    return x*y*z
    
def main():
    data = readFile("day1.txt")
    print(day1(data))
    print(day2(data))

if __name__ == "__main__":
    main()
