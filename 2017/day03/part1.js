class GridHandler {
  constructor(input) {
    if (typeof input !== 'number') throw new Error('Must be a number');
    this.input = input;
  }

  findDistance() {
    const { input } = this;
    if (input <= 1) {
      return 0;
    }

    return this
      .getBoundaries()
      .getCorners()
      .findSide()
      .getDistance()
      .report();
  }

  getBoundaries() {
    const { input } = this;

    let i = 1;
    let j = 1;
    while (true) {
      if (Math.pow(i, 2) >= input) break;
      i += 2;
      j++;
    }

    this.layer = j - 1;
    this.upper = Math.pow(i, 2);
    this.lower = Math.pow(i - 2, 2);

    return this;
  }

  getCorners() {
    const { upper, lower } = this;

    let sideLength = (upper - lower) / 4;

    this.corners = {
      bottomRight: upper,
      bottomLeft: upper - sideLength,
      topLeft: upper - (sideLength * 2),
      topRight: upper - (sideLength * 3)
    };

    return this;
  }

  findSide() {
    const { input, lower, corners: {
      topRight, topLeft, bottomRight, bottomLeft
    }} = this;

    let center;

    if (input <= topRight) {
      center = (topRight + lower) / 2;
    } else if (input <= topLeft) {
      center = (topLeft + topRight) / 2;
    } else if (input <= bottomLeft) {
      center = (bottomLeft + topLeft) / 2;
    } else {
      center = (bottomLeft + bottomRight) / 2;
    }

    this.center = center;

    return this;
  }

  getDistance() {
    const { input, center, layer } = this;

    const horizontalDistance = Math.abs(input - center);
    this.distance = horizontalDistance + layer;

    return this;
  }

  report() {
    console.log(this.distance);
  }
}

let input = 325489;
let handler = new GridHandler(input);

handler.findDistance();