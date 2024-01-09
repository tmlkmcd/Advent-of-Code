import sys
import itertools

opcode = []

part = 2

for line in sys.stdin:
    for num in [int(x) for x in line.split(",")]:
        opcode.append(num)

if part == 2:
    opcode[0] = 2

grid = []
for _ in range(25):
    grid.append([' ' for _ in range(40)])

draw_tile_stage = 0

new_tile_data = []

def draw_new_tile(new_tile_data):
    global num_block
    global grid
    x, y, tile_id = new_tile_data
    if x == -1 and y == 0:
        print("SCORE", tile_id)
        return
    tile_k = " "
    if tile_id == 0: pass
    if tile_id == 1: tile_k = "|"
    if tile_id == 2: tile_k = "#"
    if tile_id == 3: tile_k = "_"
    if tile_id == 4: tile_k = "O"
    grid[y][x] = tile_k

def draw_tile(output):
    global new_tile_data
    global draw_tile_stage
    new_tile_data.append(output)
    if draw_tile_stage == 2:
        draw_new_tile(new_tile_data)
        new_tile_data = []

    draw_tile_stage = (draw_tile_stage + 1) % 3
    

def report():
    for row in grid:
        print("".join(row))

def get_input():
    row_index, paddle_index = -1, -1
    for row in grid:
        if "O" in row:
            row_index = row.index("O")
        if "_" in row:
            paddle_index = row.index("_")

    if row_index == -1 or paddle_index == -1:
        raise Exception("something wrong")

    if row_index > paddle_index: return 1
    if row_index < paddle_index: return -1
    return 0

def run_program(intcode):
    global inputs
    global input_pointer
    l = intcode.copy() # 'l'ocal intcode
    for _ in range(200):
        l.append(0)
    p = 0

    relative_base = 0

    while True:
        if (l[p] % 100) == 99:
            print("done!")
            # print(l)
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
            l[rpa] = get_input()
            # report()
            # print("setting address", rpa, " to ", puzzle_input)
            p += 2
        elif o == 4:
            # print("============")
            # print("| output", l[rpa], "|")
            draw_tile(l[rpa])
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

run_program(opcode)

num_blocks = list(itertools.chain(*grid)).count("#")
print(num_blocks)

report()