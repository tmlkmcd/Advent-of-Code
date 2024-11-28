import sys

part = 2

if part == 1:

    h = 0
    d = 0

    for line in sys.stdin:
        cmd, val = line.split(' ')
        val = int(val)

        if cmd == 'forward': h += val
        elif cmd == 'down': d += val
        elif cmd == 'up': d -= val

    print('part 1', h * d)

else:

    h = 0
    d = 0
    a = 0

    for line in sys.stdin:
        cmd, val = line.split(' ')
        val = int(val)

        if cmd == 'forward':
            h += val
            d += (val * a)
        elif cmd == 'down': a += val
        elif cmd == 'up': a -= val

    print('part 2', h * d)
