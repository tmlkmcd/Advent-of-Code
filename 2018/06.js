const fs = require('fs');
const input = fs.readFileSync('./day06/input.txt', 'utf8')
  .split('\n')
  .map(coord => coord
    .split(', ')
    .map(a => parseInt(a, 10))
  );

let coordsString = input.map(c => c.join(','));

let ys = input.map(a => a[1]);
let xs = input.map(a => a[0]);

let maxY = Math.max.apply(null, ys);
let maxX = Math.max.apply(null, xs);

let minY = Math.min.apply(null, ys);
let minX = Math.min.apply(null, xs);

let grid = [];

for (let y = 0; y <= maxY; y++) {
  let row = [];
  for (let x = 0; x <= maxX; x++) {
    if (coordsString.includes(`${x},${y}`)) {
      row.push('-');
    } else {
      row.push('.');
    } 
  }
  grid.push(row);
}

let pt2SafeRegion = 0;
let pt2SafeThreshold = 10000;

grid.forEach((row, y) => {
  row.forEach((point, x) => {
    if (distanceFromAllPoints([x, y], input) < pt2SafeThreshold) {
      pt2SafeRegion++;
    }
    if (point === '-') return;

    let distances = input.map((pt, i) => ({
      i,
      distance: manhattanDistance(pt, [x, y])
    }));

    let lowestDistance = distances.reduce((a, b) => (a.distance < b.distance) ? a : b);

    if (distances.filter(a => a.distance === lowestDistance.distance).length > 1) {
      grid[y][x] = '.';
    } else {
      grid[y][x] = numToLetter(lowestDistance.i)
    }

  });
});

grid = trim(grid, minX, minY)
// visualize(grid); // can't be done effectively on real data
calculate(grid);
console.log('Part 2 ans:', pt2SafeRegion)

function visualize(grid) {
  grid.forEach(row => {
    console.log(row.join(''));
  });
}

function calculate(grid) {
  let scores = {};

  grid.forEach((row, i) => {
    row.forEach((item, j) => {
      if (item !== '!' && item !== '?') {
        if (i === 0 || i === grid.length - 1 || j === 0 || j === row.length - 1) {
          // infinite areas
          scores[item] = NaN;
        }
        if (!scores.hasOwnProperty(item)) {
          scores[item] = 2;
        } else if (!isNaN(scores[item])) {
          scores[item]++;
        }
      }
    })
  })

  let biggestAreaKey = Object.keys(scores).reduce((a, b) => {
    if (isNaN(scores[a])) return b;
    if (isNaN(scores[b])) return a;
    if (scores[a] > scores[b]) {
      return a;
    }
    return b;
  });

  console.log(scores[biggestAreaKey]);
}

function trim(grid, x, y) {
  let trimGrid = grid.map(row => row.slice(x, row.length))

  return trimGrid.slice(y, trimGrid.length);
}

function manhattanDistance(a, b) {
  return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
}

function numToLetter(num) {
  return String.fromCharCode(47 + num);
}

function distanceFromAllPoints(pt, coords) {
  let distance = 0;

  coords.forEach(coord => {
    distance += manhattanDistance(coord, pt);
  });

  return distance;
}