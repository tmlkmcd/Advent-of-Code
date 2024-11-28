import sys

lines_in = [line.strip() for line in sys.stdin]

class Wf:
    def __init__(self):
        self.rules = {}
        self.waiting = []
        self.pt2 = 0

    def register(self, rule):
        name, action = rule.split('{')
        action = action.split('}')[0].split(',')
        steps = []

        for a in action:
            if ':' in a:
                aa = {}
                cond, dest = a.split(':')
                aa['k'] = cond[0]
                aa['check'] = cond[1]
                aa['amt'] = int(cond[2:])
                aa['dest'] = dest
                steps.append(aa)
            else: steps.append(a)

        self.rules[name] = steps

    def apply(self, part, rule_name='in'):
        rules = self.rules[rule_name]

        for r in rules:
            if type(r) != str:
                dest = r['dest']
                if r['check'] == '>' and part[r['k']] <= r['amt']: continue
                if r['check'] == '<' and part[r['k']] >= r['amt']: continue
            else: dest = r

            if dest == 'A': part.accept()
            elif dest == 'R': part.reject()
            else: self.apply(part, dest)

    def filter_2(self, x, m, a, s, k, amt, check):
        xx, mm, aa, ss = [j for j in x], [j for j in m], [j for j in a], [j for j in s]
        xxx, mmm, aaa, sss = [j for j in x], [j for j in m], [j for j in a], [j for j in s]

        if check == '>':
            if k == 'x':
                xx = [j for j in xx if j > amt]
                xxx = [j for j in xxx if j <= amt]
            elif k == 'm':
                mm = [j for j in mm if j > amt]
                mmm = [j for j in mmm if j <= amt]
            elif k == 'a':
                aa = [j for j in aa if j > amt]
                aaa = [j for j in aaa if j <= amt]
            elif k == 's':
                ss = [j for j in ss if j > amt]
                sss = [j for j in sss if j <= amt]
        elif check == '<':
            if k == 'x':
                xx = [j for j in xx if j < amt]
                xxx = [j for j in xxx if j >= amt]
            elif k == 'm':
                mm = [j for j in mm if j < amt]
                mmm = [j for j in mmm if j >= amt]
            elif k == 'a':
                aa = [j for j in aa if j < amt]
                aaa = [j for j in aaa if j >= amt]
            elif k == 's':
                ss = [j for j in ss if j < amt]
                sss = [j for j in sss if j >= amt]
        return xx, mm, aa, ss, xxx, mmm, aaa, sss

    def apply_2(self, x=[], m=[], a=[], s=[], rule_name='in'):
        rules = self.rules[rule_name]
        _x, _m, _a, _s = x, m, a, s

        for r in rules:
            if type(r) != str:
                dest = r['dest']
                xx, mm, aa, ss, _x, _m, _a, _s = self.filter_2(_x, _m, _a, _s, r['k'], r['amt'], r['check'])
            else:
                dest = r
                xx, mm, aa, ss = _x, _m, _a, _s
            if dest == 'R': continue
            if dest == 'A':
                self.pt2 += (len(xx) * len(mm) * len(aa) * len(ss))
                continue
            self.waiting.append({
                'go': dest,
                'x': xx,
                'm': mm,
                'a': aa,
                's': ss
            })

class Part:
    def __init__(self):
        self.state = None

    def from_nums(self, x, m, a, s):
        setattr(self, 'x', x)
        setattr(self, 'm', m)
        setattr(self, 'a', a)
        setattr(self, 's', s)

    def from_string(self, part):
        for rule in part[1:len(part) - 1].split(','):
            k, v = rule.split('=')
            setattr(self, k, int(v))

    def __getitem__(self, item):
        return getattr(self, item)

    def __str__(self):
        return 'x={x}!m=={m}!a==={a}!!s===={s}'.format(x=self['x'],m=self['m'],a=self['a'],s=self['s'])

    def accept(self):
        if self.state is None:
            self.state = 'A'

    def reject(self):
        if self.state is None:
            self.state = 'R'

    def __int__(self):
        return self['x'] + self['m'] + self['a'] + self['s']

wf = Wf()
parts = []

for l in lines_in:
    if l.startswith('{'):
        p = Part()
        p.from_string(l)
        parts.append(p)
    elif l != '':
        wf.register(l)

for part in parts:
    wf.apply(part)

print('pt1', sum([int(p) for p in parts if p.state == 'A']))

x = [i for i in range(1, 4001)]
m = [i for i in range(1, 4001)]
a = [i for i in range(1, 4001)]
s = [i for i in range(1, 4001)]

wf.apply_2(x, m, a, s)

while len([k for k in wf.waiting]) > 0:
    n = wf.waiting.pop(0)
    wf.apply_2(n['x'], n['m'], n['a'], n['s'], n['go'])

print('pt2', wf.pt2)

