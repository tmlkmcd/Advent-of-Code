with open("inputs/2024/25.txt", "r") as f:
    content = f.read().split('\n\n')

keys, locks = [], []


def parse_block(block):
    lines = block.split('\n')
    amt = []
    for x in range(5):
        amt.append([lines[y][x] for y in range(len(lines))].count('#') - 1)

    if all(l == '#' for l in lines[0]):
        locks.append(amt)

    else:
        keys.append(amt)


for b in content:
    parse_block(b)

ans = 0

for k in keys:
    for l in locks:
        fits = True
        for r in range(5):
            if k[r] + l[r] > 5:
                fits = False
                break
        if fits:
            ans += 1
        else:
            continue

print(ans)
