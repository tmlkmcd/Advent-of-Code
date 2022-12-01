import sys

lines_in = [line.strip() for line in sys.stdin]
strings = lines_in[0].split(',')


def p_hash(string, part=1):
    s = string
    if part == 2:
        if '=' in s: s = s.split('=')[0]
        elif '-' in s: s = s.split('-')[0]
    current = 0
    for c in s:
        current += ord(c)
        current *= 17
        current %= 256
    return current

class Box:
    def __init__(self, index):
        self.number = index
        self.lenses = {}

    def push(self):
        arr = sorted([k for k in self.lenses])
        arr = [self.lenses[k] for k in arr]
        self.lenses = {}
        for i, k in enumerate(arr): self.lenses[i] = k

    def dash(self, label):
        for k in self.lenses:
            if self.lenses[k]['label'] == label:
                del self.lenses[k]
                self.push()
                break

    def eq(self, label, fl):
        for k in self.lenses:
            if self.lenses[k]['label'] == label:
                self.lenses[k] = {
                    'label': label,
                    'fl': fl
                }
                return

        highest_k = max([k for k in self.lenses]) if len([k for k in self.lenses]) > 0 else -1
        self.lenses[highest_k + 1] = {
            'label': label,
            'fl': fl
        }

    def __int__(self):
        t = 0
        for k in self.lenses:
            t += (self.number + 1) * (k + 1) * self.lenses[k]['fl']
        return t



boxes = [Box(index) for index in range(256)]

for string in strings:
    h = p_hash(string, 2)
    if '=' in string:
        label, fl = string.split('=')
        boxes[h].eq(label, int(fl))
    elif '-' in string:
        label = string.split('-')[0]
        boxes[h].dash(label)

print('part 1', sum([p_hash(string) for string in strings]))
print('part 2', sum([int(b) for b in boxes]))
