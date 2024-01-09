import sys
import random
g = ["##########################################",
"#...#.......#...#...#.........#...#.....##",
"#.###.#.###.#.#.#.#.#####.###.#.#.###.#.##",
"#.....#...#.#.#...#.#.....#.....#.....#.##",
"#.####.##.#.#.#####.#.#.#########.#####.##",
"#.....#...#...#...#...#.#...#...#.#...#.##",
"#####.#.#######.###.#####.#.#.#.###.#.####",
"#...#.#.#...........#.....#...#.....#...##",
"#.#.###.#.###########.########.#####.##.##",
"#.#.....#.#.............#.....#.....#...##",
"#.#######.#.###########.###.###.###.#.####",
"#...#...#.#...#...#...#.....#...#...#...##",
"#.#.#.###.###.###.#.#.#####.#.###.#####.##",
"#.#.#.......#...#.#.#.#.....#.#...#.....##",
"#.#.###########.#.#.#.#######.#.###.###.##",
"#.#...#...#...#.#.#.#.#.....#.#.#.....#.##",
"#####.#.#.#.#.#.#.#.#.#.###.#.#.#.###.#.##",
"#...#...#...#.....#.#...#.#...#.#.#...#.##",
"#.#.###############.#####.#####.###.######",
"#.#.............#...#...#.....#...#.#...##",
"#.#####.#######.#.#.###.#.###.###.#.#.#.##",
"#.#.....#.....#...#.#D#.#.#.#.#...#...#.##",
"#.#######.###.#####.#.#.#.#.#.#.#######.##",
"#.#.........#...#...#.#.....#.#.........##",
"#.#.###########.#.###.#######.#########.##",
"#...#...#.....#.#...#.......#.#...#.....##",
"#######.#.###.#.###.#######.#.#.#.#.######",
"#.......#...#...#.....#.....#.#.#.#...#.##",
"#.###.#.###.#####.#####.#####.#.#.###.#.##",
"#.#...#...#.#.....#.....#...#...#.....#.##",
"#.#.#####.#.#######.#####.###.#########.##",
"#.#.#.....#.........#.........#.........##",
"#.#.#################.#########.#######.##",
"#O#.#...#...#.......#.....#.....#.....#.##",
"###.#.#.#.#.#.#####.#####.#.###.###.#.#.##",
"#...#.#.#.#...#...#...#...#...#...#.#.#.##",
"#.###.#.#.#####.#.###.#.#########.#.#.#.##",
"#.....#.#.......#.#...#...........#.#...##",
"#.#####.#########.#.###############.######",
"#.....#...........#.....................##",
"##########################################"]

opcode = []
part = 2

for line in sys.stdin:
    for num in [int(x) for x in line.split(",")]:
        opcode.append(num)

grid_size = 42
grid = [[char for char in row] for row in g]

x = grid_size//2
y = grid_size//2

net_movement = [-1]

def report(grid):
    grid[grid_size//2][grid_size//2] = "S"
    print(net_movement)
    for _ in grid:
        print("".join(_))

most_recent_input = -1
def generate_random_direction():
    global most_recent_input
    r = random.randint(1, 4)
    most_recent_input = r
    return r

def run_program(intcode):
    global grid
    global x
    global y
    global net_movement

    l = intcode.copy() # 'l'ocal intcode
    for _ in range(200):
        l.append(0)
    p = 0

    relative_base = 0

    max_steps = 20000000
    steps = 0

    while True:
        if (l[p] % 100) == 99:
            print("done!")
            print(l)
            break

        # print("------------------------------------------")

        o = l[p] % 10 # opcode

        # if o < 3 or o == 7 or o == 8: print(l[p:p+4])
        # elif (o == 5 or o == 6): print(l[p:p+3])
        # else: print(l[p:p+2])

        dummy_opcode = str(100000000 + l[p])

        mode_1 = dummy_opcode[-3]
        mode_2 = dummy_opcode[-4]
        mode_3 = dummy_opcode[-5]

        if mode_1 == "0": rpa = l[p + 1]
        elif mode_1 == "1": rpa = p + 1
        elif mode_1 == "2": rpa = l[p + 1] + relative_base

        if mode_2 == "0": rpb = l[p + 2]
        elif mode_2 == "1": rpb = p + 2
        elif mode_2 == "2": rpb = l[p + 2] + relative_base

        if mode_3 == "0": rpc = l[p + 3]
        elif mode_3 == "1": rpc = p + 3
        elif mode_3 == "2": rpc = l[p + 3] + relative_base

        if o == 1:
            l[rpc] = l[rpa] + l[rpb]
            # print("pointer", rpc, "setting to", l[rpa], "plus", l[rpb])
            p += 4
        elif o == 2:
            l[rpc] = l[rpa] * l[rpb]
            # print("pointer", rpc, "setting to", l[rpa], "times", l[rpb])
            p += 4
        elif o == 3:
            # print("INPUT!!?!?!?!?", rpa)
            l[rpa] = generate_random_direction()
            steps += 1
            # print("setting address", rpa, " to ", puzzle_input)
            p += 2
        elif o == 4:
            # print("============")
            # print("| output", l[rpa], "|")
            tx = x
            ty = y
            if most_recent_input == 1: ty -= 1
            elif most_recent_input == 2: ty += 1
            elif most_recent_input == 3: tx -= 1
            elif most_recent_input == 4: tx += 1

            if l[rpa] == 0:
                grid[ty][tx] = "#"
            elif l[rpa] == 1:
                grid[y][x] = "."
                grid[ty][tx] = "D"
                y = ty
                x = tx
                if most_recent_input == 1:
                    if net_movement[-1] == 2: net_movement.pop()
                    else: net_movement.append(1)
                elif most_recent_input == 2:
                    if net_movement[-1] == 1: net_movement.pop()
                    else: net_movement.append(2)
                elif most_recent_input == 3:
                    if net_movement[-1] == 4: net_movement.pop()
                    else: net_movement.append(3)
                elif most_recent_input == 4:
                    if net_movement[-1] == 3: net_movement.pop()
                    else: net_movement.append(4)
            elif l[rpa] == 2:
                grid[ty][tx] = "O"
                x = tx
                y = ty
                report(grid)
                return
            if steps >= max_steps:
                report(grid)
                return
            elif steps%50000 == 0:
                print(steps)

            # print("============")
            p += 2
        elif o == 5:
            if l[rpa] != 0: p = l[rpb]
            else: p += 3
            # print("pointer currently", p, "if", l[rpa], "NOT 0 then setting to", l[rpb])
        elif o == 6:
            if l[rpa] == 0: p = l[rpb]
            else: p += 3
            # print("pointer currently", p, "if", l[rpa], "IS 0 then setting to", l[rpb])
        elif o == 7:
            if l[rpa] < l[rpb]: l[rpc] = 1
            else: l[rpc] = 0
            p += 4
            # print("target position is", rpc, "if", l[rpa], "LESS THAN", l[rpb], "setting target to 1")
        elif o == 8:
            if l[rpa] == l[rpb]: l[rpc] = 1
            else: l[rpc] = 0
            p += 4
            # print("target position is", rpc, "if", l[rpa], "EQUAL TO", l[rpb], "setting target to 1")
        elif o == 9:
            relative_base += l[rpa]
            p += 2
            # print("adjusting relative base by ", l[rpa], ", it is now", relative_base)
        else: raise "oh noes"
    return l[0]

if part == 1:
    run_program(opcode)
    exit()

def check_neighbours(x, y):
    made_change = False
    if grid[y - 1][x] == ".":
        grid[y - 1][x] = "o"
        made_change = True
    if grid[y + 1][x] == ".":
        grid[y + 1][x] = "o"
        made_change = True
    if grid[y][x - 1] == ".":
        grid[y][x - 1] = "o"
        made_change = True
    if grid[y][x + 1] == ".":
        grid[y][x + 1] = "o"
        made_change = True
    
    grid[y][x] = "x"
    return made_change

iterations = 0
report(grid)
while True:
    has_changed = False
    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if grid[y][x] == "O":
                modified = check_neighbours(x, y)
                if modified: has_changed = True

    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if grid[y][x] == "o": grid[y][x] = "O"
    if not has_changed:
        break
    iterations += 1
print(iterations)
