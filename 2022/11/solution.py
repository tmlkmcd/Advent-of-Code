import sys

input_each = sys.stdin.read().split('\n\n')
part = 2
divisors = 1

class Monkey:
    def __init__(self, text):
        global divisors
        m_number, items, operation, test, if_true, if_false = text.split('\n')
        self.number = int(m_number[7])
        self.items = [int(a) for a in items.split(': ')[1].split(', ')]
        self.test = int(test.split(' by ')[1])
        divisors *= self.test
        self.if_true = int(if_true[-1])
        self.if_false = int(if_false[-1])
        self.score = 0
        self.targets = dict()

        old, operator, value = operation.split(' = ')[1].split(' ')
        self.operator = operator
        self.op_value = value

    def operation(self, item):
        if self.operator == '+':
            return item + int(self.op_value)
        return item * (item if self.op_value == 'old' else int(self.op_value))

    def keep_away(self):
        for _ in range(len(self.items)):
            self.score += 1
            item = self.items.pop(0)
            item = self.operation(item)

            if part == 1: item = item // 3
            item %= divisors

            if item % self.test == 0: throw_to = monkeys[self.if_true]
            else: throw_to = monkeys[self.if_false]
            throw_to.items.append(item)

monkeys = [Monkey(m) for m in input_each]

for _ in range(20 if part == 1 else 10000):
    for monkey in monkeys:
        monkey.keep_away()

scores = [m.score for m in monkeys]
scores.sort(reverse=True)
print(scores[0] * scores[1])
