// 'use strict';

let input = '88,88,211,106,141,1,78,254,2,111,77,255,90,0,54,205';
let skip, position, totalLength = 256; // skip and position on global scope

const test = function() {
    console.log('Part 1 answer:', hash1(input));
    console.log('Empty String:', hash2('')); // should be a2582a3a0e66e6e86e3812dcb672a272
    console.log('AoC 2017:', hash2('AoC 2017')); // should be 33efeb34ea91902bb2f59c9920caa6cd
    console.log('1,2,3:', hash2('1,2,3')); // should be 3efbe78a8d82f29979031a4aa0b16a9d
    console.log('1,2,4:', hash2('1,2,4')); // should be 63960835bcdc130f0b66d7ff4f6a5a8e

    console.log('Part 2 answer:', hash2(input));
};

function hashIteration(input, string) {

  input.forEach(length => {
    let borrowed = 0;

    if ((position + length) >= totalLength) {
      borrowed = (position + length) - totalLength;
      string = string.slice(borrowed, totalLength).concat(string.slice(0, borrowed));
    }

    string = string.slice(0, position - borrowed)
      .concat(string.slice(position - borrowed, position + length - borrowed).reverse())
      .concat(string.slice((position + length - borrowed), totalLength));

    if (borrowed > 0) {
      string = string.slice(totalLength - borrowed, totalLength).concat(string.slice(0, totalLength - borrowed));
    }

    position += (length + skip++);
    position %= totalLength;
  });

  return string;
}

function hash1(input) {
  // reset
  skip = 0;
  position = 0;

  let string = [], totalLength = 256;

  for (let i = 0, ii = totalLength; i < ii; i++) {
    string.push(i);
  }

  input = input.split(',').map(length => parseInt(length, 10));

  return hashIteration(input, string)
    .slice(0, 2).reduce((a, b) => a * b);
}

function hash2(input) {
  // reset
  skip = 0;
  position = 0;

  input = input.split('')
    .filter(char => !!char)
    .map((char, index) => input.charCodeAt(index))
    .concat([17, 31, 73, 47, 23]);

  let string = [], totalLength = 256, iterations = 64;

  for (let i = 0, ii = totalLength; i < ii; i++) {
    string.push(i);
  }

  while (iterations-- > 0) {
    string = hashIteration(input, string);
  }

  let x = [];

  while (string.length > 0) {
    x.push(
      string.splice(0, 16).reduce((a, b) => a^b)
    );
  }

  return x.map(decimalToHex).join('');
}

function decimalToHex(d) {
  let hex = Number(d).toString(16);

  if (hex.length < 2) return '0' + hex;
  return hex;
}

module.exports = hash2;