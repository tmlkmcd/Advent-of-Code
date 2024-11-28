const fs = require("fs");

const input = fs.readFileSync("./day01/input.txt", "utf8");
const instructions = input.split("\n");


let ans = 0, ans2;
let freqReached = [];

while (!ans2) {
  // only loop for part 2
  instructions.forEach(line => {
    let dir = line[0];
    let num = parseInt(line.slice(1))
  
    if (dir === "-") ans -= num;
    else ans += num
  
    if (freqReached.indexOf(ans) > -1 && !ans2) {
      ans2 = ans
    }
    freqReached.push(ans);
  });
}



console.log(ans, ans2)