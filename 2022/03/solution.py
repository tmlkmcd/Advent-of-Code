import sys

lines_in = [line.strip() for line in sys.stdin]


def to_priority(letter):
    ascii_code = ord(letter)
    return ascii_code - 38 if ascii_code <= 90 else ascii_code - 96


assert(to_priority('a') == 1)
assert(to_priority('z') == 26)
assert(to_priority('A') == 27)
assert(to_priority('Z') == 52)

dupes = []

for backpack in lines_in:
    assert(len(backpack) % 2 == 0)
    half = len(backpack) // 2
    for c in backpack[half:]:
        if c in backpack[:half]:
            dupes.append(c)
            break

pointer = 0
badges = []

while pointer < len(lines_in):
    group = lines_in[pointer:pointer + 3]
    assert(len(group) == 3)
    pointer += 3

    for c in group[0]:
        if c in group[1] and c in group[2]:
            badges.append(c)
            break

print('part 1', sum([to_priority(i) for i in dupes]))
print('part 2', sum([to_priority(b) for b in badges]))
