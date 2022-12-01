import sys

lines_in = [line.strip() for line in sys.stdin]
grid = [list(line) for line in lines_in]
for row in grid:
    row.append('.')

stars = {}

def build_number(new, old):
    return (old * 10) + int(new) if new.isdigit() else False

def scan(x, y, l, a):
    global grid
    # print(x,y,l,a)

    for xx in range(l + 2):
        x_coord = xx + x - 1 - l
        if x_coord < 0: continue
        for yy in range(3):
            y_coord = yy + y - 1
            if y_coord < 0 or y_coord >= len(grid): continue
            cell = grid[yy + y - 1][xx + x - 1 - l]
            if cell.isdigit() or cell == '.': continue
            else:
                if cell == '*':
                    coord = str(x_coord) + ',' + str(y_coord)
                    if coord in stars: stars[coord].append(a)
                    else: stars[coord] = [a]
                return a
    return 0


total, total2 = 0, 0
current_num = 0
num_len = 0

for y, row in enumerate(grid):
    for x, d in enumerate(row):
        r = build_number(d, current_num)
        if r:
            current_num = r
            num_len += 1
        else:
            if current_num > 0: total += scan(x, y, num_len, current_num)
            current_num = 0
            num_len = 0


for k in stars:
    arr = stars[k]
    if len(arr) == 2:
        total2 += arr[0] * arr[1]

print('part 1', total)
print('part 2', total2)
