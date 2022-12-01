import sys

lines_in = [line.strip() for line in sys.stdin]

def get_card_value(c, part=1):
    if c == 'J': return 1 if part == 2 else 11
    return {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'Q': 12,
        'K': 13,
        'A': 14
    }[c]

hand_value = {
    '5oak': 70000000000,
    '4oak': 60000000000,
    'fh': 50000000000,
    '3oak': 40000000000,
    '2p': 30000000000,
    '1p': 20000000000,
    'hc': 10000000000
}

def get_hand_type(hand):
    s_hand = sorted(list(hand), key=lambda x: 15 - get_card_value(x))
    a, b, c, d, e = s_hand

    if a == e: return '5oak'
    if a == d or b == e: return '4oak'
    if (a == c and d == e) or (a == b and c == e): return 'fh'
    if a == c or c == e or b == d: return '3oak'
    if (a == b and c == d) or (b == c and d == e) or (a == b and d == e): return '2p'
    if a == b or b == c or c == d or d == e: return '1p'
    return 'hc'

def get_hand_type_2(hand):
    p1_hand = get_hand_type(hand)
    if 'J' not in hand: return p1_hand

    num_jokers = len([a for a in hand if a == 'J'])
    if num_jokers == 5 or p1_hand == 'fh' or p1_hand == '4oak': return '5oak'
    if p1_hand == '3oak': return '4oak'
    if p1_hand == '2p': return '4oak' if num_jokers == 2 else 'fh'
    if p1_hand == '1p': return '3oak'

    return '1p'

def parse_line(text, part=1):
    hand, bid = text.split(' ')
    bid = int(bid)
    value = hand_value[get_hand_type(hand) if part == 1 else get_hand_type_2(hand)]
    hc_sum = 0
    for c in list(hand):
        hc_sum *= 100
        hc_sum += get_card_value(c, part)

    return {
        'bid': bid,
        'value': value + hc_sum
    }


hands_1 = sorted([parse_line(line) for line in lines_in], key=lambda x: x['value'])
hands_2 = sorted([parse_line(line, 2) for line in lines_in], key=lambda x: x['value'])

total_bid, total_bid2 = 0, 0

for n, h in enumerate(hands_1):
    total_bid += (n + 1) * h['bid']

for n, h in enumerate(hands_2):
    total_bid2 += (n + 1) * h['bid']

print('part 1', total_bid)
print('part 2', total_bid2)
