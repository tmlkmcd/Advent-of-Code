const fs = require('fs');
const path = require('path');

const part = 2;

(async () => {
    const input = await new Promise((res) => {
        fs.readFile(path.join(__dirname, './in.txt'), (err, data) => res(data.toString()))
    });
    const lines = input.split('\n')
        .map((n) => parseInt(n, 10));

    if (part === 1) {
        for (let i = 25, ii = lines.length; i < ii; i++) { 
            if (!hasSum(lines.slice(i - 25, i + 1))) {
                console.log('FOUND IT', lines[i]);
                break;
            }
        }
        return;
    }

    const pt1Ans = 105950735;

    let sum = 0;
    let start = 0, end = 0;

    while (sum !== pt1Ans) {
        if (sum < pt1Ans) {
            sum += (lines[++end]);
        } else {
            sum -= (lines[++start]);
        }
    }

    const set = lines.slice(++start, end)
    const min = Math.min.apply(null, set);
    const max = Math.max.apply(null, set);

    console.log('pt 2', min + max);
})();

function hasSum(set) {
    const target = set.pop();
    for (let i = 0, ii = set.length; i < ii; i++) {
        const needed = target - set[i];
        if (set.includes(needed) && set.indexOf(needed) !== i) {
            return true;
        }
    }

    return false;
}
