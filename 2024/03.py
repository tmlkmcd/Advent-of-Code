import re

with open("inputs/2024/03.txt", "r") as f:
    content = f.read()


def get_muls(in_string):
    tot = 0
    matches = re.findall(r"mul\(\d+,\d+\)", in_string)
    for match in matches:
        [a, b] = [int(x) for x in re.findall(r"\d+", match)]
        tot += a * b
    return tot


sections = content.split('don\'t()')
pt2 = get_muls(sections[0])
for section in sections[1:]:
    split_sections = section.split('do()')
    for b in split_sections[1:]:
        pt2 += get_muls(b)

print('part 1', get_muls(content))
print('part 2', pt2)
