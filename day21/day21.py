def readFile(input_name):
    with open(input_name) as f:
        return [line.strip()[:-1].split(" (contains ") for line in f]

def allergenList(d):
    alergen_list = []
    for ingredients, allergens in d:
        ingredients, allergens = ingredients.split(" "), allergens.split(", ")
        for allergen in allergens: alergen_list.append([allergen, ingredients])
    return sorted(alergen_list)

def removeDuplicates(dlist):
    dlist = {ale: ing for ale, ing in sorted(dlist, key = lambda x: len(x[1]))}
    for x in dlist:
        for y in dlist:
            actual = dlist[x][0] if len(dlist[x]) > 1 else dlist[x]
            if x != y: dlist[y] = [ing for ing in dlist[y] if ing not in actual]
    return ["".join(dlist[z]) for z in sorted(dlist.keys())]

def part1(d, dangerous):
    counter = 0
    for x in d:
        for y in x[0].split(" "):
            if y not in dangerous: counter += 1
    return counter

def part2(d):
    allergen_list, dangerous = allergenList(d), []
    common_allergens, prev_ingredients = allergen_list[0][0], allergen_list[0][1]
    for allergen, ingredients in allergen_list:
        if allergen == common_allergens:
            prev_ingredients = list(set(ingredients).intersection(prev_ingredients))   
        else:
            dangerous.append([common_allergens, sorted(prev_ingredients, reverse = True)])
            common_allergens, prev_ingredients = allergen, ingredients
    dangerous.append([common_allergens, prev_ingredients])
    return removeDuplicates(dangerous)

def main():
    data = readFile("day21.txt")
    p2 = part2(data)
    print(part1(data, p2))
    print(",".join(x for x in p2))

if __name__ == "__main__":
    main()
