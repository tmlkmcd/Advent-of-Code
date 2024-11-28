import sys
import collections

input = [l.strip().split(' ') for l in sys.stdin][0]

players = int(input[0])
marble_limit = int(input[6])


def game(last_marble):
    global players
    scores = [0 for _ in range(players)]

    circle = collections.deque([0])

    current_marble = 1

    while True:
        current_player = current_marble % players
        if current_marble % 23 == 0:
            circle.rotate(7)
            scores[current_player - 1] += current_marble + circle.popleft()
        else:
            circle.rotate(-2)
            circle.appendleft(current_marble)

        if current_marble == last_marble: break
        else:
            current_marble += 1
            current_player %= players

    return scores


print('part 1', max(game(marble_limit)))
print('part 2', max(game(marble_limit * 100)))

