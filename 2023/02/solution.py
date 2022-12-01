import sys
from functools import reduce

lines_in = [line.strip() for line in sys.stdin]

total, total2 = 0, 0

def analyse(game):
    game_, details = game.split(': ')
    game_num = int(game_.split(' ')[1])
    attempts = details.split('; ')
    for attempt in attempts:
        cubes = attempt.split(', ')
        for cube in cubes:
            num_cubes, colour = cube.split(' ')
            num_cubes = int(num_cubes)
            if colour == 'green' and num_cubes > 13: return 0
            if colour == 'red' and num_cubes > 12: return 0
            if colour == 'blue' and num_cubes > 14: return 0
    return game_num

def power(game):
    game_, details = game.split(': ')
    attempts = details.split('; ')
    min_cubes = { 'red': -1, 'blue': -1, 'green': -1 }
    for attempt in attempts:
        cubes = attempt.split(', ')
        for cube in cubes:
            num_cubes, colour = cube.split(' ')
            num_cubes = int(num_cubes)
            min_cubes[colour] = max(min_cubes[colour], num_cubes)
    return reduce((lambda x, y: x * y), [min_cubes[k] for k in min_cubes])

for game in lines_in:
    total += analyse(game)
    total2 += power(game)

print('part 1', total)
print('part 2', total2)
