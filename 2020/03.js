const fs = require('fs');
const path = require('path');

(async () => {
    const input = await new Promise((res) => {
        fs.readFile(path.join(__dirname, './in.txt'), (err, data) => res(data.toString()))
    });

    const grid = input.split('\n').map((l) => l.split(''));

    const w = grid[0].length; // width of repeating pattern

    let x = 0, y = 0;
    const yMax = grid.length - 1;

    let trees = 0;

    // pt 1
    while (y < yMax) {
        x += 3;
        x %= w;
        y += 1;

        if (grid[y][x] === '#') trees++;
    }

    console.log('part 1', trees);

    // pt 2
    const trees2 = [
        [1, 1],
        [3, 1],
        [5, 1],
        [7, 1],
        [1, 2]
    ].map(([dx, dy]) => {
        let x = 0, y = 0;

        let trees = 0;
        while (y < yMax) {
            x += dx;
            x %= w;
            y += dy;

            if (grid[y][x] === '#') trees++;
        }
        return trees;
    }).reduce((a, b) => a * b);

    console.log('part 2', trees2);
})();