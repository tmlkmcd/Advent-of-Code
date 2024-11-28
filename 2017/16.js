'use strict';
const fs = require('fs');
const path = require('path');

let input = fs.readFileSync(path.join(__dirname, './input.txt'), 'utf8');

let part = 2;

let instructions = input.split(',').map(cmd => {
  let move = cmd.substr(0, 1);
  let targets = cmd.substr(1, cmd.length - 1).split('/');
  if (move === 'x') {
    targets = targets.map(num => parseInt(num, 10));
  }

  if (move === 's') {
    targets = parseInt(targets[0], 10);
  }

  return {move, targets}
});

function dance() {
  instructions.forEach(danceStep);
  return programs;
}

function danceStep(instruction) {
  let {move, targets} = instruction;
  switch (move) {
    case 's': return spin(targets);
    case 'x': return exchange(targets);
    case 'p': return partner(targets);
  }
}

function spin(length) {
  let stopPoint = l - length;
  programs = programs.substr(stopPoint, l) + programs.substr(0, stopPoint);
}

function exchange([p1, p2]) {
  let t1 = programs.charAt(p1);
  let t2 = programs.charAt(p2);

  partner([t1, t2]);
}

function partner([t1, t2]) {
  let start, rest;
  if (programs.indexOf(t2) > programs.indexOf(t1)) {
    start = programs.split(t1);
    rest = start[1].split(t2);

    programs = start[0] + t2 + rest[0] + t1 + rest[1];
    return;
  }

  start = programs.split(t2);
  rest = start[1].split(t1);

  programs = start[0] + t1 + rest[0] + t2 + rest[1];
}

let programs = 'abcdefghijklmnop';
let l = programs.length;

if (part === 1) {
  console.log(`After one iteration: ${dance()}`);
} else {
  let combinations = [programs];
  let maxIterations = 100000, i = 0;
  let repeatCycle;

  while (i++ <= maxIterations) {
    let newCombination = dance();
    if (combinations.includes(newCombination)) {
      console.log(`Repeated cycle found after ${i} iterations.`);
      repeatCycle = i;
      break;
    }
  }

  programs = 'abcdefghijklmnop';
  let iterations = 1000000000 % repeatCycle, ii = 0;

  while (ii++ < iterations) {
    dance();
  }

  console.log(`After a billion iterations: ${programs}`);

}