import sys

lines_in = [line.strip() for line in sys.stdin]
digits = ['2', '1', '0', '-', '=']

def from_snafu(n):
    tot = 0
    for d in range(len(n)):
        digit = 2 - digits.index(n[d])
        power = len(n) - d - 1
        tot += (digit * pow(5, power))
    return tot

def to_snafu(n):
    guess = []
    while from_snafu(''.join(guess)) < n: guess.append('2')
    for digit in range(len(guess)):
        while from_snafu(guess) > n:
            c = digits.index(guess[digit])
            if c < 4: guess[digit] = digits[c + 1]
            else: break
        if from_snafu(guess) < n:
            c = digits.index(guess[digit])
            guess[digit] = digits[c - 1]
    return ''.join(guess)

print('part 1: ', to_snafu(sum([from_snafu(n) for n in lines_in])))
