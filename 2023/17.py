import sys

lines_in = [line.strip() for line in sys.stdin]
grid = [[int(i) for i in list(line)] for line in lines_in]
visited, shortest = {}, 1e9
waiting = {
    (0, 0, ''): [0, [(0, 0)]]
}

sp = [1e9]

part = 2

max_y, max_x = len(grid), len(grid[0])
start, end = (0, 0), (max_y - 1, max_x - 1)

def opposite(direction):
    if direction == 'u': return 'd'
    if direction == 'l': return 'r'
    if direction == 'd': return 'u'
    if direction == 'r': return 'l'

def navigate(current_score, current, path=[]):
    global sp, shortest
    if current in visited: return
    visited[current] = current_score

    for direction in 'uldr':
        y, x, streak = current
        if direction == 'u': y -= 1
        elif direction == 'd': y += 1
        elif direction == 'l': x -= 1
        elif direction == 'r': x += 1

        if x >= max_x or y >= max_y or x < 0 or y < 0: continue
        if (y, x) in path: continue
        potential_score = current_score + grid[y][x]

        if len(streak) > 0 and direction == streak[0]:
            if len(streak) == 3: continue
            n_streak = streak + direction
        else:
            n_streak = direction

        n_path = path + [(y, x)]
        n_current = (y, x, n_streak)
        if (y, x) == end:
            if shortest > potential_score:
                shortest = potential_score
                sp = [shortest, n_path]

        if n_current in waiting and waiting[n_current][0] <= potential_score: continue
        waiting[n_current] = [potential_score, n_path]

def navigate2(current_score, current, path=[]):
    global sp, shortest
    if current in visited: return
    visited[current] = current_score

    for next_dir in 'uldr':
        y, x, current_dir = current
        if len(current_dir) > 0:
            if next_dir == current_dir[0]: continue
            if next_dir == opposite(current_dir[0]): continue

        n_path_addition = []
        potential_score = current_score

        for turn_steps in range(3):
            if next_dir == 'u': y -= 1
            elif next_dir == 'd': y += 1
            elif next_dir == 'l': x -= 1
            elif next_dir == 'r': x += 1

            n_path_addition.append((y, x))
            if x >= max_x or y >= max_y or x < 0 or y < 0: break
            potential_score += grid[y][x]

        if x >= max_x or y >= max_y or x < 0 or y < 0: continue


        for turn_steps in range(7):
            if next_dir == 'u': y -= 1
            elif next_dir == 'd': y += 1
            elif next_dir == 'l': x -= 1
            elif next_dir == 'r': x += 1

            if x >= max_x or y >= max_y or x < 0 or y < 0: break

            n_path_addition.append((y, x))
            potential_score += grid[y][x]

            n_path = path + n_path_addition
            n_current = (y, x, next_dir)

            if (y, x) == end:
                if shortest > potential_score:
                    shortest = potential_score
                    sp = [shortest, n_path]

            if n_current in waiting and waiting[n_current][0] <= potential_score: continue
            waiting[n_current] = [potential_score]



while True:
    if len([k for k in waiting]) == 0: break
    # print('waiting', len([k for k in waiting]))

    min_s = [1e9]
    for k in waiting:
        sc, p = waiting[k]
        if sc <= min_s[0]: min_s = [sc, k, p]

    del waiting[min_s[1]]
    if part == 1: navigate(*min_s)
    else: navigate2(*min_s)

print(shortest)


