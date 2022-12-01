import sys

lines_in = [line.strip() for line in sys.stdin]
assi = []

for l in lines_in:
    a = l.split(',')
    b = [[int(b) for b in c.split('-')] for c in a]
    b.sort()
    assi.append(b)

ans, ans_2 = 0, 0

for a in assi:
    if (a[0][0] <= a[1][0] and a[0][1] >= a[1][1])\
            or (a[0][0] >= a[1][0] and a[0][1] <= a[1][1]):
        ans += 1
    if a[0][1] >= a[1][0]: ans_2 += 1

print(f'part 1: {ans}, part 2: {ans_2}')
