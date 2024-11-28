'use strict';

const fs = require('fs');
const path = require('path');

let map = fs.readFileSync(path.join(__dirname, './input.txt'), 'utf8')
    .split('\n')
    .map(
        row => row.split('')
    );

let part = 2;

class Grid {
    constructor() {
        this.map = map;
        this.pad(1000);

        let startingCoords = [
            Math.floor(this.map.length / 2),
            Math.floor(this.map[0].length / 2)
        ];

        this.virus = new Virus({
            grid: this,
            startingCoords
        });
    }

    iterate() {
        (part === 1) ? this.virus.burst() : this.virus.burstPt2();
    }

    pad(number) {
        let newLength = this.map.length + (2 * number), iterator = 0;
        this.map = this.map.map(row => {
            return Grid.noise(number).concat(row).concat(Grid.noise(number));
        });


        while (iterator++ < number) {
            this.map.unshift(Grid.noise(newLength));
            this.map.push(Grid.noise(newLength))
        }
    }

    print() {
        console.log(this.map
            .map(row => row.join(''))
            .join('\n'));
    }

    report() {
        this.print();
        return this.virus.report();
    }

    static noise(number) {
        let newArray = [];
        while (newArray.length < number) {
            newArray.push('.');
        }

        return newArray;
    }
}

class Virus {
    constructor({ grid, startingCoords }) {
        this.grid = grid;
        this.direction = 'up';
        this.infectionCount = 0;
        let [x, y] = startingCoords;

        this.x = x;
        this.y = y;

        this.setNode = this.setNode.bind(this);
        this.getNode = this.getNode.bind(this);
        this.turnLeft = this.turnLeft.bind(this);
        this.turnRight = this.turnRight.bind(this);

        this.reverse = this.reverse.bind(this);
    }

    setNode(character) {
        let { x, y } = this;
        this.grid.map[y][x] = character;
    }

    getNode() {
        let { grid, x, y } = this;
        return grid.map[y][x];
    }

    burst() {
        let { getNode, setNode, turnRight, turnLeft } = this;

        if (getNode() === '#') {
            setNode('.');
            turnRight();
        } else {
            this.infectionCount++;
            setNode('#');
            turnLeft();
        }

        switch (this.direction) {
            case 'up': this.y--; break;
            case 'left': this.x--; break;
            case 'down': this.y++; break;
            case 'right': this.x++; break;
        }
    }

    burstPt2() {
        let { getNode, setNode, turnRight, turnLeft, reverse } = this;

        switch (getNode()) {
            case '#':
                setNode('F');
                turnRight();
                break;
            case '.':
                setNode('W');
                turnLeft();
                break;
            case 'W':
                this.infectionCount++;
                setNode('#');
                break;
            case 'F':
                setNode('.');
                reverse();
                break;

        }

        switch (this.direction) {
            case 'up': this.y--; break;
            case 'left': this.x--; break;
            case 'down': this.y++; break;
            case 'right': this.x++; break;
        }
    }

    turnLeft() {
        let { direction } = this;
        switch (direction) {
            case 'up': this.direction = 'left'; break;
            case 'left': this.direction = 'down'; break;
            case 'down': this.direction = 'right'; break;
            case 'right': this.direction = 'up'; break;
        }
    }

    turnRight() {
        let { direction } = this;
        switch (direction) {
            case 'up': this.direction = 'right'; break;
            case 'left': this.direction = 'up'; break;
            case 'down': this.direction = 'left'; break;
            case 'right': this.direction = 'down'; break;
        }
    }

    reverse() {
        let { direction } = this;
        switch (direction) {
            case 'up': this.direction = 'down'; break;
            case 'left': this.direction = 'right'; break;
            case 'down': this.direction = 'up'; break;
            case 'right': this.direction = 'left'; break;
        }
    }

    report() {
        return this.infectionCount;
    }
}

let grid = new Grid();

let iterations = 0, totalIterations = (part === 1) ? 10000 : 10000000;

if (totalIterations === 0) grid.print();

while (iterations++ < totalIterations) {
    grid.iterate();
}

console.log(`Part ${part} answer: ${grid.report()} infections performed.`);