def readFile(input_name): 
    return {int(x): [i+1] for i, x in enumerate(open(input_name, "r").readline().split(","))}

def day15(t):
    d = readFile("day15.txt")
    spoken = list(d)[-1]
    for turn in range(len(d) + 1, t + 1):
        spoken = 0 if len(d[spoken]) < 2 else d[spoken][-1] - d[spoken][-2]
        if not spoken in d.keys(): d[spoken] = []
        d[spoken].append(turn)
    return spoken

def main():
    print(day15(2020), day15(30000000))

if __name__ == "__main__":
    main()
