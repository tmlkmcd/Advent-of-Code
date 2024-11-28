let steps = 324;

let part = 2;

if (part === 1) {
  let buffer = [0], currentNumber = 0, currentPosition = 0;
  let limit = 2017;

  while (currentNumber++ < limit) {

    // console.log(currentPosition, buffer.length);
    currentPosition += steps;
    currentPosition %= buffer.length;
    currentPosition++;

    buffer.splice(currentPosition, 0, currentNumber);
    console.log(buffer);
  }

  let indexOf2017 = buffer.indexOf(limit);
  console.log(`After 2017 is ${buffer[indexOf2017 + 1]}`);

} else {

  let currentNumber = 1, position = 0, afterZero = 1;
  let limit = 50000000;

  for (let i = 1; i <= limit; i++) {
    position += steps;
    position %= i;
    position++;

    if (position === 1) afterZero = i;
  }

  console.log(`After zero: ${afterZero}`);

}