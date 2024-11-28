import sys
import math

lines_in = [line.strip() for line in sys.stdin]
high_count, low_count = 0, 0
waiting = []

class Module:
    def __init__(self, data):
        n, targets = data.split(' -> ')
        t = n[0]

        if t == '%': self.type = 'ff'
        elif t == '&': self.type = 'co'
        else: self.type = 'br'

        self.name = n[1:] if self.type != 'br' else n
        self.targets = targets.split(', ')
        self.on = False
        self.last = {}
        self.sent_high = False

    def register_source(self, source):
        self.last[source] = False
    def receive_pulse(self, source, high=False):
        if self.type == 'ff':
            if high: return
            if self.on: self.send_pulse(False)
            else: self.send_pulse(True)
            self.on = (not self.on)
            return

        self.last[source] = high

        if all([self.last[k] for k in self.last]):
            self.send_pulse(False)
        else: self.send_pulse(True)

    def send_pulse(self, high=False):
        global high_count, low_count, mo

        if high: self.sent_high = True
        for m in self.targets:
            if high: high_count += 1
            else: low_count += 1
            if m != 'output':
                waiting.append({
                    'module': m,
                    'source': self.name,
                    'high': high
                })

mo, pt2 = {}, {}

for l in lines_in:
    m = Module(l)
    mo[m.name] = m

for m in mo:
    for s in mo[m].targets:
        if s == 'rx': continue
        mo[s].register_source(m)

def press():
    global low_count
    low_count += 1
    mo['broadcaster'].send_pulse(False)

for source in mo['cl'].last:
    pt2[source] = -1

for num in range(100000):
    for m in mo:
        mo[m].sent_high = False
    press()
    while len(waiting) > 0:
        a = waiting.pop(0)
        if a['module'] == 'rx': continue
        mo[a['module']].receive_pulse(a['source'], a['high'])
    if num == 1000:
        print('pt1', low_count * high_count)

    for source in mo['cl'].last:
        if mo[source].sent_high:
            pt2[source] = num if pt2[source] == -1 else pt2[source]

    if all([pt2[s] > -1 for s in pt2]): break

print('pt2', math.lcm(*[pt2[s] + 1 for s in pt2]))