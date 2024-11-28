import sys

def sanitise(n):
    return int(n.strip())

part = 2

if part == 1:
    increases = 0
    prev = -99

    for line in sys.stdin:
        v = sanitise(line)
        if prev != -99 and v > prev: increases += 1
        prev = v

    print('part 1:', increases)

else:
    increases2 = 0
    heights = list(map(sanitise, sys.stdin))

    for i, h in enumerate(heights):
        if i < 3: continue
        if h > heights[i - 3]: increases2 += 1

    print('part 2:', increases2)
