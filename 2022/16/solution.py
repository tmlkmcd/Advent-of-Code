import sys

lines_in = [line.strip() for line in sys.stdin]

valves = dict()
part = 1
t_limit = 26 if part == 2 else 30

p_destinations = dict()

for line in lines_in:
    v, l = line.split('; ')
    vv = v.split(' ')
    valve, flow = vv[1], int(vv[4].split('=')[1])
    leads = l.split(' to ')[1].split(' ')[1:]
    valves[valve] = (flow, [l.strip(',') for l in leads])

def get_all_locations_from(source, depth, targets, route=[]):
    r = route.copy()
    r.append(source)
    for target in valves[source][1]:
        if target in r: continue
        if valves[target][0] > 0:
            if target not in targets or targets[target] > depth + 1:
                targets[target] = depth + 1

        get_all_locations_from(target, depth + 1, targets, r)

    return targets

for v in valves:
    p_destinations[v] = get_all_locations_from(v, 0, dict())

def calc_score(history):
    pressure = 0
    for minute, location in history:
        pressure += (t_limit - minute) * valves[location][0]
    return pressure

ans = 0

def check(history, history_2):
    global his, ans
    score = calc_score(history + history_2)
    if score > ans:
        ans = score


def aim(history=[], history_2=[]):
    if len(history) == 0:
        p_time = 0
        p_location = 'AA'
    else:
        p_time, p_location = history[-1]

    if len(history_2) == 0:
        e_time = 0
        e_location = 'AA'
    else:
        e_time, e_location = history_2[-1]

    destinations = p_destinations[p_location].copy()
    destinations_2 = p_destinations[e_location].copy() if part == 2 else {}
    no_need_1 = [h[1] for h in history]
    no_need_2 = [h[1] for h in history_2] if part == 2 else []

    no_need = no_need_1 + no_need_2

    for n in no_need:
        destinations.pop(n, None)
        destinations_2.pop(n, None)

    if len(destinations) == 0 or len(destinations_2) == 0:
        check(history, history_2)

    if p_time <= e_time or part == 1:
        for d in destinations:
            h = history.copy()
            time_to = p_time + destinations[d] + 1

            if time_to >= t_limit:
                check(history, history_2)
                continue
            h.append((time_to, d))
            aim(h, history_2)
    else:
        for d in destinations_2:
            h = history_2.copy()
            time_to = e_time + destinations_2[d] + 1

            if time_to >= t_limit:
                check(history, history_2)
                continue
            h.append((time_to, d))
            aim(history, h)


aim()

print(f'part {part}', ans)
