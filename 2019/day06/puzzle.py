import sys

orbits = []

for line in sys.stdin:
    orbits.append(line.strip())

total_o = 0

planets_score = {"COM": 0}

orbits_part1_clone = orbits.copy()

def check_orbits():
    global total_o
    for o in orbits_part1_clone:
        p1, p2 = o.split(")")
        if (p1 in planets_score.keys()):
            planets_score[p2] = planets_score[p1] + 1
            total_o += planets_score[p1] + 1
            orbits_part1_clone.remove(o)
        else:
            continue
    if (len(orbits_part1_clone) > 0):
        check_orbits()

check_orbits()
print("part 1 answer:", total_o)    
    
def find_next(p):
    return [x for x in orbits if (x.split(")")[1] == p)][0].split(")")[0]

santa = ["SAN"]
while (santa[-1] != "COM"):
    santa.append(find_next(santa[-1]))

me = ["YOU"]
while (me[-1] != "COM"):
    me.append(find_next(me[-1]))

while (me[-1] == santa[-1]):
    me.remove(me[-1])
    santa.remove(santa[-1])

me.remove("YOU")
santa.remove("SAN")

print("part 2 answer:", len(me) + len(santa))

