import re
import math

with open("inputs/2024/05.txt", "r") as f:
    content = f.read().split('\n\n')

[orders, pages] = map(lambda x: x.split('\n'), content)

orders = [[int(x) for x in re.findall(r"\d+", order)] for order in orders]
pages = [[int(x) for x in re.findall(r"\d+", page)] for page in pages]
pt1, pt2, good_pages, bad_pages = 0, 0, [], []


def scan(_pages, pages_index, current_index=0):
    global orders, pages

    if len(_pages) < 2:
        return True

    check = _pages[0]
    relevant_order = [order[0] for order in orders if order[1] == check]

    for (i, page) in enumerate(_pages[1:]):
        if page in relevant_order:
            correct(pages[pages_index], pages_index, [current_index, current_index + i + 1])
            return False

    return scan(_pages[1:], pages_index, current_index + 1)


def correct(_pages, pages_index, bad_index):
    [a, b] = bad_index
    removed = _pages[b]
    del _pages[b]
    _pages.insert(a, removed)

    if scan(_pages, pages_index):
        bad_pages.append(_pages)


for (n, page) in enumerate(pages):
    if scan(page, n):
        good_pages.append(page)

for p in good_pages:
    pt1 += p[math.floor(len(p) / 2)]

for p2 in bad_pages:
    pt2 += p2[math.floor(len(p2) / 2)]

print('part 1', pt1)
print('part 2', pt2)
