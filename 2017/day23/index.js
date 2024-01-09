const fs = require('fs');
const path = require('path');

let part = 2;

let input = fs.readFileSync(path.join(__dirname, './input.txt'), 'utf8')
  .split('\n')
  .map(line => line.split(' ')
    .map(token => {
      if (token.match(/^(\-|\+)?(\d)+$/)) return parseInt(token, 10);
      return token;
    })
  );

class Program {
  constructor(){
    this.registers = {
      a: 0,
      b: 0,
      c: 0,
      d: 0,
      e: 0,
      f: 0,
      g: 0,
      h: 0
    };

    this.instructions = input;

    this.set = this.set.bind(this);
    this.sub = this.sub.bind(this);
    this.mul = this.mul.bind(this);
    this.run = this.run.bind(this);

    this.timesMultiplied = 0;
  }

  set(key, value) {
    this.registers[key] = value;
  }

  sub(key, value) {
    this.registers[key] -= value;
  }

  mul(key, value) {
    this.timesMultiplied++;
    this.registers[key] *= value;
  }

  run() {
    let i = 0;
    while (true) {
      console.log(`${i}, ${this.instructions[i]}`);
      if (!this.instructions[i]) break;

      let [cmd, register, value] = this.instructions[i];
      if (typeof value === 'string') value = this.registers[value];

      if (['set', 'sub', 'mul'].includes(cmd)) {
        this[cmd](register, value);
        i++;
      }

      if (cmd === 'jnz') {
        let valueToCheck = (typeof register === 'string') ? this.registers[register] : register;
        if (valueToCheck > 0 || valueToCheck < 0) {
          i += value;
        } else {
          i++;
        }
      }
    }

    return this;
  }

  report() {
    console.log(this.registers);
    console.log(`Used multiply ${this.timesMultiplied} times.`);
  }
}

let program = new Program();

if (part === 1) program.run().report();
else {
  // console.log('?')
  const run = require('./part2');
  run();
}

