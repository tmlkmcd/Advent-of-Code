with open("inputs/2024/15.txt", "r") as f:
    content = f.read().split('\n\n')

grid, grid_2 = [[cell for cell in row] for row in content[0].split('\n')], []
for row in grid:
    row_2 = []
    for cell in row:
        if cell == '@': row_2 += ['@', '.']
        if cell == 'O': row_2 += ['[', ']']
        if cell == '#': row_2 += ['#', '#']
        if cell == '.': row_2 += ['.', '.']
    grid_2.append(row_2)

directions = [_dir for _dir in ''.join(content[1].split('\n'))]
direction = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}


def find_robot(_grid):
    for y, row in enumerate(_grid):
        for x, cell in enumerate(row):
            if cell == '@':
                return (y, x)


def shove(start, _direction):
    global grid
    dy, dx = direction[_direction]
    y, x = start
    start_entity = grid[y][x]
    destination = grid[y + dy][x + dx]

    if destination == '#': return False

    if destination == 'O':
        _next = shove((y + dy, x + dx), _direction)
        if _next:
            grid[y + dy][x + dx] = start_entity
            grid[y][x] = '.'
        return _next

    if destination == '.':
        grid[y + dy][x + dx] = start_entity
        grid[y][x] = '.'
        return True

    return False


def shove_2(start, _direction, commands):
    global robot_2, grid_2
    dy, dx = direction[_direction]

    if _direction == '<' or _direction == '>':
        assert len(start) == 1

        yy, xx = start[0]
        sy, sx = start[0]
        asd = [(yy, xx)]
        while True:
            yy += dy
            xx += dx
            if grid_2[yy][xx] == '#':
                return False
            if grid_2[yy][xx] == '.':
                for _ in range(len(asd)):
                    yyy, xxx = asd.pop(-1)
                    grid_2[yy][xx] = grid_2[yyy][xxx]
                    yy, xx = yyy, xxx
                grid_2[sy][sx] = '.'
                return True

            asd.append((yy, xx))

    destinations_coord = [(y + dy, x + dx) for y, x in start]
    destinations = [grid_2[y + dy][x + dx] for y, x in start]
    onward_shove = []

    for n, destination in enumerate(destinations):
        if destination == '#':
            return False

        if destination == '.':
            continue

        if destination == '[':
            y, x = destinations_coord[n]
            onward_shove.append([(y, x), (y, x + 1)])

        if destination == ']':
            y, x = destinations_coord[n]
            onward_shove.append([(y, x - 1), (y, x)])

    _next = all([shove_2(a, _direction, commands) for a in onward_shove])
    if _next:
        if start not in commands:
            commands.append(start)

    if _next and len(start) == 1:
        for c in commands:
            for coord in c:
                y, x = coord
                grid_2[y + dy][x + dx] = grid_2[y][x]
            for coord in c:
                y, x = coord
                grid_2[y][x] = '.'

    return _next


for _dir in directions:
    shove(find_robot(grid), _dir)
    shove_2([find_robot(grid_2)], _dir, [])


def get_gpt(grid):
    ans = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'O' or cell == '[':
                ans += (100 * y) + x
    return ans


print('part 1', get_gpt(grid))
print('part 2', get_gpt(grid_2))
