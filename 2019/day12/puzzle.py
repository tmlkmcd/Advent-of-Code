import sys
import re
import itertools

moon_data = []

part = 1

def extract_moon_data(raw):
    x, y, z = re.findall(r"^<x=(-?\d+), y=(-?\d+), z=(-?\d+)>$", raw)[0]
    return {"x": int(x), "y": int(y), "z": int(z), "vx": 0, "vy": 0, "vz": 0}

for line in sys.stdin:
    moon_data.append(extract_moon_data(line.strip()))

moon_data = {
    "A": moon_data[0],
    "B": moon_data[1],
    "C": moon_data[2],
    "D": moon_data[3]
}

def calculate_gravity(moon1, moon2):
    x1, x2, y1, y2, z1, z2 = moon1["x"], moon2["x"], moon1["y"], moon2["y"], moon1["z"], moon2["z"]
    if x1 > x2:
        moon1["vx"] -= 1
        moon2["vx"] += 1
    elif x1 < x2:
        moon1["vx"] += 1
        moon2["vx"] -= 1

    if y1 > y2:
        moon1["vy"] -= 1
        moon2["vy"] += 1
    elif y1 < y2:
        moon1["vy"] += 1
        moon2["vy"] -= 1
    
    if z1 > z2:
        moon1["vz"] -= 1
        moon2["vz"] += 1
    elif z1 < z2:
        moon1["vz"] += 1
        moon2["vz"] -= 1

moons = ["A", "B", "C", "D"]
def time_step():
    for pair in list(itertools.combinations(moons, 2)):
        moon1, moon2 = pair
        calculate_gravity(moon_data[moon1], moon_data[moon2])
    for moon in moons:
        m = moon_data[moon]
        m["x"] += m["vx"]
        m["y"] += m["vy"]
        m["z"] += m["vz"]

def get_total_energy(moon_data):
    total_energy = 0
    for moon in moon_data:
        m = moon_data[moon]
        p_energy, k_energy = 0, 0

        p_energy += abs(m["x"])
        p_energy += abs(m["y"])
        p_energy += abs(m["z"])
        k_energy += abs(m["vx"])
        k_energy += abs(m["vy"])
        k_energy += abs(m["vz"])
        total_energy += (p_energy * k_energy)
    return total_energy

if part == 1:
    for _ in range(1000):
        time_step()

    print(get_total_energy(moon_data))
    exit()

states = []

def get_state():
    state = []
    for moon in moon_data:
        m = moon_data[moon]
        moon_state = ",".join([
            str(m["x"]),
            str(m["y"]),
            str(m["z"]),
            str(m["vx"]),
            str(m["vy"]),
            str(m["vz"])
        ])
        state.append(moon_state)
    return ";".join(state)

states.append(get_state())
steps = 0
steps_last = 0

while True:
    time_step()
    steps += 1
    if steps > 20000000: break
    if moon_data["A"]["z"] == -7 and moon_data["B"]["z"] == 0 and moon_data["C"]["z"] == -3 and moon_data["D"]["z"] == -13:
        print(steps - steps_last)
        steps_last = steps

# all x positions reset after 231613/231614 steps
# all y positions reset after 193051/193052 steps
# all z positions reset after 102355/102356 steps
# all vx positions reset after 115807 steps
# all vy positions reset after 96526 steps
# all vz positions reset after 51178 steps

# LCM of all of the above is 572087463375796. try simulating that in one lifetime