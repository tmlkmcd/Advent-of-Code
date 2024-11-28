const testInput = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2";

const fs = require('fs');

const input = fs.readFileSync('./day08/input.txt', 'utf8');

let points = input.split(' ').map(a => parseInt(a, 10));
let cumulative = {
  amt: 0
}

scanNode = scanNode.bind(null, cumulative);
console.log('part 2 ans:', scanNode(points));
console.log('part 1 ans:', cumulative.amt);

function scanNode(cumulative, points) {
  if (!points.length) return;
  let children = points.shift();
  let metadata = points.shift();
  let childValues = [], value = 0;
  let metadatas = [];

  for (let i = 0; i < children; i++) {
    childValues.push(
      scanNode(points)
    );
  }

  for (let j = 0; j < metadata; j++) {
    let md = points.shift();
    cumulative.amt += md;
    metadatas.push(md);
  }

  if (children === 0) {
    value = metadatas.length === 1 ? metadatas[0] : metadatas.reduce((a, b) => a+b);
  } else {
    metadatas.forEach(k => {
      if (!!childValues[k-1]) {
        value += childValues[k-1];
      }
    })
  }

  return value;
}