const fs = require('fs');
const path = require('path');

const part = 2;

(async () => {
    const input = await new Promise((res) => {
        fs.readFile(path.join(__dirname, './in.txt'), (err, data) => res(data.toString()))
    });

    let grid = input.split('\n')
        .map((g) => g.split(''));

    let i = 0;
    visualize(grid);
    
    while (true) {
        let newGrid = administerStep(grid, part);
        if (compareGrid(grid, newGrid)) {
            break;
        } else {
            grid = newGrid;
        }
    }

    const occupied = grid.reduce((a, b) => ([
        ...a,
        ...b
    ]), []).filter((c) => c === '#').length;

    console.log(occupied);
})();

function administerStep(grid, part) {
    const newGrid = [];

    const limit = (part === 1) ? 4 : 5;
    const aof = (part === 1) ? adjacentOccupied : adjacentOccupied2;

    grid.forEach((row, y) => {
        const newRow = [];
        row.forEach((cell, x) => {
            if (cell === '.') {
                newRow.push('.');
                return;
            }

            const ao = aof(grid, x, y);

            if (cell === 'L' && ao === 0) {
                newRow.push('#');
                return;
            }

            if (cell === '#' && ao >= limit) {
                newRow.push('L');
                return;
            }

            newRow.push(cell);
        });

        newGrid.push(newRow);
    });

    return newGrid;
}

function adjacentOccupied(grid, x, y) {
    const adjacent = [];

    [-1, 0, 1].forEach((dx) => {
        [-1, 0, 1].forEach((dy) => {
            if (dx === 0 && dy === 0) {
                return;
            }

            try {
                adjacent.push(grid[y + dy][x + dx]);
            } catch(e) {
                // do nothing
            }
        })
    })

    return adjacent.filter((c) => c === '#').length;
}

function adjacentOccupied2(grid, x, y) {
    const inLoS = [];

    [-1, 0, 1].forEach((dx) => {
        [-1, 0, 1].forEach((dy) => {
            let xx = x, yy = y;
            if (dx === 0 && dy === 0) {
                return;
            }

            while (true) {
                try {
                    xx += dx;
                    yy += dy;

                    if (grid[yy][xx] === '.') continue;

                    inLoS.push(grid[yy][xx]);
                    break;
                } catch (e) {
                    break;
                }
            }
        });
    });

    return inLoS.filter((c) => c === '#').length;
}

function compareGrid(g1, g2) {
    const r1 = g1
        .map((g) => g.join(''))
        .join('\n');
    const r2 = g2
        .map((g) => g.join(''))
        .join('\n');

    return r1 === r2;
}

function visualize(grid) {
    console.log(grid
        .map((g) => g.join(''))
        .join('\n'));
    console.log('');
    console.log('----------');
    console.log('');
}