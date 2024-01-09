const fs = require('fs');
const crypto = require('crypto');

let input = fs.readFileSync('./day18/input.txt', 'utf8');
input = input.split('\n').map(line => line.split(''));

let part = 2;

class Square {
  constructor(value, x, y, grid) {
    this.value = value;
    this.x = x;
    this.y = y;
    this.grid = grid;
  }

  scan() {
    const { grid,x, y } = this;

    let adjacents = [
      grid.getSquare(x-1, y-1),
      grid.getSquare(x-1, y),
      grid.getSquare(x-1, y+1),
      grid.getSquare(x, y-1),
      grid.getSquare(x, y+1),
      grid.getSquare(x+1, y-1),
      grid.getSquare(x+1, y),
      grid.getSquare(x+1, y+1)
    ];

    let numTree = adjacents.filter(a => a === '|').length;
    let numLumb = adjacents.filter(a => a === '#').length;

    if (this.value === '.' && numTree >= 3) {
      this.nextValue = '|';
    }

    if (this.value === '|' && numLumb >= 3) {
      this.nextValue = '#';
    }

    if (this.value === '#') {
      if (numLumb >= 1 && numTree >= 1) {
        this.nextValue = '#';
      } else {
        this.nextValue = '.';
      }
    }

    if (!this.nextValue) {
      this.nextValue = this.value;
    }
  }
  
  convert() {
    this.value = this.nextValue;
    this.nextValue = undefined;
  }

  getValue() {
    return this.value;
  }
}

class Grid {
  constructor() {
    this.getSquare = this.getSquare.bind(this);

    this.value = [];

    for (let x = 0; x < input[0].length; x++) {
      this.value.push([]);

      for (let y = 0; y < input.length; y++) {
        this.value[x].push(new Square(input[x][y], x, y, this));
      }
    }
  }
  
  getSquare(x, y) {
    try {
      return this.value[x][y].getValue();
    } catch(e) {
      return;
    }
  }

  update() {
    this.value.forEach(row => {
      row.forEach(square => {
        square.scan();
      });
    });

    this.value.forEach(row => {
      row.forEach(square => {
        square.convert();
      });
    });
  }

  getResourceValue() {
    let numLumb = 0;
    let numTree = 0;

    this.value.forEach(row => {
      row.forEach(square => {
        if (square.getValue() === '#') {
          numLumb++;
        } else if (square.getValue() === '|') {
          numTree++;
        }
      });
    });

    return numLumb * numTree;
  }

  toString() {
    let string = '';
    this.value.forEach(row => {
      string += row.map(sq => sq.getValue()).join('');
    });
    // console.log(string);

    return string;
  }

  getChecksum() {
    let string = this.toString();
    return crypto.createHash('md5').update(string).digest('hex');
  }

  print() {
    console.log('');
    console.log('============================================================');
    this.value.forEach(line => {
      console.log(line.map(square => square.getValue()).join(''));
    });
  }
}

let grid = new Grid();

// combination at minute 605 is a repeat of minute 577, the pattern repeats every 28 minutes from here on out
let numMinutes = part === 1 ? 10 : 1000000000, numMinutesElapsed = 0;
// let combinationsSeen = [];

while (numMinutesElapsed++ < numMinutes) {
  grid.update();
  // grid.print();
  // let checksum = grid.getChecksum();
  
  /* if (combinationsSeen.includes(checksum)) {
    let before = combinationsSeen.indexOf(checksum);
    console.log('num minutes', numMinutesElapsed, 'seen already at', before);
    // grid.print();
  } */

  if (part === 2 && numMinutesElapsed === 577) {
    while (numMinutesElapsed <= numMinutes - 28) {
      numMinutesElapsed += 28;
    }
  }

  // combinationsSeen.push(checksum);
}

console.log(grid.getResourceValue());