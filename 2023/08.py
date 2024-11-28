import sys
import math

lines_in = [line.strip() for line in sys.stdin]
directions, paths = lines_in[0], {}
for line in lines_in[2:]:
    c, n = line.split(' = ')
    paths[c] = {
        'L': n[1:4],
        'R': n[6:9]
    }


def search(start, part=1):
    current, steps = start, 0
    while True:
        for step in directions:
            steps += 1
            current = paths[current][step]
            if part == 1 and current == 'ZZZ': return steps
            if part == 2 and current[2] == 'Z': return steps


print('part 1', search('AAA'))
print('part 2', math.lcm(*[search(place, 2) for place in paths if place.endswith('A')]))
