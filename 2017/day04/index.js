const fs = require('fs');
const path = require('path');

String.prototype.pull = function(char) {
  let index = this.indexOf(char);
  if (index === -1) return this;

  return this.substr(0, index) + this.substr(index + 1, this.length);
};

String.prototype.normalize = function() {
  return this.toLowerCase().trim().replace(/\s/g, '');
};

getInput()
  .then(divide)
  .then(dedupe)
  .then(count)
  .then(console.log);

function getInput() {
  let inputPath = path.join(__dirname, './input.txt');

  return new Promise(function(resolve, reject) {
    fs.readFile(inputPath, 'utf8', (err, data) => {
      if (err) reject(err);
      else resolve(data);
    });
  });
}

function divide(lines) {
  return lines.split('\n').map(line => {
    return line.split(' ').filter(password => !!password);
  });
}

function dedupe(passwords) {
  return passwords.filter(line => {
    let temp = [];

    for (let i = 0, ii = line.length; i < ii; i++) {
      let currentPw = line[i];
      if (temp.includes(currentPw)) return false;

      for (let j = 0, jj = temp.length; j < jj; j++) {
        if (isAnagram(currentPw, temp[j])) return false;
      }

      temp.push(currentPw);
    }

    return true;
  });
}

function count(passwords) {
  return passwords.length;
}

function isAnagram(input1, input2) {
  input1 = input1.normalize();
  input2 = input2.normalize();

  if (input1.length !== input2.length) return false;

  for (let i = 0, ii = input1.length; i < ii; i++) {
    let char = input1.charAt(i);
    if (input2.indexOf(char) === -1) return false;

    input2.pull(char)
  }
  return true;
}