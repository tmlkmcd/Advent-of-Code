import sys

nums = ''
boards = []
num_boards = 0

def make_num(num_string):
    return int(num_string)

def sanitize_row(row):
    new_row = []

    for n in row.split(' '):
        if n != '': new_row.append(int(n))

    return new_row

class Board:
    def __init__(self, numbers):
        global num_boards
        num_boards += 1
        self.rows = list(map(sanitize_row, numbers))
        self.highlight = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    def register_num(self, num):
        for x, r in enumerate(self.rows):
            for y, n in enumerate(r):
                if n == num: self.highlight[x][y] = 'X'

    def has_bingo(self):
        for x, r in enumerate(self.rows):
            row = True
            for y in range(5):
                if self.highlight[x][y] != 'X':
                    row = False
                    break
            if row == True:
                return True

        for y in range(5):
            column = True
            for x, r in enumerate(self.rows):
                if self.highlight[x][y] != 'X':
                    column = False
                    break
            if column == True:
                return True

        return False

    def get_score(self, last_num):
        score_sum = 0
        for x in range(5):
            for y in range(5):
                if (self.highlight[x][y] != 'X'):
                    score_sum += self.rows[x][y]
        return score_sum * last_num

in_rows = []

for i, line in enumerate(sys.stdin):
    l = line.strip()
    if i == 0: nums = list(map(make_num, l.split(',')))
    elif i >= 2: in_rows.append(l)

index = 6
while True:
    if index > len(in_rows) + 1: break
    boards.append(Board(in_rows[index - 6:index - 1]))
    index += 6

num_boards_win = 0

for n in nums:
    found = False
    for b in boards:
        if (b.has_bingo()): continue
        b.register_num(n)
        if (b.has_bingo()):
            if num_boards_win == 0:
                print('part 1', b.get_score(n))
            num_boards_win += 1

        if num_boards_win == num_boards:
            print('part 2', b.get_score(n))

print(num_boards, num_boards_win)
