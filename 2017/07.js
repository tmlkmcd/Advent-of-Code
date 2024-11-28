const fs = require('fs');
const path = require('path');

let input;

function getInput() {
  let inputPath = path.join(__dirname, './input.txt');

  return new Promise(function(resolve, reject) {
    fs.readFile(inputPath, 'utf8', (err, data) => {
      if (err) reject(err);
      else resolve(data);
      input = data;
    });
  });
}

getInput()
  .then(parse)
  .then(check)
  .then(name => console.log(`Part 1 answer: ${name}`))
  .catch(e => console.log(":(")) ;

function parse(input) {
  return input.split('\n')
    .map(line => {
      let sections = line.split(' ');
      let children = (line.includes(' -> ')) ? line.split(' -> ')[1].split(', ') : [];
      let name = sections[0];
      let weight = parseInt(sections[1].match(/\d+/)[0], 10);
      let trueWeight;

      if (children.length === 0) trueWeight = weight;

      return {name, weight, children, trueWeight}
    });
}

function check(programs) {
  let lonePrograms = programs.filter(program => {
    return input.split(program.name).length === 2;
  });

  if (lonePrograms.length > 1) throw new Error('...');
  return lonePrograms[0].name;
}

// part 2

let allPrograms = {};

getInput()
  .then(parse)
  .then(registerProgram)
  .then(getTrueWeights)
  .then(findProgramsWithoutConsistentTrueWeights)
  .then(findCorrection)
  .then(result => console.log(`Part 2 answer: ${result}`))
  .catch(err => console.warn(err));

function registerProgram(programs) {
  programs.forEach(program => {
    allPrograms[program.name] = program;
  });
}

function getTrueWeights() {
  while (true) {
    let programsAffected = 0;

    for (let programKey in allPrograms) {
      if (!allPrograms.hasOwnProperty(programKey)) continue;

      let program = allPrograms[programKey];

      if (!program.trueWeight) {
        let children = program.children.map(child => allPrograms[child]);
        if (!children.find(child => !child.trueWeight)) {
          programsAffected++;
          program.childrenTrueWeights = children.map(child => child.trueWeight);
          program.trueWeight = program.weight + children.map(child => child.trueWeight).reduce((a, b) => a + b);
        }
      }
    }

    if (programsAffected === 0) break;
  }
}

function findProgramsWithoutConsistentTrueWeights() {
  let inconsistents = [];

  for (let programKey in allPrograms) {
    if (!allPrograms.hasOwnProperty(programKey)) continue;

    let program = allPrograms[programKey];
    if (program.children.length === 0) continue;

    let children = program.children
      .map(child => allPrograms[child]);

    checkChildren: for (let i = 0, ii = children.length; i < ii; i++) {
      if (children[0].trueWeight !== children[i].trueWeight) {
        inconsistents.push(program.name);
        break checkChildren;
      }
    }
  }

  return inconsistents;
}

function findCorrection(inconsistents) {
  // find the program at the top of this hierarchy

  let offenderParent = inconsistents.find(programKey => {
    let program = allPrograms[programKey];

    for (let i = 0, ii = inconsistents.length; i < ii; i++) {
      if (program.children.includes(inconsistents[i])) return false;
    }

    return true;
  });

  offenderParent = allPrograms[offenderParent];

  let wrongWeightIndex = findOddOneOut(offenderParent.childrenTrueWeights);
  let wrongWeightProgram = allPrograms[offenderParent.children[wrongWeightIndex]];
  let wrongWeight = offenderParent.childrenTrueWeights[wrongWeightIndex];
  let correctWeight = offenderParent.childrenTrueWeights[!!wrongWeightIndex ? 0 : 1];
  let correction = correctWeight - wrongWeight;

  return wrongWeightProgram.weight + correction;
}

function findOddOneOut(list) {
  for (let i = 0, ii = list.length; i < ii; i++) {
    if (list.filter(item => item === list[i]).length === 1) return i;
  }
}