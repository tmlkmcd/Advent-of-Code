import sys
import math
import collections
import itertools

lines_in = [line.strip() for line in sys.stdin]

data = {}
data2 = {}
map2 = {}

for a, line in enumerate(lines_in):
    point, numbers = [a.strip() for a in line.split(':')]
    data[point] = [int(a) for a in numbers.split(' ') if a.isdigit()]

for line in lines_in:
    stripped = line.replace(' ', '')
    point, number = stripped.split(':')
    data2[point] = int(number)


def try_race(n):
    global data
    time = data['Time'][n]
    record = data['Distance'][n]
    successes = []
    for trying_time in range(time):
        if time == 0: continue
        if trying_time * (time - trying_time) > record:
            successes.append(trying_time)

    return sorted(successes)

def try_race2(start):
    global data2, map2
    for n in reversed(range(start)):
        if (data2['Time'] - n) * n > data2['Distance']:
            map2[n] = True
            map2[data2['Time'] - n] = True

    return len(map2.keys())




# print('part 1', math.prod([len(try_race(n)) for n in range(len(data['Time']))]))
# print(math.ceil(math.pow(data2['Time'], 0.5)))

# print(data2)
print(try_race2(math.ceil(data2['Time'] * 0.5)))
# print('part 2', tr)


