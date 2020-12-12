def readFile(input_name):
    return [(l.strip()[0], int(l.strip()[1:])) for l in open(input_name, "r").readlines()]
 
def newDirection(old, act, angle):
    dirs, offset = ["E", "S", "W", "N"], angle // 90
    if act == "L":  offset *= -1
    return dirs[(dirs.index(old) + offset) % len(dirs)]

def sinCos(x, mode, e = 2.718281828459045):
    if mode == "sin":
        return (e**(x*1j)).imag
    return (e**(x*1j)).real

def rotateWaypoint(actx, acty, angle, pi = 3.14159265359):
    angle = angle * pi / 180
    x = sinCos(angle, "cos") * actx - sinCos(angle, "sin") * acty
    y = sinCos(angle, "sin") * actx + sinCos(angle, "cos") * acty
    return int(round(x)), int(round(y))

def part1(d):
    direction = "E"
    coords = {"N":0, "S":0, "E":0, "W":0}
    for action, value in d:
        if action == "F": coords[direction] += value
        elif not action in coords: direction = newDirection(direction, action, value)
        else: coords[action] += value
    return abs(coords["N"]-coords["S"]) + abs(coords["E"]-coords["W"])

def part2(d):
    coords, waypoint = {'x': 0, 'y': 0}, {'x': 10, 'y': 1}
    for action, value in d:
        if   action == 'N': waypoint['y'] += value
        elif action == 'S': waypoint['y'] -= value
        elif action == 'E': waypoint['x'] += value
        elif action == 'W': waypoint['x'] -= value
        elif action == 'F':
            coords['x'] += waypoint['x'] * value
            coords['y'] += waypoint['y'] * value
        else:
            if action == 'R': value = -value
            waypoint['x'], waypoint['y'] = rotateWaypoint(waypoint['x'], waypoint['y'], value)
    return abs(coords['x']) + abs(coords['y'])

def main():
    data = readFile("day12.txt")
    print(part1(data))
    print(part2(data))

if __name__ == "__main__":
    main()
