const fs = require('fs');
const path = require('path');

let part = 2;

getTableChecksum()
  .then(console.log);

function getTableChecksum() {
  return getInput()
    .then(parseRows)
    .then(getChecksums)
    .then(reduce)
    .catch(err => {
      console.log(':\'(');
      console.error(err);
    });
}

function getInput() {
  let inputPath = path.join(__dirname, './input.txt');

  return new Promise(function(resolve, reject) {
    fs.readFile(inputPath, 'utf8', (err, data) => {
      if (err) reject(err);
      else resolve(data);
    });
  });
}

function parseRows(input) {
  let rows = input.split('\n');
  return rows
    .map(
      row => row.split('\t').map(cell => parseInt(cell, 10))
    )
}

function getChecksums(rows) {
  let cb = (part === 1) ? getChecksum1 : getChecksum2;
  return rows.map(cb);
}

function getChecksum1(row) {
  let max = Math.max.apply(undefined, row);
  let min = Math.min.apply(undefined, row);

  return max - min;
}

function getChecksum2(row) {
  for (let i = 0, ii = row.length; i < ii; i++) {
    for (let j = i + 1; j < ii; j++) {
      if (isDivisible(row[i], row[j])) {
        return (row[i] > row[j])
          ? row[i]/row[j]
          : row[j]/row[i];
      }
    }
  }
}

function isDivisible(a, b) {
  return (a%b === 0 || b%a === 0);
}

function reduce(checksums) {
  return checksums.reduce((a, b) => {
    return a + b;
  });
}