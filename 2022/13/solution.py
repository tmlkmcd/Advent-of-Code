import sys
from functools import cmp_to_key

packets = sys.stdin.read().split('\n\n')
data = [[eval(line) for line in packet.strip().split('\n')] for packet in packets]

def right_order(pair):
    left, right = pair

    if isinstance(left, int) and isinstance(right, int):
        return None if left == right else left < right

    if isinstance(left, list) and isinstance(right, list):
        for n in range(len(left)):
            try:
                so_far_so_good = right_order((left[n], right[n]))
                if so_far_so_good == None: continue
                return so_far_so_good
            except:
                return False

        if len(left) < len(right): return True
        return None

    return right_order(([left], right)) if isinstance(left, int) else right_order((left, [right]))

indices = 0
for n, d in enumerate(data):
    if right_order(d): indices += n + 1

data.append([[[2]], [[6]]])
flattened_data = [item for sublist in data for item in sublist]

sorted_data = sorted(flattened_data, key=cmp_to_key(lambda d1, d2: -1 if right_order((d1, d2)) else 1))
a, b = sorted_data.index([[2]]), sorted_data.index([[6]])

print(f'part 1: {indices}, part 2: {(a + 1) * (b + 1)}')
