const fs = require('fs');

const input = fs.readFileSync('./day10/input.txt', 'utf8');

// arbitrary!!
const threshold = 180;
const maximum = 100000;
// end arbitrary!!

class Point {
    constructor(data) {
        let details = data.split('<')
            .map(fragment => fragment.split('>')[0]);

        let position = details[1];
        let velocity = details[2];

        this.position = position.split(', ').map(n => parseInt(n, 10));
        this.velocity = velocity.split(', ').map(n => parseInt(n, 10));
    }

    move() {
        let [x1, y1] = this.position;
        let [dx, dy] = this.velocity;

        this.position = [x1 + dx, y1 + dy];
    }

    getPosition() {
        return this.position;
    }

    getModifiedPositionString(dx, dy) {
        let [x, y] = this.position;
        let vX = x - dx;
        let vY = y - dy;
        return this.position.join(',');
    }

    getVelocity() {
        return this.velocity;
    }
}

const points = input.split('\n').map(line => new Point(line));

let counter = 0, hasBeenInThreshold = false;

while (++counter <= maximum) {
    points.forEach(p => p.move());

    if (visualise(points)) {
        break;
    }
}

function visualise(points) {
    let minX, minY, maxX, maxY;

    points.forEach(point => {
        let [x, y] = point.getPosition();

        if (x < minX || minX === undefined) minX = x;
        if (x > maxX || maxX === undefined) maxX = x;
        if (y < minY || minY === undefined) minY = y;
        if (y > maxY || maxY === undefined) maxY = y;
    });

    const xRange = maxX - minX + 15;
    const yRange = maxY - minY + 15;

    if ((xRange < threshold) && (yRange < threshold) && counter === 10886) {
        // 10886 identified as the time taken for message to appear
        hasBeenInThreshold = true;
        let p = points.map(point => point.getModifiedPositionString(minX, minY));
        console.log('================================================', counter)

        let vY = minY - 5;

        while (vY++ < threshold) {
            let vX = minX - 5;
            let row = '';
            while (vX++ < threshold + 150) {

                if (p.includes(`${vX},${vY}`)) {
                    row += '#';
                } else {
                    row += '.';
                }
            }

            console.log(row);
        }
    } else {
        if (counter > 10886) {
            return true;
        }
        if (hasBeenInThreshold) {
            return true;
        }
        // console.log('thresholds exceeded...', `${xRange},${yRange}`);
        return false;
    }
}
