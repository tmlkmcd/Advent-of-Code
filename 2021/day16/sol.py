import sys
from math import prod

in_16 = ''
for line in sys.stdin: in_16 = line.strip()

bitmap = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

decoded = ''
for c in in_16: decoded += bitmap[c]

pt1_tot_version = 0

def parse_packet(num):
    global pt1_tot_version
    version = int(num[0:3], 2)

    pt1_tot_version += version

    p_type = int(num[3:6], 2)
    if p_type == 4: return parse_literal(num)
    return parse_operator(num, p_type)

def parse_literal(num):
    read_idx = 6
    num_decoded = ''

    while True:
        num_bin = num[read_idx:read_idx + 5]
        prefix = num_bin[0]
        num_decoded += num_bin[1:]

        read_idx += 5
        if prefix != '1': break

    return int(num_decoded, 2), read_idx

def parse_operator(num, p_type):
    length_type = num[6]
    sub_packets = []
    consumed = 0
    end = 0
    value = -1

    if length_type == '0':
        sub_p_length_bin = num[7:22]
        sub_p_length = int(sub_p_length_bin, 2)
        sub_p_end = 22 + sub_p_length

        while consumed < sub_p_length:
            packet, n_consumed = parse_packet(num[22 + consumed:])
            sub_packets.append(packet)
            consumed += n_consumed
        end = sub_p_end

    elif length_type == '1':
        sub_p_amt_bin = num[7:18]
        sub_p_amt = int(sub_p_amt_bin, 2)

        parsed = 0
        while parsed < sub_p_amt:
            packet, n_consumed = parse_packet(num[18 + consumed:])
            sub_packets.append(packet)
            consumed += n_consumed
            parsed += 1
        end = 18 + consumed

    if p_type == 0: value = sum(sub_packets)
    elif p_type == 1: value = prod(sub_packets)
    elif p_type == 2: value = min(sub_packets)
    elif p_type == 3: value = max(sub_packets)
    elif p_type == 5: value = 1 if sub_packets[0] > sub_packets[1] else 0
    elif p_type == 6: value = 1 if sub_packets[0] < sub_packets[1] else 0
    elif p_type == 7: value = 1 if sub_packets[0] == sub_packets[1] else 0


    if value == -1: raise Exception('dammit')
    return value, end




pt2_val, _ = parse_packet(decoded)
print('part 1', pt1_tot_version)
print('part 2', pt2_val)
