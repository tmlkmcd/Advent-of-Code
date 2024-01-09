'use strict';

const fs = require('fs');
const path = require('path');

class Packet {
  constructor() {
    this.path = fs.readFileSync(path.join(__dirname, './input.txt'), 'utf8')
      .split('\n')
      .map(line => line.split(''));

    this.x = 1;
    this.y = 0;
    this.direction = 'down';
    this.letters = [];
    this.steps = 0;
  }

  run() {
    while (true) {
      try {
        switch (this.direction) {
          case 'down': this.goDown(); break;
          case 'up': this.goUp(); break;
          case 'right': this.goRight(); break;
          case 'left': this.goLeft(); break;
        }

        this.steps++;

        if (this.path[this.y][this.x].match(/^\w$/)) {
          this.letters.push(this.path[this.y][this.x]);
        }

        if (this.path[this.y][this.x] === '+') this.direction = this.turn();
        if (this.path[this.y][this.x] === ' ') throw new Error('Reached end of path; aborting.');

      } catch (e) {
        console.log(this.letters.join(''));
        console.log(`Took ${this.steps} steps.`);
        break;
      }
    }
  }

  goUp() { this.y--; }
  goDown() { this.y++; }
  goRight() { this.x++; }
  goLeft() { this.x--; }

  turn() {
    let {direction: currentDirection} = this;
    let possibleNextCoords = [
      {
        direction: 'up',
        coords: [this.y - 1, this.x]
      },
      {
        direction: 'down',
        coords: [this.y + 1, this.x]
      },
      {
        direction: 'right',
        coords: [this.y, this.x + 1]
      },
      {
        direction: 'left',
        coords: [this.y, this.x - 1]
      }
    ];

    let opposite = {
      up: 'down',
      down: 'up',
      left: 'right',
      right: 'left'
    };

    return possibleNextCoords.find(coords => {
      let {direction, coords: [y, x]} = coords;
      return !!this.path[y][x] && this.path[y][x] !== ' ' && direction !== opposite[currentDirection];
    }).direction;
  }
}

let packet = new Packet();
packet.run();