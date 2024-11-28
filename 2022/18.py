import sys

lines_in = [line.strip() for line in sys.stdin]
cubes = [[int(a) for a in line.split(',')] for line in lines_in]
cubes = [(x, y, z) for x, y, z in cubes]
sa_1, sa_2 = 0, 0
exposed = []

min_x = min(x for x, y, z in cubes)
min_y = min(y for x, y, z in cubes)
min_z = min(z for x, y, z in cubes)
max_x = max(x for x, y, z in cubes)
max_y = max(y for x, y, z in cubes)
max_z = max(z for x, y, z in cubes)

goes_to_infinity_d = {}

def explore(checking_point, explored=[]):
    global goes_to_infinity_d
    if checking_point in goes_to_infinity_d: return True
    x, y, z = checking_point
    for dd in [-1, 1]:
        for c in [(x + dd, y, z), (x, y + dd, z), (x, y, z + dd)]:
            if c in cubes:
                continue
            xx, yy, zz = c
            if xx < min_x or xx > max_x or yy < min_y or yy > max_y or zz < min_z or zz > max_z:
                return True
            if c not in explored:
                explored.append(checking_point)
                goes_to_infinity = explore(c, explored)
                if goes_to_infinity:
                    for _ in explored:
                        goes_to_infinity_d[_] = True
                    return True
    return False

for x, y, z in cubes:
    psa_1 = 6
    psa_2 = 0
    for dd in [-1, 1]:
        for c in [(x + dd, y, z), (x, y + dd, z), (x, y, z + dd)]:
            if c in cubes: psa_1 -= 1
            if c not in cubes:
                is_exposed = explore(c, [])
                if is_exposed:
                    psa_2 += 1

    sa_1 += psa_1
    sa_2 += psa_2

print(f'part 1: {sa_1}, part 2: {sa_2}')
