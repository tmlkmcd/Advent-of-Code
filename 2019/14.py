import sys
import re
import math

reactions = {}
part = 2

def parse_entity(string):
    quan, chem = re.findall(r"^(\d+) ([A-Z]+)$", string)[0]
    quan = int(quan)
    return (quan, chem)

def parse_line(line):
    reagents, product = line.split(" => ")
    r_map, p_map = {}, {}
    for reagent in reagents.split(", "):
        quan, chem = parse_entity(reagent)
        r_map[chem] = quan

    quan, chem = parse_entity(product)
    p_map[chem] = quan

    return r_map, p_map

for line in sys.stdin:
    reagents, product = parse_line(line.strip())
    for p in product:
        if p in reactions: raise Exception("multiple")
        reactions[p] = [product[p], reagents]

def get_requirements(entity, amt, leftover):
    if amt == 0:
        return {}
    amount, requirements = reactions[entity]
    amt_prod_required = amt
    if entity in leftover:
        if leftover[entity] > amt_prod_required:
            leftover[entity] = leftover[entity] - amt_prod_required
            return {}
        amt_prod_required -= leftover[entity]
        leftover[entity] = 0
    num_reactions = 1 if amt_prod_required <= amount else math.ceil(amt_prod_required/amount)
    new_requirements = {}
    for r in requirements:
        amt_required = requirements[r] * num_reactions
        if r in leftover:
            if leftover[r] > amt_required:
                leftover[r] = leftover[r] - amt_required
            elif leftover[r] <= amt_required:
                amt_required -= leftover[r]
                leftover[r] = 0
        new_requirements[r] = amt_required
    if amt_prod_required < (amount * num_reactions):
        leftover[entity] = (amount * num_reactions) - amt_prod_required
    return new_requirements

def solve(fuel_amt):
    ore_required = 0
    leftover = {}
    def get_requirements_r(entity, amt, leftover):
        nonlocal ore_required
        requirements = get_requirements(entity, amt, leftover)
        for r in requirements:
            if r == "ORE":
                ore_required += requirements[r]
            else:
                get_requirements_r(r, requirements[r], leftover)
    get_requirements_r("FUEL", fuel_amt, leftover)
    return ore_required

if part == 1:
    print(solve(1))
    exit()

start = 998500
current = start
while True:
    current += 1
    if solve(current) >= 1000000000000:
        ans = current - 1
        print(ans)
        break
