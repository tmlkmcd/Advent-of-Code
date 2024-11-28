import sys

lines_in = [line.strip() for line in sys.stdin]

propositions = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}
propositions_name = {0: 'north', 1: 'south', 2: 'west', 3: 'east'}
round_num = 0
not_moving = 'NOT_MOVING'

class Elf:
    def __init__(self, y, x):
        self.y = y
        self.x = x
        self.proposition = None

    def reset(self, move=True):
        if move:
            y, x = self.proposition
            self.y = y
            self.x = x
        self.proposition = None

    def position(self):
        return self.y, self.x

    def move(self, d):
        dy, dx = d
        return self.y + dy, self.x + dx

    def get_all_neighbours(self):
        d = []
        for dy in [-1, 0, 1]:
            for dx in [-1, 0, 1]:
                if dy == 0 and dx == 0: continue
                d.append((self.y + dy, self.x + dx))
        return d

    def get_neighbours(self, flavour):
        d = []
        if flavour == 0: d = [(-1, 0), (-1, 1), (-1, -1)]
        elif flavour == 1: d = [(1, 0), (1, 1), (1, -1)]
        elif flavour == 2: d = [(0, -1), (-1, -1), (1, -1)]
        elif flavour == 3: d = [(0, 1), (-1, 1), (1, 1)]
        assert len(d) > 0
        return [(self.y + dy, self.x + dx) for dy, dx in d]

    def propose(self, positions):
        neighbours = self.get_all_neighbours()
        bad = False
        for n in neighbours:
            if n in positions:
                bad = True
                break
        if not bad:
            self.proposition = not_moving
            return not_moving

        for f in range(4):
            ff = (f + round_num) % 4
            neighbours = self.get_neighbours(ff)
            bad = False
            for n in neighbours:
                if n in positions:
                    bad = True
                    break
            if bad: continue
            self.proposition = self.move(propositions[ff])
            return self.proposition

        self.proposition = self.position()
        return self.proposition

elves = []

for y, l in enumerate(lines_in):
    for x, c in enumerate(list(l)):
        if c == '#':
            elves.append(Elf(y, x))

def visualise(l_elves):
    print('')
    print('======')

    positions = [e.position() for e in l_elves]
    max_x = max(x for y, x in positions)
    min_x = min(x for y, x in positions)
    max_y = max(y for y, x in positions)
    min_y = min(y for y, x in positions)

    range_y = (max_y - min_y) + 4
    range_x = (max_x - min_x) + 4

    positions = [((y - min_y) + 2, (x - min_x) + 2) for y, x in positions]

    for yy in range(range_y):
        row = []
        for xx in range(range_x):
            if (yy, xx) in positions: row.append('#')
            else: row.append('.')
        print(''.join(row))

def round(l_elves):
    global round_num
    positions = [e.position() for e in l_elves]
    propositions = [e.propose(positions) for e in l_elves]

    moved = 0

    for e in l_elves:
        p = e.proposition
        no_need_to_move = p == not_moving
        will_move = (not no_need_to_move) and (propositions.index(p) == (len(propositions) - propositions[-1::-1].index(p) - 1))
        if will_move:
            moved += 1
        e.reset(move=will_move)
    round_num += 1
    print(f'round: {round_num}, num moved: {moved}')
    return len(set(propositions)) == 1 and propositions[0] == not_moving

def count_space(l_elves):
    positions = [e.position() for e in l_elves]

    max_x = max(x for y, x in positions)
    min_x = min(x for y, x in positions)
    max_y = max(y for y, x in positions)
    min_y = min(y for y, x in positions)

    range_y = (max_y - min_y + 1)
    range_x = (max_x - min_x + 1)

    return (range_y * range_x) - len(l_elves)

visualise(elves)

while True:
    none_moved = round(elves)
    if round_num == 10:
        print('part 1:', count_space(elves))

    if none_moved:
        print('part 2:', round_num)
        break


