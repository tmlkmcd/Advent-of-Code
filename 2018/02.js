const fs = require("fs");

const input = fs.readFileSync("./day02/input.txt", "utf8");
const boxes = input.split("\n");

class Box {
  constructor(id) {
    this.id = id;
    this.letters = {}
    id.split('').forEach(letter => {

      if (!this.letters[letter]) {
        this.letters[letter] = 0;
      }

      this.letters[letter]++
    });
  }

  hasTwo() {
    return Object.values(this.letters).indexOf(2) > -1;
  }

  hasThree() {
    return Object.values(this.letters).indexOf(3) > -1;
  }
}

let twox = 0;
let threex = 0;

// part1

boxes.forEach(box => {
  let thisBox = new Box(box);
  if (thisBox.hasTwo()) {
    twox++;
  }

  if (thisBox.hasThree()) {
    threex++;
  }
});

console.log("Part 1 answer", twox * threex)

// part2

boxes.forEach((box, index) => {
  boxes.slice(index+1).forEach(compareBox => {
    if (compareString(box, compareBox) === 1) {
      console.log("Part 2 answer");
      console.log(box, compareBox);
    }
  });
});

function compareString(a, b) {
  let diff = 0;
  for (let i = 0; i < a.length; i++) {
    if (b.charAt(i) !== a.charAt(i)) {
      diff++;
    }
  }

  return diff;
}