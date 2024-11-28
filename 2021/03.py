import sys

lines_in = []

for line in sys.stdin:
    lines_in.append(line.strip())

def get_frequencies(lines, pt2_mode='o2'):
    num_lines = 0
    freq = []

    for l in lines:
        num_lines += 1

        for i in range(len(l)):
            try: freq[i]
            except: freq.append(0)
            if l[i] == '1': freq[i] = freq[i] + 1

    most = []
    least = []

    for bit in freq:
        if bit < (num_lines / 2):
            most.append('0')
            least.append('1')
        elif bit > (num_lines / 2):
            most.append('1')
            least.append('0')
        else:
            if pt2_mode == 'o2':
                most.append('1')
                least.append('0')
            if pt2_mode == 'co2':
                most.append('0')
                least.append('1')

    return (most, least)

most, least = get_frequencies(lines_in)

b = int('0b' + ''.join(most), 2)
c = int('0b' + ''.join(least), 2)
print('part 1', b * c)

# part 2

pt2_lines_o = lines_in
pt2_lines_co2 = lines_in
checking_index = 0

while len(pt2_lines_o) > 1:
    most, _ = get_frequencies(pt2_lines_o)
    temp_lines = []
    for l in pt2_lines_o:
        if l[checking_index] == most[checking_index]:
            temp_lines.append(l)

    pt2_lines_o = temp_lines
    checking_index += 1

checking_index = 0
while len(pt2_lines_co2) > 1:
    _, least = get_frequencies(pt2_lines_co2)
    temp_lines = []
    for l in pt2_lines_co2:
        if l[checking_index] == least[checking_index]:
            temp_lines.append(l)

    pt2_lines_co2 = temp_lines
    checking_index += 1

d = int('0b' + ''.join(pt2_lines_o[0]), 2)
e = int('0b' + ''.join(pt2_lines_co2[0]), 2)

print('part 2', d * e)
