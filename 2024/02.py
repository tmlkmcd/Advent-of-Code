f = open("inputs/2024/02.txt", "r")

lines_in = [line.strip() for line in f]

reports = [[int(x) for x in a.split(' ')] for a in lines_in]
safe, safe_2 = 0, 0


def is_safe(this_report):
    current = this_report[0]
    asc = this_report[1] - this_report[0] > 0
    this_report_is_safe = True

    for level in this_report[1:]:
        if asc and not 1 <= (level - current) <= 3:
            this_report_is_safe = False
            break
        elif not asc and not -1 >= (level - current) >= -3:
            this_report_is_safe = False
            break
        current = level
    return this_report_is_safe


for report in reports:
    if is_safe(report):
        safe += 1
        safe_2 += 1
    else:
        for n in range(len(report)):
            if is_safe(report[:n] + report[n + 1:]):
                safe_2 += 1
                break

print('part 1', safe)
print('part 2', safe_2)
