let input = 325489;

class Crawler {
  constructor() {
    this.x = 0;
    this.y = 0;

    this.goUp = this.goUp.bind(this);
    this.goRight = this.goRight.bind(this);
    this.goDown = this.goDown.bind(this);
    this.goLeft = this.goLeft.bind(this);
  }

  goUp() {;this.y = this.y + 1;}
  goRight() {this.x = this.x + 1;}
  goDown() {this.y = this.y - 1;}
  goLeft() {this.x = this.x - 1;}

  getCoordinates() {
    return [this.x, this.y];
  }
}

class Grid {
  constructor(input) {
    this.crawler = new Crawler();
    this.coordinates = [
      {x: 0, y: 0, value: 1}
    ];

    this.limit = input;
  }

  registerCoordinate() {
    let [x, y] = this.crawler.getCoordinates();
    let surroundings = [
      [x-1, y],
      [x-1, y-1],
      [x, y-1],
      [x+1, y-1],
      [x+1, y],
      [x+1, y+1],
      [x, y+1],
      [x-1, y+1]
    ];

    let value = surroundings
      .map(this.getCoordinate.bind(this))
      .reduce((a, b) => a + b);

    this.saveCoordinate({x, y, value});
  }

  saveCoordinate({x, y, value}) {
    if (!this.getCoordinate([x, y])) {
      this.coordinates.push({
        x, y, value
      });
    }
  }

  getCoordinate([x, y]) {
    let existing = this.coordinates.find(coordinate => coordinate.x === x && coordinate.y === y);
    return (existing) ? existing.value : 0;
  }

  spiral() {
    let { goRight, goUp, goLeft, goDown } = this.crawler;
    let action = [goRight, goUp, goLeft, goDown];
    let index = 0;
    let isMovingSideways = true;
    let numOfRepeats = 1;

    while (true) {
      for (let i = 0; i < numOfRepeats; i++) {
        let highest = this.coordinates[this.coordinates.length - 1].value;
        if (highest > this.limit) return this.report();

        action[index]();
        this.registerCoordinate();
      }

      if (!isMovingSideways) numOfRepeats++;
      
      index = (index + 1 === 4) ? 0 : index + 1;
      isMovingSideways = !isMovingSideways;
    }
  }

  report() {
    console.log(this.coordinates.map(coordinate => coordinate.value));
  }
}

let grid = new Grid(input);

grid.spiral();
