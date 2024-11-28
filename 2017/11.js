'use strict';

const fs = require('fs');
const path = require('path');

function getInput() {
  let inputPath = path.join(__dirname, './input.txt');

  return new Promise(function (resolve, reject) {
    fs.readFile(inputPath, 'utf8', (err, data) => {
      if (err) reject(err);
      else resolve(data);
    });
  });
}

class Mover {
  constructor(directions) {
    this.i = 0;
    this.j = 0;
    this.k = 0;

    this.directions = directions;
    this.walk = this.walk.bind(this);
    this.consolidate = this.consolidate.bind(this);
    this.reportFinal = this.reportFinal.bind(this);
    this.reportMax = this.reportMax.bind(this);

    this.distances = [];
  }

  n() { this.i++; }
  ne() { this.j++; }
  se() { this.k++; }
  s() { this.i--; }
  sw() { this.j--; }
  nw() { this.k--; }

  walk() {
    let {directions} = this;

    directions.forEach(movement => {
      this[movement]();
      this.consolidate();
    });
    return this;
  }

  consolidate() {
    this.i = this.i - this.k;
    this.j = this.j + this.k;

    this.distances.push(Math.abs(this.i + this.j));
    return this;
  }

  reportFinal() {
    console.log(`Final distance: ${this.distances[this.distances.length - 1]}`);
    return this;
  }

  reportMax() {
    console.log(`Max distance: ${Math.max.apply(null, this.distances)}`);
    return this;
  }
}

getInput()
  .then(input => {
    let mover = new Mover(input.split(','));
    return mover;
  })
  .then(mover => {
    mover.walk()
      .reportFinal()
      .reportMax();
  });
