import sys
import math
import collections
import itertools

lines_in = [line.replace('\n', '') for line in sys.stdin]
grid = [list(line) for line in lines_in]

turn = ['l', 's', 'r']


class Cart:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        self.turn = 0
        self.crashed = False

    def __lt__(self, other):
        if self.y < other.y:
            return True
        if self.y > other.y:
            return False

        return self.x < other.x

    def __str__(self):
        return f'Cart: ({self.x}, {self.y}, {self.dir})'

    def move(self):
        if self.dir == 'v':
            self.y += 1
        elif self.dir == '^':
            self.y -= 1
        elif self.dir == '<':
            self.x -= 1
        elif self.dir == '>':
            self.x += 1

    def junction(self):
        old_dir = self.dir
        turn_dir = turn[self.turn]
        if self.turn == 0:
            if self.dir == 'v':
                self.dir = '>'
            elif self.dir == '>':
                self.dir = '^'
            elif self.dir == '^':
                self.dir = '<'
            elif self.dir == '<':
                self.dir = 'v'
        elif self.turn == 2:
            if self.dir == 'v':
                self.dir = '<'
            elif self.dir == '<':
                self.dir = '^'
            elif self.dir == '^':
                self.dir = '>'
            elif self.dir == '>':
                self.dir = 'v'
        self.turn = (self.turn + 1) % len(turn)

    def corner(self, corner_type):
        old_dir = self.dir
        if corner_type == '\\':
            if self.dir == 'v':
                self.dir = '>'
            elif self.dir == '^':
                self.dir = '<'
            elif self.dir == '>':
                self.dir = 'v'
            elif self.dir == '<':
                self.dir = '^'
        elif corner_type == '/':
            if self.dir == 'v':
                self.dir = '<'
            elif self.dir == '^':
                self.dir = '>'
            elif self.dir == '<':
                self.dir = 'v'
            elif self.dir == '>':
                self.dir = '^'

carts = []

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell in 'v^<>':
            carts.append(Cart(x, y, cell))
            grid[y][x] = '|' if cell in 'v^' else '-'


part_1 = None

def tick():
    global part_1
    carts.sort()
    for _, c in enumerate(carts):
        if c.crashed: continue
        c.move()

        y = c.y
        x = c.x

        try:
            if grid[y][x] == '+': c.junction()

            if grid[y][x] == '\\' or grid[y][x] == '/':
                c.corner(grid[y][x])
        except:
            print(c.history)
            return True

        for cc in carts:
            if c == cc: continue
            if cc.crashed: continue

            if c.y == cc.y and c.x == cc.x:
                if part_1 is None: part_1 = (c.x, c.y)
                c.crashed = True
                cc.crashed = True

while True:
    num_carts = tick()
    if len([cart for cart in carts if cart.crashed is False]) == 1:
        break

print('part 1', part_1)
print('part 2', [(cart.x, cart.y) for cart in carts if cart.crashed is False])

