'use strict';
const fs = require('fs');
const path = require('path');

let input = fs.readFileSync(path.join(__dirname, './input.txt'), 'utf8');
let blocks = input.split('\t').map(num => parseInt(num, 10));
let combinations = [], iterations = 0;

function distribute(blocks) {
  let max = Math.max.apply(Math, blocks);
  let ind = blocks.indexOf(max);
  blocks[ind] = 0;

  while (max-- > 0) {
    ind++;
    if (ind >= blocks.length) ind = 0;
    blocks[ind] = blocks[ind] + 1;
  }
}

while (true) {
  let checksum = blocks.join(',');
  if (combinations.includes(checksum)) {
    console.log(`Found repeat after ${iterations} iterations.`);
    console.log(`Loop lasted ${iterations - combinations.indexOf(checksum)} iterations.`);
    break;
  }
  combinations.push(checksum);

  distribute(blocks);
  iterations++;
}