import sys
from itertools import chain

digits = []

for line in sys.stdin:
    for digit in line:
        digits.append(int(digit))

width = 25 
height = 6
num_digits = len(digits)
digits_processed = 0

layers = []

while digits_processed < len(digits):
    layers.append([])
    for x in range(height):
        layers[len(layers) - 1].append([])
        for _ in range(width):
            layers[len(layers) - 1][x].append(digits[digits_processed])
            digits_processed += 1

current_lowest = [-1, 99999, 0, 0]

for n, l in enumerate(layers):
    layer = list(chain.from_iterable(l))
    if (layer.count(0) <= current_lowest[1]):
        current_lowest = [n, layer.count(0), layer.count(1), layer.count(2)]

print("part 1 ans:", current_lowest[2] * current_lowest[3])

new_image = []

for x, row in enumerate(layers[0]):
    new_image.append([])
    for y, pixel in enumerate(row):
        try:
            for z in range(len(layers)):
                if (layers[z][x][y] != 2):
                    new_image[x].append(layers[z][x][y])
                    raise Exception(':)')
        except:
            # yuck, but i don't know a better way to do this in python. javascript this would be easy
            pass

print("part 2 ans:")
for row in new_image:
    printable = ["#" if x == 1 else "-" for x in row]
    print("".join(printable))