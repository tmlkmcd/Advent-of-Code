import sys
from collections import deque
lines_in = [int(line.strip()) for line in sys.stdin]

def mix(q, mix_amt=1):
    Q = deque([complex(l, n + 1) for n, l in enumerate(q)])
    for _ in range(mix_amt):
        for ind in range(len(q)):
            while Q[0].imag != ind + 1: Q.rotate(1)
            a = Q.popleft()
            Q.rotate(int(a.real) * -1)
            Q.appendleft(a)
    return [int(a.real) for a in list(Q)]

Q = mix(lines_in)
zero = Q.index(0)
print('part 1:', sum([Q[(zero + i) % len(Q)] for i in [1000, 2000, 3000]]))

Q2 = [(a * 811589153) for a in lines_in]
Q2 = mix(list(Q2), 10)
zero2 = Q2.index(0)
print('part 2:', sum([Q2[(zero2 + i) % len(Q2)] for i in [1000, 2000, 3000]]))