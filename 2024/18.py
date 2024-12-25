test = False

with open("inputs/2024/18-test.txt" if test else "inputs/2024/18.txt", "r") as f:
    content = f.read().split('\n')

size, initial = 7 if test else 71, 12 if test else 1024
start, end = (0, 0), (size - 1, size - 1)
corrupted = [[int(_a) for _a in a.split(',')] for a in content]
corrupted = [(y, x) for x, y in corrupted]


def bfs(num_bits):  # both breadth-first search and brute-force search!! :D
    explored, current, _corrupted = {start: 0}, [start], corrupted[:num_bits]
    for y, x in _corrupted: explored[(y, x)] = '#'

    while current:
        if end in explored: return explored[end]
        y, x = current.pop(0)

        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            yy, xx = y + dy, x + dx
            if (yy, xx) in explored or not (size > yy >= 0 and size > xx >= 0): continue

            explored[(yy, xx)] = explored[(y, x)] + 1
            current.append((yy, xx))

    return explored[end] if end in explored else False


print('part 1', bfs(initial))
for n in range(initial, len(content)):
    if not bfs(n):
        print('part 2', ','.join([str(a) for a in [corrupted[n - 1][1], corrupted[n - 1][0]]]))
        break
