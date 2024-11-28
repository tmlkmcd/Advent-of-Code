import sys

m = []

for line in sys.stdin:
    m.append([int(n) for n in line.strip()])

xx = len(m[0])
yy = len(m)

tot = 0

basins = []

def scan_basin(x, y, checked=[]):
    str_coord = str(y) + ',' + str(x)

    if m[y][x] < 9 and str_coord not in checked:
        checked.append(str_coord)
    else: return checked

    try:
        if x > 0: checked = scan_basin(x - 1, y, checked)
        if x < xx - 1: checked = scan_basin(x + 1, y, checked)
        if y > 0: checked = scan_basin(x, y - 1, checked)
        if y < yy - 1: checked = scan_basin(x, y + 1, checked)
    except Exception as e:
        pass

    return checked

for x in range(xx):
    for y in range(yy):
        n = m[y][x]

        up = 20
        left = 20
        right = 20
        down = 20

        try: up = m[y - 1][x]
        except: pass

        try: down = m[y + 1][x]
        except: pass

        try: right = m[y][x + 1]
        except: pass

        try: left = m[y][x - 1]
        except: pass

        if n < left and n < right and n < up and n < down:
            s = scan_basin(x, y, [])
            basins.append(len(s))
            tot += (1 + n)

print('part 1', tot)

basins.sort(reverse=True)
print('part 2', basins[0] * basins[1] * basins[2])


