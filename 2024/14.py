import re

test = False

with open("inputs/2024/14-test.txt" if test else "inputs/2024/14.txt", "r") as f:
    content = f.read().split('\n')

height = 7 if test else 103
width = 11 if test else 101

half_height = (height // 2)
half_width = (width // 2)

robots = [[int(a) for a in re.findall(r"^p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)[0]] for line in content]


def visualise(steps):
    grid = [['.' for a in range(width)] for b in range(height)]
    for robot in robots:
        grid[robot[1]][robot[0]] = '#'

    longest_streak = 0
    for y in range(height):
        for x in range(width):
            if grid[y][x] == '#':
                streak = 1
                while grid[y][(x + streak) % width] == '#':
                    streak += 1

                if streak > longest_streak:
                    longest_streak = streak

    _longest_streak = 0
    for x in range(width):
        for y in range(height):
            if grid[y][x] == '#':
                streak = 1
                while grid[(y + streak) % height][x] == '#':
                    streak += 1

                if streak > _longest_streak:
                    _longest_streak = streak
    if (longest_streak < 12 and _longest_streak < 12):
        return False

    print('part 2', steps)
    for row in grid: print(''.join(row))
    return True


def step():
    global robots
    for robot in robots:
        robot[0] = (robot[0] + robot[2]) % width
        robot[1] = (robot[1] + robot[3]) % height
    return robots


def get_pt_1():
    global robots
    _robots = [a for a in robots if a[0] != half_width and a[1] != half_height]
    q1, q2, q3, q4 = [], [], [], []

    for robot in _robots:
        if robot[0] < half_width and robot[1] < half_height:
            q1.append(robot)

        if robot[0] < half_width and robot[1] > half_height:
            q2.append(robot)

        if robot[0] > half_width and robot[1] < half_height:
            q3.append(robot)

        if robot[0] > half_width and robot[1] > half_height:
            q4.append(robot)

    return len(q1) * len(q2) * len(q3) * len(q4)


steps_taken = 0
while True:
    step()
    steps_taken += 1

    if steps_taken == 100:
        print('part 1', get_pt_1())

    if steps_taken % 1500 == 0:
        print('finding part 2...', steps_taken)
    if visualise(steps_taken):
        break
