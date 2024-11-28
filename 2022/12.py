import sys

lines_in = [line.strip() for line in sys.stdin]
grid = [list(line) for line in lines_in]
my_as = []
paths = dict()

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == 'S':
            S = (y, x)
            my_as.append(S)
        elif cell == 'E': E = (y, x)
        elif cell == 'a': my_as.append((y, x))

def is_valid_step(first_coord, second_coord):
    global grid
    y, x = first_coord
    yy, xx = second_coord
    first_height = grid[y][x]
    second_height = grid[yy][xx]
    second_height = 'z' if second_height == 'E' else second_height

    if first_height == 'S': return True
    return ord(first_height) - ord(second_height) >= -1

def crawl(current_energy, paths):
    examine = [p for p in paths if paths[p] == current_energy]
    ne = current_energy + 1

    if len(examine) == 0: return 1e9  # the E is not accessible at all from some 'a' starting points

    for p in examine:
        y, x = p
        for yy, xx in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
            nc = (yy, xx)
            if yy < 0 or xx < 0 or yy >= len(grid) or xx >= len(grid[0]): continue
            if (yy, xx) in paths: continue
            if not is_valid_step(p, nc): continue
            paths[nc] = ne

    if E not in paths: return crawl(ne, paths)
    else: return paths[E]

paths[S] = 0
print('pt1', crawl(0, paths))

pt2 = 1e9

for a in my_as:  # brute-forcing it is a bit of a cheat, but it runs in about ~10 seconds 🤷
    as_path = dict()
    as_path[a] = 0
    pt2 = min(crawl(0, as_path), pt2)

print('pt2', pt2)
