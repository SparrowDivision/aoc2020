def readFile(input_name):
    rules, messages, separate = {}, [], False
    with open(input_name, "r") as f:
        for line in f:
            if line == "\n": separate = True
            elif separate: messages.append(line.strip())
            else: rules.update(formatRules(line.strip()))
    return rules, messages

def formatRules(l):
    ruleID, rule = l.split(": ")
    if "|" in rule:
        r1, r2 = rule.strip().split(" | ")
        rule = [[int(x) for x in r1.split(" ")], [int(y) for y in r2.split(" ")]]
    elif rule[1].isalpha(): rule = rule.strip('"')
    else: rule = [[int(z) for z in rule.split(" ")]]
    return {int(ruleID): rule}

def evaluateMatch(rl, rls, msg):
    if len(rl) == 0 or len(msg) == 0: return len(rl) == 0 and len(msg) == 0
    num = rl.pop()
    if isinstance(num, int):
        for rule in rls[num]:
            if evaluateMatch(rl + list(rule)[::-1], rls, msg): return True   
    elif msg[0] == num: return evaluateMatch(rl, rls, msg[1:])
    return False

def countMatching(rls, mssgs):
    counter, rule = 0, rls[0][0]
    for msg in mssgs:
        if evaluateMatch(rule[::-1], rls, msg): counter += 1
    return counter

def main():
    rules, messages = readFile("day19.txt")
    print(countMatching(rules, messages))
    rules.update({8: [[42], [42, 8]]})
    rules.update({11: [[42, 31], [42, 11, 31]]})
    print(countMatching(rules, messages))

if __name__ == "__main__":
    main()
