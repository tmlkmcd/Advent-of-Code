with open("inputs/2024/09.txt", "r") as f:
    content = f.read().split('\n')


class Block:
    def __init__(self, id, num, gap=0, part=1):
        self.id = id
        self.values = [id for _ in range(num)]
        self.gap = gap
        self.part = part
        self.added_values = []

    def __str__(self):
        values = ''.join(str(id) for id in (self.values + self.added_values))
        gap = ''.join(['.' for _ in range(self.gap)])
        return f'{values}{gap}'

    def has_space(self):
        return self.gap > 0

    def has_enough_space(self, other_block):
        return self.gap >= len(other_block.values) and self.id < other_block.id

    def has_blocks(self):
        return len(self.values) > 0

    def take(self, other_block):
        if self.part == 2:
            other_block.added_values = [0 for _ in other_block.values] + other_block.added_values
        if self.gap >= len(other_block.values):
            self.added_values += other_block.values
            self.gap -= len(other_block.values)
            other_block.values = []
        else:
            self.added_values += other_block.values[-1 * self.gap:]
            other_block.values = other_block.values[self.gap:]
            self.gap = 0


input, blocks_1, blocks_2 = [int(a) for a in content[0]], [], []
i = 0

while i < len(input):
    blocks_1.append(Block(i // 2, input[i], input[i + 1] if i + 1 < len(input) else 0))
    blocks_2.append(Block(i // 2, input[i], input[i + 1] if i + 1 < len(input) else 0, 2))
    i += 2

while True:
    first_block_with_gap = next((b for b in blocks_1 if b.has_space()), None)
    last_block_with_numbers = next((b for b in reversed(blocks_1) if b.has_blocks()), None)
    if first_block_with_gap == None or last_block_with_numbers == None or first_block_with_gap == last_block_with_numbers:
        break

    first_block_with_gap.take(last_block_with_numbers)

for block in reversed(blocks_2):
    first_block_with_enough_gap = next((b for b in blocks_2 if b.has_enough_space(block)), None)
    if first_block_with_enough_gap == None:
        continue

    first_block_with_enough_gap.take(block)

pt1_blocks = [x for xx in [b.values + b.added_values for b in blocks_1] for x in xx]
pt2_blocks = [x for xx in [b.values + b.added_values + [0 for _ in range(b.gap)] for b in blocks_2] for x in xx]

print('part 1', sum(i * id for i, id in enumerate(pt1_blocks)))
print('part 2', sum(i * id for i, id in enumerate(pt2_blocks)))
