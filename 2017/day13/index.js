'use strict';
const fs = require('fs');
const path = require('path');

let input = fs.readFileSync(path.join(__dirname, './input.txt'), 'utf8');
let jsonData = [];
let parsedInput = input.split('\n')
  .map(line => line.split(': '))
  .forEach(([depth, numOfLayers]) => {
    jsonData[parseInt(depth, 10)] = {
      position: 1,
      direction: 'fwd',
      depth: parseInt(numOfLayers, 10)
    };
  });

for (let i = 0, ii = jsonData.length; i < ii; i++) {
  if (!jsonData[i]) jsonData[i] = {depth: 0}
}

let stringifiedJson = JSON.stringify(jsonData);

function getDataClone() {
  return JSON.parse(stringifiedJson);
}

class LayeredSecuritySystem {
  constructor(delay) {
    this.layers = [];
    this.severity = 0;
    this.delay = delay || 0;
    this.crawlerLayer = 0 - this.delay;
  }

  getInput() {
    this.layers = getDataClone();
    return this;
  }

  takeStep() {
    if (this.crawlerLayer >= 0 && this.layers[this.crawlerLayer].position === 1) {
      console.log(`Delay: ${this.delay}, caught at layer ${this.crawlerLayer}.`)
      this.severity += (this.crawlerLayer * this.layers[this.crawlerLayer].depth);
    }

    this.layers = this.layers.map(layer => {
      let {position, direction, depth} = layer;

      if (depth === 0) return layer;

      if (position === 1 && direction === 'bwd') direction = 'fwd';
      if (position === depth && direction === 'fwd') direction = 'bwd';

      if (direction === 'fwd') position++;
      else position--;

      return {position, direction, depth}
    });

    this.crawlerLayer++;
  }

  crawl() {
    while (this.crawlerLayer < this.layers.length - 1) {
      this.takeStep();
      // if (this.caught) break;
    }

    return this;
  }

  getSeverity() {
    return this.severity;
  }
}

// part 1
let system = new LayeredSecuritySystem(15);
console.log('Severity:', system.getInput()
  .crawl()
  .getSeverity());

// part 2
let operations = input.split('\n')
  .map(line => line.split(': ')
    .map(num => parseInt(num, 10))
  );

function skipDelay(i) {
  return !!operations.find(([layer, depth]) => {
    let dangerFrequency = (depth * 2) - 2;

    let distance = i + layer;
    return distance % dangerFrequency === 0;
  });
}

let i = -1;

while (true) {
  console.log(`Checking ${++i}...`);
  if (skipDelay(i)) continue;
  console.log('Good delay found at', i);break;
};