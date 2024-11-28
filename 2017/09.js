const fs = require('fs');
const path = require('path');

function getInput() {
  let inputPath = path.join(__dirname, './input.txt');
  return fs.readFileSync(inputPath).toString();
}

let input = getInput();

function run(input) {
  let scoreTracker = [];
  let stack = [];
  let isGarbage = false;
  let ignore = false;
  let garbageCharCounter = 0;

  for (let i = 0, ii = input.length; i < ii; i++) {
    let char = input.charAt(i);

    if (ignore) {
      ignore = false;
      continue;
    }

    if (isGarbage) garbageCharCounter++;

    if (char === '{') {
      if (isGarbage) continue;

      let latestStack = stack[stack.length - 1];
      let score = (latestStack) ? latestStack.score + 1 : 1;

      scoreTracker.push({score});
      stack.push({score});
    }

    if (char === '}') {
      if (!isGarbage) stack.pop();
    }

    if (char === '<') isGarbage = true;
    if (char === '>') {
      isGarbage = false;
      garbageCharCounter--;
    }

    if (char === '!') {
      if (isGarbage) ignore = true;
      garbageCharCounter--;
    }
  }

  let score = scoreTracker.reduce((a,b) => ({score: a.score + b.score})).score;
  
  return {
    score,
    garbageCharCounter
  }
}

console.log(run(input));
