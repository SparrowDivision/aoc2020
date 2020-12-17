def readFile(input_name): 
    lines = [l.strip().split(":") for l in open(input_name, "r").readlines()]
    blank1, blank2 = findBlank(lines)
    return ({field: getRule(rule) for field, rule in lines[:blank1]},
            [int(value) for value in (lines[blank2 - 1][0]).split(",")],
            [[int(value) for value in (z[0]).split(",")] for z in lines[blank2 + 2:]])

def findBlank(l):
    empty_line1, empty_line1 = 0, 0
    for i, line in enumerate(l):
        if empty_line1 == 0 and line == [""]: empty_line1 = i
        elif line == [""]: empty_line2 = i
    return empty_line1, empty_line2

def getRule(r):
    return [int(x) for x in "".join(filter(lambda d: str.isdigit(d) or d == " ", r.replace("-", " "))).split()]

def checkRule(r, v):
    return r[0] <= v <= r[1] or r[2] <= v <= r[3]

def part1(rs, ts):
    solution, invalid_tickets = 0, []
    for ticket in ts:
        for value in ticket:
            valid_value = False
            for rule in rs.values():
                if checkRule(rule, value): valid_value = True         
            if not valid_value:
                solution += value
                invalid_tickets.append(ticket)
    return solution, [ticket for ticket in ts if ticket not in invalid_tickets]

def part2(rs, mt, vts):
    possible = {rname: set() for rname in rs}
    for i in range(len(mt)):
        col_values = [vticket[i] for vticket in vts]
        for rule in rs.items():
            valid_rule = True
            for value in col_values:
                if not checkRule(rule[1], value): valid_rule = False
            if valid_rule: possible[rule[0]].add(i)

    valid_order, overlap = {}, set()
    while len(valid_order) < len(mt):
        for field, poss in possible.items():
            poss -= overlap
            if len(poss) == 1:
                valid_order[field] = poss.pop()
                overlap.add(valid_order[field])

    solution = 1
    for field in valid_order:
        if "departure" in field: solution *= mt[valid_order[field]]
    return solution

def main():
    rules, myticket, tickets = readFile("day16.txt")
    p1, validtickets = part1(rules, tickets)
    p2 = part2(rules, myticket, validtickets)
    print(p1, p2)

if __name__ == "__main__":
    main()
