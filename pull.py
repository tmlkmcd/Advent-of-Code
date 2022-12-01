#!/usr/bin/env python3

import sys
import os
import requests
from datetime import datetime

year = '2023'
date = -1

for arg in sys.argv:
    if not arg.startswith('date='):
        continue
    date = arg.split('date=')[1]

if date == -1:
    date = datetime.now().strftime('%d')

dir_name = f'{year}/{date if len(date) == 2 else f"0{date}"}'

if not os.path.exists(dir_name):
    os.makedirs(dir_name)

content = '\n'.join([
    'import sys',
    'import math',
    'import collections',
    'import itertools',
    '',
    'lines_in = [line.strip() for line in sys.stdin]',
    ''
])

with open(f'{dir_name}/solution.py', 'w') as f:
    f.write(content)

with open(f'{dir_name}/in.txt', 'a') as ff:
    uri = f'https://adventofcode.com/{year}/day/{date[1] if date[0] == "0" else date}/input'
    puzzle_input = requests.get(
        uri,
        cookies={'session': open('cookie.txt', 'r').read()},
        headers={
            'User-Agent': 'https://github.com/tmlkmcd/AoC-2022/blob/main/pull.py by rejectmusician@hotmail.co.uk pls lmk if this is no good'
        }
    ).text

    if "log in" in puzzle_input:
        print("User session expired, remember to re-set your token")
    else:
        ff.write(puzzle_input)
