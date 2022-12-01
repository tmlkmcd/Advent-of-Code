import sys

lines_in = [line for line in sys.stdin]
part, c_pointer = 1, 8

crates = lines_in[:c_pointer]
instructions = [line.split(' ') for line in lines_in[c_pointer + 2:]]
p_instructions = [[int(a) * -1, int(b), int(c)] for _, a, _, b, _, c in instructions]
stacks = ['']

for n, l in enumerate(lines_in[c_pointer]):
    if l.strip() == '': continue

    stacks.append([])
    for nn in reversed(range(c_pointer)):
        c = crates[nn][n]
        if c == ' ': break
        stacks[len(stacks) - 1].append(c)

for num, from_pile, to_pile in p_instructions:
    moving = stacks[from_pile][num:]
    stacks[to_pile] += moving if part == 2 else reversed(moving)
    stacks[from_pile] = stacks[from_pile][:num]

last = [s[1] for s in stacks[1:]]
print(f'part {part}:', ''.join(last))
