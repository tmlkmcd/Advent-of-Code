# this file is a mess but i'm not such a skilled python programmer that i can figure out the solutions to this kind of problem more elegantly - yet
# just watched https://www.youtube.com/watch?v=tMPQp60q9GA - maybe i should consider another career

import sys

wires = []

for line in sys.stdin:
    wire = line.strip()
    wire_sections = [[x[0], int(x[1:])] for x in wire.split(",")]
    wires.append(wire_sections)

grid = []

max_x = 0
min_x = 0
max_y = 0
min_y = 0

for wire in wires:
    curr_x = 0
    curr_y = 0
    for section in wire:
        direction, distance = section
        if (direction == "U"): curr_y += distance
        if (direction == "D"): curr_y -= distance
        if (direction == "R"): curr_x += distance
        if (direction == "L"): curr_x -= distance

        if (max_y < curr_y): max_y = curr_y
        if (min_y > curr_y): min_y = curr_y
        if (max_x < curr_x): max_x = curr_x
        if (min_x > curr_x): min_x = curr_x

for y in range(abs(max_y) + abs(min_y) + 3):
    grid.append([])
    for x in range(abs(max_x) + abs(min_x) + 3):
        grid[y].append(".")

def visualize(grid):
    newgrid = grid.copy()
    newgrid.reverse()
    for row in newgrid:
        print("".join(row))

starting_x = abs(min_x) + 1
starting_y = abs(min_y) + 1
x = starting_x
y = starting_y
lowest_x = 0
lowest_y = 0
grid[y][x] = "o"

def draw(n, y, x, direction):
    try:
        if (grid[y][x] != "." and grid[y][x] != str(n)):
            char = "X"
        else:
            char = str(n)
    except:
        print(len(grid), len(grid[0]))
        print(y, x)
    
    grid[y][x] = char

for n, wire in enumerate(wires):
    x = starting_x
    y = starting_y
    for j, section in enumerate(wire):
        direction, length = section
        if (direction == "U"):
            for i in range(length):
                y += 1
                draw(n, y, x, direction)
        elif (direction == "D"):
            for i in range(length):
                y -= 1
                draw(n, y, x, direction)
        elif (direction == "R"):
            for i in range(length):
                x += 1
                draw(n, y, x, direction)
        elif (direction == "L"):
            for i in range(length):
                x -= 1
                draw(n, y, x, direction)

closest_x = 5000
intersections = []
for y, row in enumerate(grid):
    for x, item in enumerate(row):
        if (item == "X"):
            intersections.append([y, x])
            m_distance = abs(y - starting_y) + abs(x - starting_x)
            
            if (m_distance < closest_x):
                closest_x = m_distance

print("part 1", closest_x)
# visualize(grid)

# part 2

print(intersections)

distances_to_intersections = []

for point in intersections:
    total_distance_to_point = 0
    for wire in wires:
        distance_traversed = 0
        x = starting_x
        y = starting_y
        for section in wire:
            direction, distance = section
            if (y == point[0] and ((direction == "R" and x + distance >= point[1]) or (direction == "L" and x - distance <= point[1]))):
                if (direction == "R" and x + distance >= point[1]):
                    distance_traversed += (point[1] - x)
                    break
                elif (direction == "L" and x - distance <= point[1]):
                    distance_traversed += (x - point[1])
                    break
            elif (x == point[1] and ((direction == "U" and y + distance >= point[0]) or (direction == "D" and y - distance <= point[0]))):
                if (direction == "U" and y + distance >= point[0]):
                    distance_traversed += (point[0] - y)
                    break
                elif (direction == "D" and y - distance <= point[0]):
                    distance_traversed += (y - point[0])
                    break

            # the next section will not hit the intersection in question
            distance_traversed += distance
            if (direction == "U"): y += distance
            elif (direction == "D"): y -= distance
            elif (direction == "R"): x += distance
            elif (direction == "L"): x -= distance

        total_distance_to_point += distance_traversed

    print(total_distance_to_point)
    distances_to_intersections.append(total_distance_to_point)

print("part 2", min(distances_to_intersections))
