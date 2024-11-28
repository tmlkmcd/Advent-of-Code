import math

puzzle_input = "59796737047664322543488505082147966997246465580805791578417462788780740484409625674676660947541571448910007002821454068945653911486140823168233915285229075374000888029977800341663586046622003620770361738270014246730936046471831804308263177331723460787712423587453725840042234550299991238029307205348958992794024402253747340630378944672300874691478631846617861255015770298699407254311889484508545861264449878984624330324228278057377313029802505376260196904213746281830214352337622013473019245081834854781277565706545720492282616488950731291974328672252657631353765496979142830459889682475397686651923318015627694176893643969864689257620026916615305397"

# test inputs
# puzzle_input = "12345678"
# puzzle_input = "80871224585914546619083218645595"
# puzzle_input = "19617804207202209144916044189917"
# puzzle_input = "69317163492948606335995924319873"
# puzzle_input = "03036732577212944063491565474664"
part = 2

l = []

for d in puzzle_input:
    l.append(int(d))

def get_ones_digit(n):
    return abs(n) % 10

def multiply_by_pattern(puzzle_input, pattern):
    return get_ones_digit(sum([n * pattern[i] for i, n in enumerate(puzzle_input)]))

base_pattern = [0, 1, 0, -1]

patterns = []

def phase(my_input):
    output = []
    for i, n in enumerate(my_input):
        pattern = []
        if len(patterns) - 1 >= i: pattern = patterns[i]
        else:
            for _ in range(len(my_input) + 1):
                ii = i + 1
                if _ == 0: ii -= 1
                if len(pattern) >= len(my_input): break
                for __ in range(ii):
                    pattern.append(base_pattern[_ % 4])
                    if len(pattern) >= len(my_input): break
            patterns.append(pattern)
        new_num = multiply_by_pattern(my_input, pattern)
        output.append(new_num)
    return output

if part == 1:
    for _ in range(100):
        l = phase(l)
    print("".join([str(n) for n in l])[0:8])
    exit()

def phase_2_old(inp):
    # this method is much faster, but fully simulating part 2 is still entirely impractical without the mother of all supercomputers
    output = []
    for n in range(len(inp)):
        total = 0
        wavelength = n + 1
        scan_index = wavelength
        total += sum(inp[wavelength - 1:scan_index + n])
        scan_index += (2 * wavelength) - 1
        while scan_index < len(inp):
            total -= sum(inp[scan_index:(scan_index + wavelength)])
            scan_index += (2 * wavelength)
            total += sum(inp[scan_index:(scan_index + wavelength)])
            scan_index += (2 * wavelength)

        
        output.append(get_ones_digit(total))
    return output

digits_to_skip = int(puzzle_input[0:7])
total_digits = len(puzzle_input) * 10000
answer_starting_digit_from_end = total_digits - digits_to_skip

l = puzzle_input
ll = l
while len(ll) <= answer_starting_digit_from_end:
    ll = ll + l

while len(ll) > answer_starting_digit_from_end:
    ll = ll[1:]

def phase_2(i):
    p = 0
    n = []
    for _, m in reversed(list(enumerate(i))):
        nn = (p + m) % 10
        n.append(nn)
        p = nn
    return list(reversed(n))

l_i = [int(x) for x in ll]

x = l_i
for _ in range(100):
    x = phase_2(x)

print("".join([str(n) for n in x[:8]]))