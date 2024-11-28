const fs = require('fs');
const path = require('path');

const part = 2;

(async () => {
    const input = await new Promise((res) => {
        fs.readFile(path.join(__dirname, './in.txt'), (err, data) => res(data.toString()))
    });

    const instructions = input.split('\n')
        .map(parseInstruction);

    if (part === 1) {
        const coords = [0, 0];
        let d = 1;

        instructions.forEach((ins) => {
            const [dy, dx, dd] = move(ins, d);

            coords[0] += dy;
            coords[1] += dx;

            d += dd;
            d += 4;
            d = d % 4;
        });

        console.log(coords);
        console.log(Math.abs(coords[0]) + Math.abs(coords[1]));
        return;
    }
    
    let coords = [0, 0];
    let waypointCoords = [1, 10];

    instructions.forEach((ins) => {
        const [cy, cx, wcy, wcx] = move2(ins, coords, waypointCoords);

        coords = [cy, cx];
        waypointCoords = [wcy, wcx];
    });

    console.log(coords);
    console.log(waypointCoords);
    console.log(Math.abs(coords[0]) + Math.abs(coords[1]));
})();

function move(instruction, direction) {
    const [action, value] = instruction;

    if (['L', 'R'].includes(action)) {
        let dd = value/90;
        if (action === 'L') {
            dd *= -1;
        }

        return [0, 0, dd];
    }

    let effectiveDirection = action;

    if (effectiveDirection === 'F') {
        switch (direction) {
            case 0: effectiveDirection = 'N'; break;
            case 1: effectiveDirection = 'E'; break;
            case 2: effectiveDirection = 'S'; break;
            case 3: effectiveDirection = 'W'; break;
            default: throw new Error('Invalid direction: ' + direction);
        }
    }

    switch (effectiveDirection) {
        case 'N': return [value, 0, 0];
        case 'E': return [0, value, 0];
        case 'S': return [value * -1, 0, 0];
        case 'W': return [0, value * -1, 0];
        default: throw new Error('Invalid effective direction: ' + effectiveDirection);
    }
}

function move2(instruction, coords, waypointCoords) {
    const [action, value] = instruction;

    const [cy, cx] = coords;
    const [wcy, wcx] = waypointCoords;

    switch (action) {
        case 'N': return [...coords, wcy + value, wcx];
        case 'E': return [...coords, wcy, wcx + value];
        case 'S': return [...coords, wcy - value, wcx];
        case 'W': return [...coords, wcy, wcx - value];
        // no default - cascade to other options
    }

    if (action === 'F') {
        const dy = wcy * value;
        const dx = wcx * value;

        return [cy + dy, cx + dx, ...waypointCoords];
    }

    let rotation = value/90;

    if (action === 'L') rotation *= -1;

    rotation += 4;
    rotation %= 4;

    if (rotation === 0) {
        return [...coords, ...waypointCoords];
    }

    if (rotation === 1) {
        return [...coords, wcx * -1, wcy];
    }

    if (rotation === 2) {
        return [...coords, wcy * -1, wcx * -1];
    }

    if (rotation === 3) {
        return [...coords, wcx, wcy * -1];
    }
}

function parseInstruction(l) {
    const d = l.charAt(0);
    const a = parseInt(l.slice(1), 10);

    return [d, a];
}
