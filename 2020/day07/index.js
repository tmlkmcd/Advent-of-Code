/*
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
*/

const fs = require('fs');
const path = require('path');

(async () => {
    const input = await new Promise((res) => {
        fs.readFile(path.join(__dirname, './in.txt'), (err, data) => res(data.toString()))
    });

    const rules = input
        .split('\n')
        .reduce((a, b) => ({ ...a, ...parseRule(b) }), {});
    
    console.log('pt1', trawlUp(rules, 'shiny gold').length);

    console.log('pt2', countBags(rules)['shiny gold'] - 1); // minus one - the shiny gold bag itself is not counted
})();

function parseRule(rule) {
    const [bag, contains] = rule.split(' contain ');

    const bags = contains
        .split(', ')
        .map((r) => {
            const g = (r.match(/(?<number>\d) (?<colour>\D+) bags?/) || null);
            return g
                ? {
                    number: parseInt(g.groups.number, 10),
                    colour: g.groups.colour
                }
                : undefined;
        })
        .filter((a) => !!a);

    return {
        [bag.split(' bags')[0]]: bags
    }
}

function trawlUp(rules, colour) {
    let hasIn = [];

    Object.keys(rules).forEach((c) => {
        const has = rules[c].filter((b) => b.colour === colour);

        if (has.length >= 1) {
            hasIn.push(c);
            hasIn = [
                ...hasIn,
                ...trawlUp(rules, c)
            ]
        }
    });

    return Array.from(new Set(hasIn));
}

function countBags(rules) {
    const numbers = { ...rules };

    for (let i in numbers) {
        if (Object.keys(numbers[i]).length === 0) {
            numbers[i] = 1;
        }
    }

    while (true) {
        const stillRequired = Object.keys(numbers)
            .filter((k) => typeof numbers[k] !== 'number');

        if (stillRequired.length === 0) {
            break;
        }

        stillRequired.forEach((k) => {
            const e = numbers[k];
            const notNumber = e.filter((c) => typeof c !== 'number');
            if (notNumber.length === 0) {
                numbers[k] = numbers[k].reduce((a, b) => a + b, 0) + 1;
                return;
            }

            e.forEach((f, i) => {
                if (f.colour && typeof numbers[f.colour] === 'number') {
                    e[i] = numbers[f.colour] * f.number
                }
            });
        });
    }

    return numbers;
}