/*
BBFBBBFLRR
BBFBFBFLLL
FFBBBFBLLL
BFBFBFBRLR
BFFFFFFLRR
FBBFFBFRRL
BFBBBBBLLL
FBBBBFBRRL
*/

const fs = require('fs');
const path = require('path');

(async () => {
  const input = await new Promise((res) => {
    fs.readFile(path.join(__dirname, './in.txt'), (err, data) => res(data.toString()))
  });

  const tickets = input.split('\n');
  const rowAndColumn = tickets.map(parseRow);
  const id = rowAndColumn.map(([row, column]) => (row * 8 + column));
  const maxId = Math.max.apply(null, id);
  const minId = Math.min.apply(null, id);

  for (let i = minId; i <= maxId; i++) {
    if (!id.includes(i)) {
      console.log(i);
      break;
    }
  }
})();

function parseRow(row) {
  return [row.slice(0, 7), row.slice(-3)]
    .map((str) => {
      const bin = str
        .replace(/F/g, '0')
        .replace(/B/g, '1')
        .replace(/R/g, '1')
        .replace(/L/g, '0');

      return parseInt(bin, 2);
    });
}
