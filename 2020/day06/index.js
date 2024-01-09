const fs = require('fs');
const path = require('path');

(async () => {
  const input = await new Promise((res) => {
    fs.readFile(path.join(__dirname, './in.txt'), (err, data) => res(data.toString()))
  });

  const q = input.split('\n\n');
  const total = q
    .map(dedupe)
    .map((q) => q.length)
    .reduce((a, b) => a + b);

  console.log('pt1', total);

  const total2 = q
    .map(parsePt2)
    .reduce((a, b) => a + b);

  console.log('pt2', total2);
})();

function dedupe(q) {
  return [...new Set(q.split('\n').join('').split(''))];
}

function parsePt2(q) {
  const people = q.split('\n').sort((a, b) => a.length - b.length);
  let hasAll = 0;
  for (let i = 0, ii = people[0].length; i < ii; i++) {
    const qn = people[0][i];
    if (people.filter((qs) => qs.includes(qn)).length === people.length) {
      hasAll++;
    }
  }

  return hasAll;
}
