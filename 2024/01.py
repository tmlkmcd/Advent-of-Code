f = open("inputs/2024/01.txt", "r")

lines_in = [line.strip() for line in f]
l_col, r_col = [], []

for line in lines_in:
    [l, r] = [int(a) for a in line.split('   ')]
    l_col.append(l)
    r_col.append(r)

l_col.sort()
r_col.sort()

pt1, pt2 = 0, 0

for i in range(len(l_col)):
    pt1 += abs(l_col[i] - r_col[i])

print('part 1', pt1)

appears, scanning = {}, 0

for i in range(len(l_col)):
    current = l_col[i]
    if appears.get(current):
        continue

    amt = 0
    try:
        while r_col[scanning] < current:
            scanning += 1
        while r_col[scanning] == current:
            amt += 1
            scanning += 1
    except IndexError:
        pass

    appears[current] = amt * current

for n in l_col:
    pt2 += appears[n]

print('part 2', pt2)
