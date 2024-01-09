'use strict';
const fs = require('fs');
const path = require('path');

let part = 2;

let [genA, genB] = fs.readFileSync(path.join(__dirname, './input.txt'), 'utf8')
  .split('\n')
  .map(line => line.split(' ').slice(-1)[0])
  .map(number => parseInt(number, 10));

let factorA = 16807, factorB = 48271;
let divide = 2147483647;
let count = 0;
let iterations = (part === 1) ? 4 * Math.pow(10, 7) : 5 * Math.pow(10, 6);

function iteration() {
  genA = (genA * factorA) % divide;
  genB = (genB * factorB) % divide;
  if (getBin(genA) === getBin(genB)) count++;
}

function getBin(number) {
  let binary = number.toString(2);

  while (binary.length < 16) {
    binary = "0" + binary;
  }

  return binary.substr(-16);
}

if (part === 1) {
  // THIS TAKES A WHILE!!
  while (--iterations > 0) {
    iteration();
  }
}

function iteration2() {
  do {
    genA = (genA * factorA) % divide;
  } while (genA % 4 !== 0);

  do {
    genB = (genB * factorB) % divide;
  } while (genB % 8 !== 0);

  if (getBin(genA) === getBin(genB)) count++;
}

if (part === 2) {
  while (--iterations > 0) {
    iteration2();
  }
}

console.log(`Part ${part}: ${count} iterations that have the same last 16 binary digits.`);