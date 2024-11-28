import sys

class School:
    def __init__(self, fish_input):
        self.timers = [0, 0, 0, 0, 0, 0, 0, 0, 0]

        for s in fish_input.split(','):
            index = int(s)
            self.timers[index] += 1

    def tick(self):
        new_timers = [
            self.timers[1],
            self.timers[2],
            self.timers[3],
            self.timers[4],
            self.timers[5],
            self.timers[6],
            self.timers[7] + self.timers[0],
            self.timers[8],
            self.timers[0]
        ]

        self.timers = new_timers

    def total(self):
        tot = 0
        for n in self.timers:
            tot += n

        return tot


school = ''

for line in sys.stdin:
    school = School(line.strip())

for days in range(256):
    school.tick()
print(school.total())
