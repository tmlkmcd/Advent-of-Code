'use strict';

const fs = require('fs');
const path = require('path');

const register = {};
const registerOfHighest = {};

getInput('input.txt')
  .then(parseInput)
  .then(runActions)
  .then(reduce)
  .then(console.log);

function getInput(input) {
  let inputPath = path.join(__dirname, './', input);

  return new Promise(function (resolve, reject) {
    fs.readFile(inputPath, 'utf8', (err, data) => {
      if (err) reject(err);
      else resolve(data);
    });
  });
}

function parseInput(input) {
  return input.split('\n').map(interpretLine);
}

function runActions(actions) {
  actions.forEach(({action, condition}) => {
    if (condition()) action();
  });
}

function reduce() {
  let highest, highestEver;

  for (let key in register) {
    if (!register.hasOwnProperty(key)) continue;

    if ((!highest && highest !== 0) || register[key] >= highest) {
      highest = register[key];
    }

    if ((!highestEver && highestEver !== 0) || registerOfHighest[key] >= highestEver) {
      highestEver = registerOfHighest[key];
    }
  }

  return {
    part1: highest,
    part2: highestEver
  };
}

function interpretLine(line) {
  let split = line.split(' if ');
  let action = interpretAction(split[0]), condition = interpretCondition(split[1]);

  return {action, condition}
}

function interpretAction(text) {
  let action = (text.includes('inc')) ? 'inc' : 'dec';
  let [register, magnitude] = text.split(` ${action} `);

  return doAction.bind(null, register, action, parseInt(magnitude, 10));
}

function interpretCondition(text) {
  let operators = ['>=', '>', '<=', '<', '==', '!='];
  let comparison = operators.find(operator => text.includes(` ${operator} `));

  if (!comparison) throw new Error(`Unknown operator: ${text}`);

  let split = text.split(` ${comparison} `);
  let key = split[0], magnitude = split[1];

  return checkCondition.bind(null, key, comparison, magnitude);
}

function doAction(key, action, magnitude) {
  if (!register.hasOwnProperty(key)) register[key] = 0;
  if (!registerOfHighest.hasOwnProperty(key)) registerOfHighest[key] = 0;

  let start = register[key], answer;

  if (action === 'inc') answer = start + magnitude;
  else answer = start - magnitude;

  register[key] = answer;

  if (answer > registerOfHighest[key]) {
    registerOfHighest[key] = answer;
  }
}

function checkCondition(key, comparison, magnitude) {
  if (!register.hasOwnProperty(key)) register[key] = 0;
  if (!registerOfHighest.hasOwnProperty(key)) registerOfHighest[key] = 0;

  let start = register[key];

  switch (comparison) {
    case '>=':
      return start >= magnitude;
    case '>':
      return start > magnitude;
    case '<=':
      return start <= magnitude;
    case '<':
      return start < magnitude;
    case '==':
      return start == magnitude;
    case '!=':
      return start != magnitude;
  }
}