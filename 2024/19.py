with open("inputs/2024/19.txt", "r") as f:
    content = f.read().split('\n\n')

available, patterns = content[0].split(', '), content[1].split('\n')
remember = dict()


def find(remaining):
    if remaining in remember: return remember[remaining]

    ans = 0
    if not remaining:
        ans += 1
        return ans
    for n, p in enumerate(available):
        if remaining.startswith(p):
            ans += find(remaining[len(p):])
    remember[remaining] = ans
    return ans


pt1, pt2 = 0, 0
for n, p in enumerate(patterns):
    found = find(p)
    pt2 += found
    if found > 0: pt1 += 1

print('part 1', pt1)
print('part 2', pt2)
