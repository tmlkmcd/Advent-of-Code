const fs = require('fs');
const path = require('path');

(async () => {
    const input = await new Promise((res) => {
        fs.readFile(path.join(__dirname, './in.txt'), (err, data) => res(data.toString()))
    });

    const jolts = input.split('\n')
        .map((j) => parseInt(j, 10));

    const allJolts = [0, ...jolts, Math.max.apply(null, jolts) + 3];
    allJolts.sort((a, b) => a - b);
    
    let ones = 0;
    let threes = 0;

    allJolts.forEach((j, i) => {
        if (j === allJolts[i - 1] + 1) ones++;
        if (j === allJolts[i - 1] + 3) threes++;
    });

    console.log(ones * threes);

    // part 2

    const segments = [];
    let segment = [];

    allJolts.forEach((j, i) => {
        segment.push(j);

        if (allJolts[i + 1] === (j + 3)) {
            segments.push(segment);
            segment = [];
        }
    });

    const totalCombos = segments.map(combosForSegment)
        .reduce((a, b) => a * b);

    console.log(totalCombos);
})();

function combosForSegment(segment) {
    // all segments are consecutive numbers in groups of 5 maximum - there are no gaps of 2
    if (segment.length === 1 || segment.length === 2) {
        return 1;
    }
    
    if (segment.length === 3) {
        return 2;
    }

    if (segment.length === 4) {
        return 4;
    }

    if (segment.length === 5) {
        return 7;
    }
}