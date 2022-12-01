import sys

jets = list(sys.stdin.read().strip())
rocks, movements, max_height = 0, 0, 0

grid = [['.' for _ in range(7)] for _ in range(150000)]
num_rocks_pt2 = 1_000_000_000_000

last_few_rocks = []
last_few_heights = []
found_periodicity = False
starting_rocks = -1
starting_height = -1
rock_periodicity = -1
height_periodicity = -1
pt2_done = False
remainder = None

fudge_factor = 8

def get_new_rock(type):
    global max_height
    mhp3 = max_height + 3
    if type == 0: # hyphen
        return [(2, mhp3), (3, mhp3), (4, mhp3), (5, mhp3)]
    if type == 1: # plus
        return [(2, mhp3 + 1), (3, mhp3 + 1), (4, mhp3 + 1), (3, mhp3), (3, mhp3 + 2)]
    if type == 2: # L
        return [(2, mhp3), (3, mhp3), (4, mhp3), (4, mhp3 + 1), (4, mhp3 + 2)]
    if type == 3: # I
        return [(2, mhp3), (2, mhp3 + 1), (2, mhp3 + 2), (2, mhp3 + 3)]
    if type == 4: # O
        return [(2, mhp3), (2, mhp3 + 1), (3, mhp3), (3, mhp3 + 1)]


def spawn():
    global rocks, max_height, starting_rocks, rock_periodicity, remainder
    rock = get_new_rock(rocks % 5)


    if found_periodicity and remainder is not None and rocks > 2030:
        if (rocks) % rock_periodicity == fudge_factor: # ?????
            print('without remainder', max_height)
            visualise(grid, [], max_height)
        if (rocks) % rock_periodicity == remainder + fudge_factor:
            print('with remainder', max_height)
            visualise(grid, [], max_height)

    while True:
        landed, rock = move(rock)
        if landed == 'break':
            return True
        if landed:
            for x, y in rock: grid[y][x] = '#'
            max_height = max([n for n, row in enumerate(grid) if '#' in row]) + 1
            break
    rocks += 1

def move(rock):
    global movements, found_periodicity, starting_rocks, starting_height, rock_periodicity, height_periodicity, pt2_done
    global remainder
    jet = jets[movements % len(jets)]
    landed = False

    if not found_periodicity and movements % (len(jets) * 1) == 0:
        last_few_rocks.append(rocks)
        last_few_heights.append(max_height)
        if len(last_few_rocks) > 7: last_few_rocks.pop(0)
        if len(last_few_heights) > 7: last_few_heights.pop(0)

        if len(last_few_rocks) >= 7 and len(last_few_heights) >= 7:
            rock_diffs = [r - last_few_rocks[n - 1] for n, r in enumerate(last_few_rocks) if n > 0]
            height_diffs = [h - last_few_heights[n - 1] for n, h in enumerate(last_few_heights) if n > 0]

            if len(set(rock_diffs)) == 1 and len(set(height_diffs)) == 1:
                found_periodicity = True
                rock_periodicity = rock_diffs[0]
                height_periodicity = height_diffs[0]

                loops = (num_rocks_pt2 - starting_rocks) // rock_periodicity
                pt_2_height = starting_height + loops * height_periodicity
                remainder = (num_rocks_pt2 - starting_rocks) % rock_periodicity

                print(pt_2_height) # add the diff between 'with remainder' and 'without remainder' to this
            else:
                starting_rocks = rock_diffs[0]
                starting_height = height_diffs[0]

    if pt2_done:
        return 'break', []

    if jet == '>':
        can_move_right = True
        for x, y in rock:
            if x > 5 or grid[y][x + 1] != '.':
                can_move_right = False
                break
        if can_move_right: rock = [(x + 1, y) for x, y in rock]
    else:
        can_move_left = True
        for x, y in rock:
            if x < 1 or grid[y][x - 1] != '.':
                can_move_left = False
                break
        if can_move_left: rock = [(x - 1, y) for x, y in rock]

    movements += 1

    can_move_down = True
    for x, y in rock:
        if y == 0 or grid[y - 1][x] != '.':
            landed = True
            can_move_down = False
            break

    if can_move_down:
        rock = [(x, y - 1) for x, y in rock]

    return landed, rock

def visualise(grid, rock=[], row=None):
    temp_grid = []
    for yy, row in enumerate(grid[row-8:row+1] if row is not None else grid):
        temp_row = []
        for xx, cell in enumerate(row):
            if (xx, yy) in rock: temp_row.append('#')
            else: temp_row.append(cell)
        temp_grid.append(temp_row)
    for row in reversed(temp_grid):
        print(''.join(row))

for _ in range(50000):
    done = spawn()
    if _ == 2021:
        print('part 1', max_height)
    if done: break

