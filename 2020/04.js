/*
eyr:2024 pid:662406624 hcl:#cfa07d byr:1947 iyr:2015 ecl:amb hgt:150cm

iyr:2013 byr:1997 hgt:182cm hcl:#ceb3a1
eyr:2027
ecl:gry cid:102 pid:018128535

hgt:61in iy
*/

const fs = require('fs');
const path = require('path');

(async () => {
    const input = await new Promise((res) => {
        fs.readFile(path.join(__dirname, './in.txt'), (err, data) => res(data.toString()))
    });

    const pp = input.split('\n\n').map(parsePassport);

    console.log(pp
        .filter(validPassport)
        .filter(validPassport2)
        .length);
})();

function parsePassport(pp) {
    const details = pp.split('\n').join(' ').split(' ');
    const passport = {};
    details.forEach((d) => {
        const [k, v] = d.split(':');
        passport[k] = v;
    });

    return passport;
}
function validPassport(pp) {
    const keys = Object.keys(pp);
    return keys.includes('byr')
        && keys.includes('iyr')
        && keys.includes('eyr')
        && keys.includes('hgt')
        && keys.includes('hcl')
        && keys.includes('ecl')
        && keys.includes('pid');
}

function validPassport2(pp) {
    const { byr, iyr, eyr, hgt, hcl, ecl, pid } = pp;

    const nByr = parseInt(byr, 10);
    const vByr = (!!nByr && nByr >= 1920 && nByr <= 2002);

    const nIyr = parseInt(iyr, 10);
    const vIyr = (!!nIyr && nIyr >= 2010 && nIyr <= 2020);

    const nEyr = parseInt(eyr, 10);
    const vEyr = (!!nEyr && nEyr >= 2020 && nEyr <= 2030);

    const nHgt = parseInt(hgt, 10);
    const hgtUnit = hgt.slice(-2);

    const vHgt = (['cm', 'in'].includes(hgtUnit))
        && ((hgtUnit === 'cm' ? (nHgt >= 150 && nHgt <= 193) : false)
            || (hgtUnit === 'in' ? (nHgt >= 59 && nHgt <= 76) : false)
        );
    
    const vHcl = hcl.charAt(0) === '#'
        && hcl.length === 7
        && isHex(hcl.slice(1));

    const vEcl = [
        'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'
    ].includes(ecl);

    const vPid = pid.length === 9 && isNumeric(pid);

    return vByr && vIyr && vEyr && vHgt && vHcl && vEcl && vPid;
        
}

function isHex(c) {
    for (let i = 0, ii = c.length; i < ii; i++) {
        const code = c.charCodeAt(i);
        if (!((code >= 48 && code <= 57) || (code >= 97 && code <= 122))) {
            return false;
        }
    }

    return true;
}

function isNumeric(c) {
    for (let i = 0, ii = c.length; i < ii; i++) {
        const code = c.charCodeAt(i);
        if (!(code >= 48 && code <= 57)) {
            return false;
        }
    }

    return true;
}