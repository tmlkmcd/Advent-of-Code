const fs = require('fs');
const path = require('path');

let input = fs.readFileSync(path.join(__dirname, './input.txt'), 'utf8')
  .split('\n')
  .map(line => line.split(' '));

let part = 2;
let sentVals = 0;

class Program {
  constructor({id, link}) {
    this.id = id;
    this.input = input;
    this.registers = {
      p: id
    };
    this.lastPlayed = {};

    this.snd = (part === 1) ? this.snd.bind(this) : this.sndPt2.bind(this);
    this.set = this.set.bind(this);
    this.add = this.add.bind(this);
    this.mul = this.mul.bind(this);
    this.mod = this.mod.bind(this);
    this.rcv = (part === 1) ? this.rcv.bind(this) : this.rcvPt2.bind(this);
    this.getVal = this.getVal.bind(this);
    this.run = (part === 1) ? this.run.bind(this) : this.runPt2.bind(this);

    if (part === 2) {
      if (link) {
        this.link = link;
        this.link.link = this;
      }

      this.queue = [];
      this.i = 0;
    }
  }

  snd(pointer) {
    this.lastPlayed[pointer] = this.registers[pointer];
    console.log(`Playing sound ${this.registers[pointer]} (${pointer}).`);
  }

  set (pointer, value) {
    this.registers[pointer] = value;
  }

  add(pointer, value) {
    this.registers[pointer] = (this.registers[pointer] || 0) + value;
  }

  mul(pointer, value) {
    this.registers[pointer] = (this.registers[pointer] || 0) * value;
  }

  mod(pointer, value) {
    this.registers[pointer] = (this.registers[pointer] || 0) % value;
  }

  rcv(pointer) {
    if (!!this.lastPlayed[pointer]) console.log(`Recovered ${this.lastPlayed[pointer]} from ${pointer}.`);

    if (part === 1 && this.lastPlayed[pointer] > 0) {
      let msg = `Aborting program - non zero value received: ${this.lastPlayed[pointer]}`;
      throw new Error(msg);
    }
  }

  sndPt2(pointer) {
    this.link.queue.push(this.registers[pointer]);

    if (this.id === 1) {
      sentVals++;
    }
  }

  rcvPt2(pointer) {
    if (!this.queue.length) return false;

    this.registers[pointer] = this.queue.shift();
    return true;
  }

  getVal(pointer) {
    if (pointer.match(/^(\-)?\d+$/)) return parseInt(pointer, 10);

    if ((pointer.match(/^\D+$/))) {
      if (!!this.registers[pointer]) return parseInt(this.registers[pointer], 10);
      return 0;
    }
  }

  run() {
    try {
      for (let i = 0, ii = input.length; i < ii; null) {
        // console.log(`LINE ${i + 1}: ${input[i].join('/')}`);

        let line = input[i], action, pointer, value;

        if (line.length === 3) [action, pointer, value] = line;
        else [action, pointer] = line;

        value = (value) ? this.getVal(value) : null;

        if (action === 'jgz') {
          if (this.getVal(pointer) > 0) {
            i += (value || 1);
          } else {
            i++;
          }
        } else {
          this[action](pointer, value);
          i++;
        }
      }
    } catch (e) {
      console.log('Terminating');
    }
  }

  runPt2(cb) {
    // console.log(this.i);
    let line = input[this.i], action, pointer, value;

    if (line.length === 3) [action, pointer, value] = line;
    else [action, pointer] = line;

    value = (value) ? this.getVal(value) : null;

    if (action === 'jgz') {
      if (this.getVal(pointer) > 0) {
        this.i += (value || 1);
      } else {
        this.i++;
      }
    } else if (action === 'rcv') {
      let gotValue = this.rcv(pointer);
      if (!gotValue) {
        cb();
        return false;
      }

      this.i++;
    } else {
      this[action](pointer, value);
      this.i++;
    }

    return true;
  }
}

if (part === 1) {
  let id = 0;
  let program = new Program({id});
  program.run();
}

if (part === 2) {
  let first = new Program({id: 0});
  let second = new Program({id: 1, link: first});

  let currentSystem = first;
  let lastResult = true;

  function callback() {
    if (currentSystem === first) {
      currentSystem = second;
    } else {
      currentSystem = first;
    }
  }

  while (true) {
    let x = currentSystem.run(callback);
    if (!x && !lastResult) break;

    lastResult = x;
  }

  console.log(`Program sent values ${sentVals} times.`);
}