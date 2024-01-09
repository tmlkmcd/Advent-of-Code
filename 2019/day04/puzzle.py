input = "153517-630395"
use_this_input = "155554-630395" # fudge for the first number; manually found the first valid number
# the system that finds the next valid number is fast but will not work for the given input because the last digit is higher than the rest

input_range = [int(x) for x in use_this_input.split("-")]

part = 1

def has_adjacent(digits):
    if (part == 1):
        return any(digits[i] == digits[i + 1] for i in range(len(digits) - 1))

    if (part == 2):
        return any(digits[i] == digits[i + 1] and (i == 0 or digits[i] != digits[i - 1]) and (i == len(digits) - 2 or digits[i] != digits[i + 2]) for i in range(len(digits) - 1))

def next_num(num):
    digits = [int(d) for d in str(num + 1)]
    for i, n in enumerate(digits):
        if i == 0:
            continue
        if (n < digits[i-1]):
            digits[i] = digits[i-1]
    new_num = int("".join([str(i) for i in digits]))

    if (not has_adjacent(digits)):
        return next_num(new_num)
    
    return new_num

i = input_range[0]
num_valid = 0
while True:
    i = next_num(i)
    if i > input_range[1]:
        break
    # print(i)
    num_valid += 1

print(num_valid, "valid numbers")