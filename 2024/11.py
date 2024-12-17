with open("inputs/2024/11.txt", "r") as f:
    content = f.read().split(' ')


def blink_stone(num):
    if num == '0': return ['1']

    if len(num) % 2 == 0:
        half_digits = len(num) // 2
        return [str(int(a)) for a in [num[:half_digits], num[half_digits:]]]

    return [str(int(num) * 2024)]


def get_ans(_a):
    ans = 0
    for keys in _a: ans += _a[keys]
    return ans


a = dict()
for n in content:
    if n in a:
        a[n] += 1
    else:
        a[n] = 1

for i in range(75):
    b = dict()
    for key in a:
        c = blink_stone(key)
        for n in c:
            if n in b:
                b[n] += (1 * a[key])
            else:
                b[n] = (1 * a[key])
    a = b

    if i == 24: print('part 1', get_ans(a))
print('part 2', get_ans(a))
