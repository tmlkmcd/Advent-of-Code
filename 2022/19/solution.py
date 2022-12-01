import sys
import re
import math
from collections import defaultdict
from functools import reduce

lines_in = [line.strip() for line in sys.stdin]
part = 2
if part == 2: print('brace yourselves, this could take a little while...')
t_limit = 24 if part == 1 else 32
production_levels = [0] + [0 for blueprint in lines_in]

class Blueprint:
    def __init__(self, line_in):
        num, ore, clay, obs_1, obs_2, geo_1, geo_2 = [int(a) for a in re.findall(r'-?\d+', line_in)]

        self.num = num
        self.ore = ore  # consumes ore
        self.clay = clay  # consumes ore
        self.obsidian = [obs_1, obs_2]  # consumes ore and clay
        self.geode = [geo_1, geo_2]  # consumes ore and obsidian

        self.max_ore_consumption = max(ore, clay, obs_1, geo_1)
        self.max_clay_consumption = obs_2
        self.max_obsidian_consumption = geo_2


class Outcome:
    def __init__(self, blueprint: Blueprint, ore=0, clay=0, obsidian=0, geode=0, ore_robot=1, clay_robot=0, obsidian_robot=0, geode_robot=0, time=0, precursors=[]):
        self.blueprint = blueprint
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian
        self.geode = geode
        self.ore_robot = ore_robot
        self.clay_robot = clay_robot
        self.obsidian_robot = obsidian_robot
        self.geode_robot = geode_robot
        self.time = time
        self.precursors = precursors

    def __eq__(self, other):
        return self.blueprint.num == other.blueprint.num \
            and self.ore == other.ore \
            and self.clay == other.clay \
            and self.obsidian == other.obsidian \
            and self.geode == other.geode \
            and self.ore_robot == other.ore_robot \
            and self.clay_robot == other.clay_robot \
            and self.obsidian_robot == other.obsidian_robot \
            and self.geode_robot == other.geode_robot \
            and self.time == other.time

    def __hash__(self):
        return hash(('or', self.ore,
                     'cl', self.clay,
                     'ob', self.obsidian,
                     'ge', self.geode,
                     'orr', self.ore_robot,
                     'clr', self.clay_robot,
                     'obr', self.obsidian_robot,
                     'ger', self.geode_robot,
                     't', self.time))

    def copy(self, ore=None, clay=None, obsidian=None, geode=None, ore_robot=None, clay_robot=None, obsidian_robot=None, geode_robot=None, time_taken=0):
        return Outcome(
            blueprint=self.blueprint,
            ore=self.ore if ore is None else ore,
            clay=self.clay if clay is None else clay,
            obsidian=self.obsidian if obsidian is None else obsidian,
            geode=self.geode if geode is None else geode,
            ore_robot=self.ore_robot if ore_robot is None else ore_robot,
            clay_robot=self.clay_robot if clay_robot is None else clay_robot,
            obsidian_robot=self.obsidian_robot if obsidian_robot is None else obsidian_robot,
            geode_robot=self.geode_robot if geode_robot is None else geode_robot,
            time=self.time + time_taken,
            precursors=self.precursors + [hash(self)]
        )

    def propagate(self, examined):
        global production_levels
        if hash(self) in examined: return []

        possibilities = []

        if self.ore_robot < self.blueprint.max_ore_consumption:
            time_taken = 1 + max(0, math.ceil((self.blueprint.ore - self.ore) / self.ore_robot))
            if self.time + time_taken < t_limit:
                possibilities.append(self.copy(
                    ore=self.ore + (self.ore_robot * time_taken) - self.blueprint.ore,
                    clay=self.clay + (self.clay_robot * time_taken),
                    obsidian=self.obsidian + (self.obsidian_robot * time_taken),
                    geode=self.geode + (self.geode_robot * time_taken),
                    ore_robot=self.ore_robot + 1,
                    clay_robot=self.clay_robot,
                    obsidian_robot=self.obsidian_robot,
                    geode_robot=self.geode_robot,
                    time_taken=time_taken
                ))

        if self.clay_robot < self.blueprint.max_clay_consumption:
            time_taken = 1 + max(0, math.ceil((self.blueprint.clay - self.ore) / self.ore_robot))
            if self.time + time_taken < t_limit:
                possibilities.append(self.copy(
                    ore=self.ore + (self.ore_robot * time_taken) - self.blueprint.clay,
                    clay=self.clay + (self.clay_robot * time_taken),
                    obsidian=self.obsidian + (self.obsidian_robot * time_taken),
                    geode=self.geode + (self.geode_robot * time_taken),
                    ore_robot=self.ore_robot,
                    clay_robot=self.clay_robot + 1,
                    obsidian_robot=self.obsidian_robot,
                    geode_robot=self.geode_robot,
                    time_taken=time_taken
                ))

        if self.clay_robot > 0 and self.obsidian_robot < self.blueprint.max_obsidian_consumption:
            time_taken = 1 + max(
                0,
                math.ceil((self.blueprint.obsidian[0] - self.ore) / self.ore_robot),
                math.ceil((self.blueprint.obsidian[1] - self.clay) / self.clay_robot)
            )
            if self.time + time_taken < t_limit:
                possibilities.append(self.copy(
                    ore=self.ore + (self.ore_robot * time_taken) - self.blueprint.obsidian[0],
                    clay=self.clay + (self.clay_robot * time_taken) - self.blueprint.obsidian[1],
                    obsidian=self.obsidian + (self.obsidian_robot * time_taken),
                    geode=self.geode + (self.geode_robot * time_taken),
                    ore_robot=self.ore_robot,
                    clay_robot=self.clay_robot,
                    obsidian_robot=self.obsidian_robot + 1,
                    geode_robot=self.geode_robot,
                    time_taken=time_taken
                ))

        if self.obsidian_robot > 0:
            time_taken = 1 + max(
                0,
                math.ceil((self.blueprint.geode[0] - self.ore) / self.ore_robot),
                math.ceil((self.blueprint.geode[1] - self.obsidian) / self.obsidian_robot)
            )
            if self.time + time_taken < t_limit:
                possibilities.append(self.copy(
                    ore=self.ore + (self.ore_robot * time_taken) - self.blueprint.geode[0],
                    clay=self.clay + (self.clay_robot * time_taken),
                    obsidian=self.obsidian + (self.obsidian_robot * time_taken) - self.blueprint.geode[1],
                    geode=self.geode + (self.geode_robot * time_taken),
                    ore_robot=self.ore_robot,
                    clay_robot=self.clay_robot,
                    obsidian_robot=self.obsidian_robot,
                    geode_robot=self.geode_robot + 1,
                    time_taken=time_taken
                ))

        if len(possibilities) == 0:
            production_levels[self.blueprint.num] = max(
                self.geode + ((t_limit - self.time) * self.geode_robot),
                production_levels[self.blueprint.num]
            )
            for p in self.precursors: examined[p] = True
            return []

        return possibilities

blueprints = [Blueprint(line) for line in lines_in]
if part == 2: blueprints = blueprints[0:3]

def examine_possibilities(outcomes, examined):
    possibilities = [o.propagate(examined) for o in outcomes]
    for p in possibilities: examine_possibilities(p, examined)

for n, b in enumerate(blueprints):
    print(f'{n + 1} out of {len(blueprints)}')
    possibilities = [Outcome(blueprint=b)]
    examined = defaultdict(int)
    examine_possibilities(possibilities, examined)

if part == 1: print('part 1', sum([n * a for n, a in enumerate(production_levels)]))
else: print('part 2', reduce(lambda aa, bb: aa * bb, [a for a in production_levels if a > 0]))
