import sys

pt1_unique = 0

pt2_tot = 0

def get_number(chars, known):
    if len(chars) == 2:
        return '1'
    if len(chars) == 3: return '7'
    if len(chars) == 4: return '4'
    if len(chars) == 7: return '8'

for line in sys.stdin:
    l = line.strip()
    first, second = l.split(' | ')

    for x in second.split(' '):
        y = len(x)
        if y == 2 or y == 3 or y == 4 or y == 7:
            pt1_unique += 1

    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []
    zero = []


    b = ''

    def get_number(n):
        if len(n) == 2: return '1'
        if len(n) == 3: return '7'
        if len(n) == 4: return '4'
        if len(n) == 7: return '8'

        if len(n) == 5:
            is_two = True
            is_three = True
            is_five = True

            for char in n:
                if char not in two: is_two = False
                if char not in three: is_three = False
                if char not in five: is_five = False

            if is_two: return '2'
            if is_three: return '3'
            if is_five: return '5'

            raise Exception('bugger')

        if len(n) == 6:
            is_six = True
            is_zero = True

            for char in n:
                if char not in six: is_six = False
                if char not in zero: is_zero = False

            if is_six: return '6'
            if is_zero: return '0'

        return '9'


    nums = first.split(' ')
    iterations = 0

    while True:
        for n in nums:
            if len(n) == 2: one = [char for char in n]
            if len(n) == 3: seven = [char for char in n]
            if len(n) == 4: four = [char for char in n]
            if len(n) == 7: eight = [char for char in n]

            if len(one) > 0 and len(n) == 6:
                if not (one[0] in n and one[1] in n): six = [char for char in n]
                elif len(three) > 0:
                    for char in three:
                        if char not in n: zero = [char for char in n]

            if len(one) > 0 and len(n) == 5:
                if one[0] in n and one[1] in n: three = [char for char in n]
                elif len(b) == 1:
                    if b in n: five = [char for char in n]
                    else: two = [char for char in n]

            if len(four) > 0 and len(three) > 0:
                for char in four:
                    if char not in three:
                        b = char

        iterations += 1

        if iterations > 30:
            break
#             raise Exception('damn')

    number = ''
    for nn in second.split(' '):
        number += get_number(nn)

    pt2_tot += int(number)

print('part 1', pt1_unique)
print('part 2', pt2_tot)
