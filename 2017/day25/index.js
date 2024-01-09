const fs = require('fs');
const path = require('path');

class Tape {
  constructor({ input }) {
    let preamble = input.shift(), instructions = {};
    let [ initialState, numSteps ] = preamble.split('\n');

    this.initialState = initialState.split(' ').pop().charAt(0).toLowerCase();
    this.numSteps = parseInt(numSteps.match(/\d+/)[0], 10);
    this.stepsTaken = 0;

    this.tape = {};
    this.cursorPosition = 0;
    this.instructions = {};

    this.nextMove = this.initialState;

    instructionsText.forEach(inStateXInstructions => {
      let [
        inState,
        if0,
        write0,
        move0,
        continue0,
        if1,
        write1,
        move1,
        continue1,
      ] = inStateXInstructions.split('\n');

      inState = inState.split(' ').pop().charAt(0).toLowerCase();

      this.instructions[inState] = this.generateInstruction({
        '0': {
          write0,
          move0,
          continue0
        },
        '1': {
          write1,
          move1,
          continue1
        }
      })
    });

    this.getState = this.getState.bind(this);
    this.setState = this.setState.bind(this);
    this.move = this.move.bind(this);
    this.generateInstruction = this.generateInstruction.bind(this);
  }

  getState() {
    let { tape, cursorPosition } = this;

    if (!tape.hasOwnProperty(cursorPosition)) tape[cursorPosition] = 0;
    return tape[cursorPosition];
  }

  setState(state) {
    let { tape, cursorPosition } = this;
    tape[cursorPosition] = state;
  }

  move(direction) {
    if (direction === 'left') this.cursorPosition--;
    else this.cursorPosition++;
  }

  generateInstruction(params) {
    let {
      '0': { write0, move0, continue0 },
      '1': { write1, move1, continue1 }
    } = params;

    write0 = parseInt(write0.match(/\d+/)[0], 10);
    move0 = move0.match(/(left|right)/)[0];
    continue0 = continue0.match(/.\.$/)[0].toLowerCase().charAt(0);

    write1 = parseInt(write1.match(/\d+/)[0], 10);
    move1 = move1.match(/(left|right)/)[0];
    continue1 = continue1.match(/.\.$/)[0].toLowerCase().charAt(0);

    return function({write0, move0, continue0, write1, move1, continue1}) {
      if (this.getState() === 0) {
        this.setState(write0);
        this.move(move0);
        this.nextMove = continue0;
        return;
      }

      this.setState(write1);
      this.move(move1);
      this.nextMove = continue1;
    }.bind(this, {
      write0, move0, continue0, write1, move1, continue1
    });
  }

  run() {
    let { instructions, numSteps } = this;
    while (this.stepsTaken++ < numSteps) {
      let { nextMove } = this;
      instructions[nextMove]();
    }

    this.reportOnes();
  }

  reportOnes() {
    let { tape } = this, numberOfOnes = 0;

    for (let i in tape) {
      if (!tape.hasOwnProperty(i)) continue;
      if (tape[i] === 1) numberOfOnes++;
    }

    console.log(`'${numberOfOnes}' 1s in the tape.`);
  }
}

let instructionsText = fs.readFileSync(path.join(__dirname, './input.txt'), 'utf8')
  .split('\n\n');

let tape = new Tape({
  input: instructionsText
});

tape.run();