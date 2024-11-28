const knotHash = require('../day10');
const input = 'hfdlxzhv', inputs = [];

let i = -1;

while (++i < 128) {
  inputs.push(`${input}-${i}`);
}

let grid = inputs
  .map(knotHash)
  .map(hashToBinary);

let usedSquares = grid
  .join('')
  .split('')
  .filter(d => d === '1')
  .length;


console.log(`${usedSquares} used squares in the grid.`);

function hashToBinary(hash) {
  let binaryValues = [];
  let substr = 0;

  while (substr < hash.length) {
    let digit = hash.substr(substr, 1);
    binaryValues.push(
      ("00000000" + (parseInt(digit, 16))
        .toString(2))
        .substr(-4)
    );

    substr++;
  }

  return binaryValues.join('');
}

let grid2D = grid.map(row => row.split(''));

class Store {
  constructor() {
    this.store = []
  }

  registerCoord(x, y) {
    if (!this.hasCoord(x, y)) {
      this.store.push(`${x},${y}`);
    }
  }

  hasCoord(x, y) {
    return this.store.includes(`${x},${y}`);
  }
}

function scan(grid) {
  let store = new Store();
  let regions = 0;

  for (let row = 0; row < 128; row++) {
    for (let col = 0; col < 128; col++) {
      if (grid[row][col] === '0') continue;
      if (!store.hasCoord(row, col)) regions++;
      mapRegion(grid, store, row, col);
    }
  }

  return regions;
}

function mapRegion(grid, store, x, y) {
  if (grid[x][y] === '0') return;
  if (store.hasCoord(x, y)) return;

  store.registerCoord(x, y);

  if (x - 1 >= 0) mapRegion(grid, store, x - 1, y);
  if (x + 1 < 128) mapRegion(grid, store, x + 1, y);
  if (y - 1 >= 0) mapRegion(grid, store, x, y - 1);
  if (y + 1 < 128) mapRegion(grid, store, x, y + 1);
}

console.log(`${scan(grid2D)} used regions in the grid.`);