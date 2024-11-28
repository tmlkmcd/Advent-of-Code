import sys
from math import pow

lines_in = [line.strip() for line in sys.stdin]

match_map = {}
num_cards = {}


def numbers(num_list):
    return [int(a) for a in filter(lambda x: x != '', num_list.split(' '))]


def check_card(card):
    global match_map, num_cards

    _, nums = card.split(': ')
    __, card_num = [s.strip() for s in _.split('Card')]
    num_cards[int(card_num)] = 1
    win, has = nums.split(' | ')
    win, has = numbers(win), numbers(has)
    win_map, has_win = {}, 0

    for w in win: win_map[w] = True
    for h in has:
        if h in win_map: has_win += 1

    match_map[int(card_num)] = has_win

    return 0 if has_win == 0 else int(pow(2, has_win - 1))


total, total2 = 0, 0
for line in lines_in: total += check_card(line)

for card_num in range(len(lines_in) + 1):
    if card_num == 0: continue

    m = match_map[card_num]
    for n in range(m):
        bump = card_num + n + 1
        if bump in match_map:
            num_cards[bump] += num_cards[card_num]

for x in num_cards:
    total2 += num_cards[x]

print('part 1', total)
print('part 2', total2)
