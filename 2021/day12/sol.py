import sys
from collections import Counter

caves = []
part = 2

def find(code):
    for c in caves:
        if c.code == code: return c

    return None

class Cave:
    def __init__(self, code):
        self.code = code
        self.size = 's' if code.islower() else 'l'
        self.connections = []

    def connection(self, connected_to):
        if connected_to not in self.connections:
            self.connections.append(connected_to)

for line in sys.stdin:
    c1, c2 = line.strip().split('-')

    for c in [c1, c2]:
        if find(c) is None:
            caves.append(Cave(c))

    find(c1).connection(c2)
    find(c2).connection(c1)

journeys = []

def navigate(cave, journey=[]):
    for conn in cave.connections:
        conn_cave = find(conn)
        if conn_cave.code == 'end':
            finished_journey = ','.join(journey + [conn_cave.code])
            if finished_journey not in journeys: journeys.append(finished_journey)
            continue

        if conn_cave.code == 'start': continue
        n_journey = journey
        if conn_cave.size == 's' and conn_cave.code in journey:
            if part == 1: continue
            num_times_visited = Counter(journey)[conn_cave.code]

            if num_times_visited == 1 and 'small' not in journey:
                n_journey = journey + ['small']
            else: continue
        navigate(conn_cave, n_journey + [conn_cave.code])

start = find('start')

navigate(start, ['start'])
print('part', part, len(journeys))
