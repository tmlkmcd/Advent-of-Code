const fs = require('fs');
const path = require('path');

const year = '2023';

const yearDirectory = path.join(__dirname, '../', year);

fs.readdir(yearDirectory, (err, files) => {
    files.forEach(file => {
        const dateDirectory = path.join(yearDirectory, file);
        fs.readdir(dateDirectory, (err, files) => {
            const numSolutions = files?.filter((file) => file.split('.')[1] !== 'txt').length ?? 0;

            if (numSolutions > 1) {
                console.log(`Multiple solutions found for ${file}`);
                return;
            }

            (files ?? []).forEach((_file) => {
                const [name, extension] = _file.split('.');
                if (extension === 'txt') return;

                const date = padNumber(file);

                const current = path.join(dateDirectory, _file);
                const next = path.join(yearDirectory, `${date}.${extension}`);

                fs.rename(current, next, (err) => {
                    if (err) {
                        console.log(err);
                    }
                });
            })
        });
    });
});

function padNumber(number) {
    const _number = parseInt(number.match(/\d+/)[0], 10);
    return _number < 10 ? `0${_number}` : _number.toString();
}