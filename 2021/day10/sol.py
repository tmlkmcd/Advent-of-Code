import sys
import math

puzzle_input = [l.strip() for l in sys.stdin]

pt2_scores = []

def finish(l):
    # part 2
    score = 0

    for c in l[::-1]:
        score *= 5
        if c == '(': score += 1
        elif c == '[': score += 2
        elif c == '{': score += 3
        elif c == '<': score += 4

    pt2_scores.append(score)

def scan(l):
    # part 1
    string = ''

    for c in l:
        if c == '[' or c == '(' or c == '{' or c == '<':
            string += c
        elif c == ']':
            if string[-1] == '[': string = string[:-1]
            else: return c
        elif c == ')':
            if string[-1] == '(': string = string[:-1]
            else: return c
        elif c == '}':
            if string[-1] == '{': string = string[:-1]
            else: return c
        elif c == '>':
            if string[-1] == '<': string = string[:-1]
            else: return c

    finish(string)

    return True



pt1_score = 0

for l in puzzle_input:
    s = scan(l)
    if s == True: continue

    if s == ')': pt1_score += 3
    if s == ']': pt1_score += 57
    if s == '}': pt1_score += 1197
    if s == '>': pt1_score += 25137

print('part 1', pt1_score)
pt2_scores.sort()
print('part 2', pt2_scores[math.floor(len(pt2_scores)/2)])
