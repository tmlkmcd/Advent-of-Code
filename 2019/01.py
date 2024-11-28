import sys
import math

total_fuel = 0

def fuel_required(mass):
    my_fuel = max(math.floor(mass / 3) - 2, 0)
    if (my_fuel == 0):
        return 0

    return my_fuel + fuel_required(my_fuel)

for line in sys.stdin:
    mass = int(line.strip())
    total_fuel += fuel_required(mass)

print(total_fuel)