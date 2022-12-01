import sys

lines_in = [line.strip() for line in sys.stdin]

elves = [0]
index = 0

for cals in lines_in:
    if cals == "":
        index += 1
        elves.append(0)
    else:
        cal = int(cals)
        elves[index] += cal

elves.sort(reverse=True)
print('part 1', elves[0])
print('part 2', sum(elves[:3]))
