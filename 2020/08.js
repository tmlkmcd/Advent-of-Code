/*
acc +13
jmp -77
acc +15
nop +310
nop +335
jmp +232
acc -3
nop +50
acc +41
jmp +112
*/

const fs = require('fs');
const path = require('path');

(async () => {
    const input = await new Promise((res) => {
        fs.readFile(path.join(__dirname, './in.txt'), (err, data) => res(data.toString()))
    });

    const instructions = input.split('\n').map(parseInstruction);

    const { accumulator } = runProgram(instructions);
    console.log('pt1', accumulator);

    for (let i = 0, ii = instructions.length; i < ii; i++) {
        if (instructions[i].order === 'acc') {
            continue;
        }

        let { accumulator, finished } = runProgram(instructions, i);

        if (finished) {
            console.log('pt2', accumulator);
            break;
        }
    }
})();

function parseInstruction(ins) {
    let [order, amt] = ins.split(' ');
    const dir = amt.slice(0, 1);
    amt = parseInt(amt, 10);

    if (amt === '-') amt *= -1;

    return {
        order,
        amt
    }
}

function runProgram(p, override = -1) {
    const run = [];
    let finished = false;
    let accumulator = 0;

    for (let line = 0;;) {
        if (run.includes(line)) {
            break;
        }

        if (line === p.length) {
            finished = true;
            break;
        }

        run.push(line);
        let {order, amt} = p[line];
        if (line === override) {
            if (order === 'jmp') {
                order = 'nop';
            } else if (order === 'nop') {
                order = 'jmp';
            }
        }
        switch (order) {
            case 'acc':
                accumulator += amt;
                line++;
                break;
            case 'jmp':
                line += amt;
                break;
            case 'nop':
                line++;
                break;
        }
    }

    return {
        accumulator,
        finished
    }
}