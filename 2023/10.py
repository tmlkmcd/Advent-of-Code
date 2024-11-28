import sys

grid = [list(line.strip()) for line in sys.stdin]
max_y, max_x = len(grid), len(grid[0])
step_map, wrapped_map = {}, {}

class Coord:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __add__(self, other):
        return Coord(self.y + other.y, self.x + other.x)

    def __str__(self):
        return '({y}, {x})'.format(y=self.y, x=self.x)

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

    def is_valid(self):
        global max_y, max_x
        return 0 <= self.x < max_x and 0 <= self.y < max_y

    def get_value(self):
        global grid
        if not self.is_valid():
            raise "Invalid coordinate {coord}".format(coord=self)
        val = grid[self.y][self.x]
        return 'F' if val == 'S' else val


movement = {
    'l': Coord(0, -1),
    'r': Coord(0, 1),
    'u': Coord(-1, 0),
    'd': Coord(1, 0)
}

inner_check = {
    '-': {
        'u': [movement['d']],
        'd': [movement['u']]
    },
    '|': {
        'l': [movement['r']],
        'r': [movement['l']]
    },
    'F': {
        'l': [Coord(1, 1)],
        'r': [movement['l'], movement['u'], Coord(-1, -1)]
    },
    'L': {
        'l': [Coord(-1, 1)],
        'r': [movement['l'], movement['d'], Coord(1, -1)]
    },
    'J': {
        'l': [movement['r'], movement['d'], Coord(1, 1)],
        'r': [Coord(-1, -1)]
    },
    '7': {
        'l': [movement['r'], movement['u'], Coord(-1, 1)],
        'r': [Coord(1, -1)]
    }
}



def find_s():
    global grid
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'S':
                cell = Coord(y, x)
                proceed = []
                for m in movement:
                    new_cell = cell + movement[m]
                    if not new_cell.is_valid(): continue
                    adjacent = new_cell.get_value()
                    if m == 'r' and adjacent in '-7J' \
                            or m == 'l' and adjacent in '-FL' \
                            or m == 'u' and adjacent in '7F|' \
                            or m == 'd' and adjacent in 'JL|':
                        proceed.append(m)
                return cell, proceed

starting_cell, proceed = find_s()
step_map[str(starting_cell)] = 0

def get_next_direction(current_direction, piece):
    if current_direction == 'r':
        match piece:
            case '7': return 'd'
            case 'J': return 'u'
            case '-': return 'r'
    elif current_direction == 'l':
        match piece:
            case 'L': return 'u'
            case 'F': return 'd'
            case '-': return 'l'
    elif current_direction == 'u':
        match piece:
            case '7': return 'l'
            case 'F': return 'r'
            case '|': return 'u'
    elif current_direction == 'd':
        match piece:
            case 'J': return 'l'
            case 'L': return 'r'
            case '|': return 'd'
    raise 'Unknown next, {current}, {piece}'.format(current=current_direction, piece=piece)

def get_next_facing(piece, next_piece, current_facing):
    if piece == '|' or next_piece == '|': return current_facing

    if piece == 'F':
        if next_piece == '-':
            return 'd' if current_facing == 'r' else 'u'
        if next_piece == '7' : return 'l' if current_facing == 'r' else 'r'
    elif piece == 'J':
        if next_piece == '-': return 'd' if current_facing == 'r' else 'u'
        if next_piece == 'L': return 'l' if current_facing == 'r' else 'r'
    elif piece == '7':
        if next_piece == '-': return 'u' if current_facing == 'r' else 'd'
        if next_piece == 'F': return 'l' if current_facing == 'r' else 'r'
    elif piece == 'L':
        if next_piece == '-': return 'u' if current_facing == 'r' else 'd'
        if next_piece == 'J': return 'l' if current_facing == 'r' else 'r'
    elif piece == '-':
        if next_piece == '7' or next_piece == 'L':
            return 'l' if current_facing == 'd' else 'r'
        if next_piece == 'J' or next_piece == 'F':
            return 'l' if current_facing == 'u' else 'r'

    return current_facing

def crawl_inner(coord):
    global inner_check, grid, step_map, wrapped_map
    s = str(coord)
    if not coord.is_valid() or s in step_map or s in wrapped_map: return
    wrapped_map[s] = True
    for m in movement:
        crawl_inner(coord + movement[m])

def crawl(starting_coord, starting_direction, part=1):
    global grid, step_map, wrapped_map
    current_coord, current_direction = starting_coord, starting_direction
    last_value = starting_coord.get_value()
    current_facing = 'l'
    steps = 0

    while True:
        steps += 1
        current_coord += movement[current_direction]
        if str(current_coord) in step_map:
            step_map[str(current_coord)] = min(step_map[str(current_coord)], steps)
        else: step_map[str(current_coord)] = steps
        if current_coord == starting_coord: break
        cell_value = current_coord.get_value()
        current_facing = get_next_facing(last_value, cell_value, current_facing)
        if part == 2:
            for dir in inner_check[cell_value][current_facing]:
                crawl_inner(current_coord + dir)
        current_direction = get_next_direction(current_direction, cell_value)
        last_value = cell_value


for p in proceed:
    crawl(starting_cell, p)

print('part 1', max(*[step_map[k] for k in step_map]))

c = None
for x in range(max_x):
    c = Coord(0, x)
    if grid[0][x] == 'F' and str(c) in step_map: break

crawl(c, 'r', 2)
print('part 2', len([a for a in wrapped_map]))
