'use strict';
const fs = require('fs');
const path = require('path');

function getInput() {
  return new Promise(resolve => {
    fs.readFile(path.join(__dirname, './input.txt'), 'utf8', (err, data) => resolve(data));
  });
}

function parse(input) {
  let programs = {};

  input.split('\n').forEach(stringInput => {
    let [id, connections] = stringInput.split(' <-> ');
    programs[id] = {
      connections: connections.split(', ').map(number => parseInt(number, 10))
    }
  });

  return programs;
}

function findConnections(programs, index, store) {
  if (!programs[index]) return;

  let foundNewProgram = false;
  programs[index].connections.forEach(connection => {
    if (store.includes(connection)) return;
    foundNewProgram = true;
    store.push(connection);
    findConnections(programs, connection, store);
  });

  delete programs[index];
}

function findGroups(programs) {
  let groups = 0;
  while (Object.keys(programs).length) {
    groups++;
    let firstProgram = Object.keys(programs)[0], connections = [];
    findConnections(programs, firstProgram, connections);
  }
  return groups;
}

const connectedProgramsPart1 = [];
getInput().then(parse)
  .then(programs => findConnections(programs, 0, connectedProgramsPart1))
  .then(() => console.log(`${connectedProgramsPart1.length} programs connected to program 0.`));

getInput().then(parse)
  .then(findGroups)
  .then(groups => console.log(`${groups} groups in total.`));