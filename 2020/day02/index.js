/*
1-5 j: jjjnjjjjj
9-10 g: ggggggxggg
7-9 r: rrrvrrbrdr
9-18 j: jjjjjjjjnjjjjjjjjfjj
14-18 q: kjtxqqqqltlpgqshdx
*/

const fs = require('fs');
const path = require('path');

(async () => {
    const input = await new Promise((res) => {
        fs.readFile(path.join(__dirname, './in.txt'), (err, data) => res(data.toString()))
    });
    const entries = input.split('\n');
    console.log(
        entries
            .map(isValidPw2)
            .filter((n) => !!n)
            .length
    );
})();

function isValidPw(line) {
    console.log
    const [rule, pw] = line.split(': ');
    const [limit, letter] = rule.split(' ');
    let [lower, upper] = limit.split('-');
    lower = parseInt(lower, 10);
    upper = parseInt(upper, 10);

    numOfLetter = pw.split('').filter((l) => l === letter).length;

    return numOfLetter >= lower && numOfLetter <= upper;
}

function isValidPw2(line) {
    const [rule, pw] = line.split(': ');
    const [limit, letter] = rule.split(' ');
    let [first, second] = limit.split('-');
    first = parseInt(first, 10);
    second = parseInt(second, 10);

    let occurrences = 0;
    if (pw.charAt(first - 1) === letter) occurrences++;
    if (pw.charAt(second - 1) === letter) occurrences++;

    return occurrences === 1;
}