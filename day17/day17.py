def readFile(input_name): 
    return [l.strip() for l in open(input_name, "r").readlines()]

def startingCubes(d, dim):
    if dim == 3: return {(i, j, 0): d[i][j] for i in range(len(d)) for j in range(len(d[0]))}
    return {(i, j, 0, 0): d[i][j] for i in range(len(d)) for j in range(len(d[0]))}

def findNeighbors(cb, dim):
    if dim == 3: return [(cb[0] + i, cb[1] + j, cb[2] + k)
                         for i in range(-1, 2) for j in range(-1, 2) for k in range(-1, 2)
                         if not (i == 0 and j == 0 and k == 0) and dim == 3] 
    return [(cb[0] + i, cb[1] + j, cb[2] + k, cb[3] + l)
            for i in range(-1, 2) for j in range(-1, 2)
            for k in range(-1, 2) for l in range(-1, 2)
            if not (i == 0 and j == 0 and k == 0 and l == 0)]

def checkNeighbors(cb, cbs, dim):
    return len([n for n in findNeighbors(cb, dim) if cbs.get(n) == "#"])

def enforceRules(cubes, dim):
    new_cubes = {}
    for cube in cubes:
        i = checkNeighbors(cube, cubes, dim)
        if cubes[cube] == "#":
            new_cubes[cube] = "#" if i == 2 or i == 3 else "."
            neighbors = findNeighbors(cube, dim)
            for i in neighbors:
                if i not in cubes:
                    j = checkNeighbors(i, cubes, dim)
                    if j == 3: new_cubes[i] = "#"
        elif cubes[cube] == ".": new_cubes[cube] = "#" if i == 3 else "."
    return new_cubes

def simulateCycles(d, dim):
    if dim not in (3, 4): return "'{}' is not a valid dimension here.".format(dim)
    cubes = startingCubes(d, dim)
    for i in range(6):
        cubes = enforceRules(cubes, dim)
    return [cube for cube in cubes.values()].count("#")

def main():
    data = readFile("day17.txt")
    part1, part2 = simulateCycles(data, 3), simulateCycles(data, 4)
    print("{0}, {1}".format(part1, part2))

if __name__ == "__main__":
    main()
