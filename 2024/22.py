with open("inputs/2024/22.txt", "r") as f:
    content = f.read().split('\n')

unique_intervals = set()


class Buyer:
    def __init__(self, sn):
        self.sn = sn
        self.history = [sn % 10]
        self.intervals = dict()

    def generate(self):
        r = self.sn
        r = (r * 64) ^ r
        r %= 16777216
        r = (r // 32) ^ r
        r %= 16777216
        r = (r * 2048) ^ r
        r %= 16777216
        self.sn = r
        bananas = self.sn % 10
        self.history.append(bananas)
        while len(self.history) > 5: self.history.pop(0)
        if len(self.history) < 5: return
        change = (
            self.history[1] - self.history[0],
            self.history[2] - self.history[1],
            self.history[3] - self.history[2],
            self.history[4] - self.history[3]
        )

        while len(self.history) > 4: self.history.pop(0)
        if len(self.history) < 4: return
        unique_intervals.add(change)

        if change not in self.intervals:
            self.intervals[change] = bananas

    def get_interval(self, interval):
        return self.intervals[interval] if interval in self.intervals else 0

    def __int__(self):
        return self.sn


buyers = [Buyer(int(a)) for a in content]
print(f'{len(buyers)} buyers...')
for _ in range(2000):
    for b in buyers: b.generate()

pt1, pt2 = 0, 0
for a in buyers: pt1 += int(a)

for n, interval in enumerate(unique_intervals):
    if n % 400 == 0:
        print(f'part 2: processing {n}/{len(unique_intervals)}')
    amt = 0
    for b in buyers: amt += b.get_interval(interval)
    pt2 = max(pt2, amt)

print('part 1', pt1)
print('part 2', pt2)
