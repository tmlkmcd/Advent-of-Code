'use strict';

const fs = require('fs');
const path = require('path');

let input = fs.readFileSync(path.join(__dirname, './input.txt'), 'utf8');
let instructions = input.split('\n')
  .map(item => parseInt(item, 10));

let part = 2, stepsTaken = 0, pointer = 0;

while (pointer >= 0 || pointer <= instructions.length) {
  let jump = instructions[pointer];

  if (part === 2 && jump >= 3) instructions[pointer] = jump - 1;
  else instructions[pointer] = jump + 1;

  pointer += jump;
  stepsTaken++;
}

// last step is after leaving the limits; subtraction corrects for this
console.log(stepsTaken - 1);
