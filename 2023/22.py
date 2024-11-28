import sys

lines_in = [line.strip() for line in sys.stdin]

class Pile:
    def __init__(self):
        self.bricks = []

    def add_brick(self, brick):
        self.bricks.append(brick)

    def drop(self):
        moved = False
        self.bricks = sorted(self.bricks, key=lambda brick: brick.get_lowest_z())
        for n, b in enumerate(self.bricks):
            m = b.drop(self.bricks[0:n])
            if m: moved = True
        return moved

    def set_supports(self):
        self.bricks = sorted(self.bricks, key=lambda brick: brick.get_lowest_z())

        for n, b in enumerate(self.bricks):
            s = [a for a in self.bricks if b.is_supporting(a)]
            b.supporting = s
            for ss in s:
                ss.supported_by.append(b)
    def pt1_ans(self):
        self.set_supports()
        ans = 0
        for b in self.bricks:
            if all([
                len(bb.supported_by) > 1 for bb in b.supporting
            ]): ans += 1
        return ans

    def pt2_ans(self):
        ans = 0
        for n, b in enumerate(self.bricks):
            print('calculating', n, 'out of', len(self.bricks))
            for bb in self.bricks:
                bb.pretend_fall = False
            ans += len([k for k in b.supporting_chain()])
        return ans


class Brick:
    def __init__(self, line, c):
        self.c = c
        for n, coord in enumerate(line.split('~')):
            x, y, z = [int(a) for a in coord.split(',')]
            if n == 0:
                self.x1 = x
                self.y1 = y
                self.z1 = z
            else:
                self.x2 = x
                self.y2 = y
                self.z2 = z

        self.x_y = set([
            (self.x1, y) for y in range(*self.lowest_first([self.y1, self.y2]))
        ]) if self.x1 == self.x2 else set([
            (x, self.y1) for x in range(*self.lowest_first([self.x1, self.x2]))
        ])

        self.supporting = []
        self.supported_by = []
        self.supporting_total = None
        self.pretend_fall = False

    def get_lowest_z(self):
        return min(self.z1, self.z2)

    def get_highest_z(self):
        return max(self.z1, self.z2)

    def intersects(self, other_brick):
        if self.c == other_brick.c: return False
        return len(list(self.x_y & other_brick.x_y)) > 0

    def is_supporting(self, other_brick):
        if self.c == other_brick.c: return False
        return self.intersects(other_brick) and self.get_highest_z() == other_brick.get_lowest_z() - 1

    def lowest_first(self, list):
        if list[0] <= list[1]: return [list[0], list[1] + 1]
        return [list[1], list[0] + 1]

    def drop(self, below):
        lowest = 1
        for brick in reversed(below):
            if self.intersects(brick):
                if brick.get_highest_z() > self.get_lowest_z(): continue
                lowest = max(brick.get_highest_z() + 1, lowest)

        delta = self.get_lowest_z() - lowest
        if delta == 0: return False
        self.z1 -= delta
        self.z2 -= delta
        return True

    def supporting_chain(self):
        current_set = set()
        self.pretend_fall = True
        for b in self.supporting:
            if all(bb.pretend_fall for bb in b.supported_by):
                b.pretend_fall = True
        for b in self.supporting:
            if all(bb.pretend_fall for bb in b.supported_by):
                current_set.add(b.c)
                current_set.update(b.supporting_chain())
        return current_set

pile = Pile()
for a, line in enumerate(lines_in):
    b = Brick(line, chr(ord('A') + a))
    pile.add_brick(b)

moved = True
while moved: moved = pile.drop()

print('part 1', pile.pt1_ans())
print('part 2', pile.pt2_ans())
