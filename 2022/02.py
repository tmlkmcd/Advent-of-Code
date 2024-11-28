import sys

games = [line.strip().split(' ') for line in sys.stdin]

score_1 = 0
score_2 = 0

# X = A = rock (1)
# Y = B = paper (2)
# Z = C = scissors (3)
# win = 6
# draw = 3
# lose = 0

def play_1(game):
    them, me = game
    if me == 'X':
        if them == 'A': return 1 + 3
        elif them == 'B': return 1 + 0
        elif them == 'C': return 1 + 6
    elif me == 'Y':
        if them == 'A': return 2 + 6
        elif them == 'B': return 2 + 3
        elif them == 'C': return 2 + 0
    elif me == 'Z':
        if them == 'A': return 3 + 0
        elif them == 'B': return 3 + 6
        elif them == 'C': return 3 + 3

def play_2(game):
    them, me = game
    if me == 'X': # lose
        if them == 'A': return 0 + 3
        elif them == 'B': return 0 + 1
        elif them == 'C': return 0 + 2
    elif me == 'Y': # draw
        if them == 'A': return 3 + 1
        elif them == 'B': return 3 + 2
        elif them == 'C': return 3 + 3
    elif me == 'Z': # win
        if them == 'A': return 6 + 2
        elif them == 'B': return 6 + 3
        elif them == 'C': return 6 + 1

for l in games:
    score_1 += play_1(l)
    score_2 += play_2(l)

print('pt1', score_1)
print('pt2', score_2)


