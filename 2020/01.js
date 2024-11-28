
const fs = require('fs');
const path = require('path');

(async () => {
    const input = await new Promise((res) => {
        fs.readFile(path.join(__dirname, './in.txt'), (err, data) => res(data.toString()));
    });
    
    const numbers = input.split('\n').map((n) => parseInt(n, 10));
    
    for (let i = 0, ii = numbers.length; i < ii; i++) {
        for (let j = i + 1; j < ii; j++) {
            const n1 = numbers[i];
            const n2 = numbers[j];
            if ((n1 + n2) === 2020) {
                console.log(n1 * n2);
                break;
            }
        }
    }

    for (let i = 0, ii = numbers.length; i < ii; i++) {
        for (let j = i + 1; j < ii; j++) {
            for (let k = j + 1; k < ii; k++) {
                const n1 = numbers[i];
                const n2 = numbers[j];
                const n3 = numbers[k];
                if ((n1 + n2 + n3) === 2020) {
                    console.log(n1 * n2 * n3);
                    break;
                }
            }
        }
    }
})();