import sys

fish = ''
fishes = [] # yes, we are going with 'fishes'
new_fishes = []

class Fish:
    def __init__(self, n):
        self.timer = n

    def tick(self):
        self.timer -= 1
        if self.timer == -1:
            new_fishes.append(Fish(8))
            self.timer = 6

def visualize():
    s = ''
    for f in fishes:
        s += str(f.timer) + ','
    print(s)

for line in sys.stdin:
    fish = line.strip()


for f in fish.split(','):
    fishes.append(Fish(int(f)))


for days in range(80):
    print('day', days)
    for f in fishes:
        f.tick()

    if len(new_fishes) > 0:
        for ff in new_fishes:
            fishes.append(ff)
    new_fishes = []
#     visualize()

print(len(fishes))
