'use strict';

const fs = require('fs');
const path = require('path');

let input = fs.readFileSync(path.join(__dirname, './input.txt'), 'utf8');
let rules = input.split('\n')
    .map(line => line.split(' => '));

let start = '.#./..#/###';

class Pattern {
    constructor(pattern) {
        this.pattern = pattern;
        this.rows = pattern.split('/');
    }

    flip() {
        return new Pattern(this.rows.reverse().join('/'));
    }

    rotate() {
        let newPattern = (this.rows.length === 2)
            ? [
                this.rows[1].charAt(0) + this.rows[0].charAt(0),
                this.rows[1].charAt(1) + this.rows[0].charAt(1),
            ]
            : [
                this.rows[2].charAt(0) + this.rows[1].charAt(0) + this.rows[0].charAt(0),
                this.rows[2].charAt(1) + this.rows[1].charAt(1) + this.rows[0].charAt(1),
                this.rows[2].charAt(2) + this.rows[1].charAt(2) + this.rows[0].charAt(2)
            ];

        return new Pattern(newPattern.join('/'));
    }

    getFlavours() {
        let rotated1 = this.rotate();
        let rotated2 = rotated1.rotate();
        let rotated3 = rotated2.rotate();

        let flipped = this.flip();
        let flipRotated1 = flipped.rotate();
        let flipRotated2 = flipRotated1.rotate();
        let flipRotated3 = flipRotated2.rotate();

        return [
            this.pattern,
            rotated1.pattern,
            rotated2.pattern,
            rotated3.pattern,
            flipped.pattern,
            flipRotated1.pattern,
            flipRotated2.pattern,
            flipRotated3.pattern
        ];
    }

    enhance() {
        let flavours = this.getFlavours(), enhancementRule;

        for (let i = 0, ii = flavours.length; i < ii; i++) {
            enhancementRule = rules.find(rule => rule[0] === flavours[i]);
            if (!!enhancementRule) break;
        }

        if (!enhancementRule) throw new Error(`No rule was found: ${this.pattern}`);

        return new Pattern(enhancementRule[1]);
    }

    print() {
        console.log('---------');
        console.log(this.rows.join('\n'));
    }
}

class PatternGroup {
    constructor(seed) {
        this.patterns = [seed];
        this.merge();
    }

    iterate(iterations) {
        // initialize lattice and patterns array
        this.merge();
        this.split();

        while (iterations-- > 0) {
            this.enhance();
            this.merge();
            this.split();
        }

        return this;
    }

    split() {
        let split = this.lattice.split('/');
        let division = split[0].length;

        let rows = split, newPatternSize;
        let patterns = [];

        if (division % 2 === 0) {
            newPatternSize = 2;
        } else if (division % 3 === 0) {
            newPatternSize = 3;
        } else throw new Error('Lattice wasn\'t divisible by 2 or 3.');

        while (rows.length > 0) {
            let rowsToChop = rows.splice(0, newPatternSize);
            let iterator = 0;
            while (iterator < rowsToChop[0].length) {
                let newPattern = rowsToChop[0].substr(iterator, newPatternSize) + '/'
                    + rowsToChop[1].substr(iterator, newPatternSize)
                    + ((rowsToChop[2]) ? '/' + rowsToChop[2].substr(iterator, newPatternSize) : '');

                patterns.push(new Pattern(newPattern));

                iterator += newPatternSize
            }
        }

        this.patterns = patterns;
    }

    merge() {
        let sqrt = Math.pow(this.patterns.length, 0.5);

        if (sqrt === 1) {
            this.lattice = this.patterns[0].pattern;
            return;
        }

        let newPatterns = [];
        while (this.patterns.length > 0) {
            newPatterns.push(this.patterns.splice(0, sqrt));
        }

        newPatterns = newPatterns.map(patternsArray => {
            patternsArray = patternsArray.map(pattern => pattern.rows);
            let string = '';

            for (let i = 0, ii = patternsArray[0].length; i < ii; i++) {
                for (let j = 0, jj = patternsArray.length; j < jj; j++) {
                    string += patternsArray[j][i];
                }

                string += '/'
            }

            return string.substr(0, string.length - 1); // remove trailing forward slash
        });

        this.lattice = newPatterns.join('/');
    }

    enhance() {
        this.patterns = this.patterns.map(pattern => pattern.enhance());
    }

    report() {
        console.log(this.lattice.split('/').join('\n'));
        console.log(`${(this.lattice.match(/#/g) || []).length} pixels turned on.`);
    }
}

start = new Pattern(start);
let group = new PatternGroup(start);

group.iterate(18)
    .report();
