const fs = require('fs')
const input = fs.readFileSync('./input.txt', 'utf8');

const lines = input.split('\n')

/*
THIS CODE IS MESSY
*/

Date.prototype.addHours = function(h) {    
    this.setTime(this.getTime() + (h*60*60*1000)); 
    return this;   
 }

Date.prototype.addMinutes = function(m) {
    this.setTime(this.getTime() + (m*60*1000));
    return this;
}

class Record {
	constructor(str) {
		let [ date, entry ] = str.split('] ')
		date = date.split(' ').join('T').slice(1);
		date = new Date(date)
        this.date = date;

        this.date.addHours(1);

        if (entry.includes("Guard")) {
			this.entry = parseInt(entry.match(/\d+/)[0])
		} else if (entry.toLowerCase().indexOf('w') === 0) {
            this.entry = 'w'
        } else if (entry.toLowerCase().indexOf('f') === 0) {
            this.entry = 'f'
        } else {
            this.entry = 'unknown:' + entry
        }
    }
    
    toJson() {
        return {
            date: this.date,
            entry: this.entry
        }
    }

	report() {
		console.log(this.date.toISOString(), this.entry)
	}
}

const dates = {}

const records = lines.map(line => new Record(line))
    .sort((a, b) => (a.date < b.date) ? -1 : 1)


records.forEach(r => {
    const date = r.date.getDate();
    const datePadded = date < 10 ? `0${date}` : date;
    const month = r.date.getMonth()+1;
    const monthPadded = month < 10 ? `0${month}` : month;
    const dateKey = `${monthPadded}-${datePadded}`;
    
    if (!dates[dateKey]) {
        dates[dateKey] = {
            guard: undefined,
            events: [],
            map: []
        }
    }

    r.report()

    if (typeof r.entry === 'number') {
        dates[dateKey].guard = r.entry;
    } else {
        dates[dateKey].events.push(r.toJson());
    }
});

for (let day in dates) {
    // console.log(day);
    let arbitrarilyEarlyStartingTime = new Date(`1518-${day}T00:40:00.000`);
    let endingTime = new Date(`1518-${day}T02:05:00.000Z`);

    let time = arbitrarilyEarlyStartingTime;

    let status = '.'

    while (time < endingTime) {
        if (day === '09-27') {
            // console.log('time', time, status)
            // console.log(status)
        }
        let matchingEvent = dates[day].events.find(event => event.date.toISOString() === time.toISOString());
        if (!!matchingEvent) {
            if (matchingEvent.entry === 'f') {
                status = '#'
            } else {
                status = '.'
            }
        }

        if (time.getHours() === 1) {
            dates[day].map.push(status);
        }
        time.addMinutes(1);
    }
}


//part 1
let guards = {}

for (let day in dates) {
    let {guard, map} = dates[day];

    if (!guards[guard]) {
        guards[guard] = 0;
    }

    // console.log(day, guard, map.join(''))

    map.forEach(min => {
        if (min === '#') {
            guards[guard]++;
        }
    })
}

let maxTimeSpentAsleep = Math.max.apply(null, Object.values(guards))
let guardWhoSleepsTheMost = parseInt(Object.keys(guards).filter(k => 
    guards[k] === maxTimeSpentAsleep
)[0]);

let mins = {};

for (let day in dates) {
    let {guard, map} = dates[day];
    if (guard !== guardWhoSleepsTheMost) continue;

    map.forEach((item, index) => {
        if (item === '#') {
            if (!mins[index]) {
                mins[index] = 1
            } else {
                mins[index]++;
            }
        }
    });
}

let minWithMaxSleepAmount = Math.max.apply(null, Object.values(mins));
let minWithMaxSleep = parseInt(Object.keys(mins).filter(k => 
    mins[k] === minWithMaxSleepAmount
)[0]);

console.log(minWithMaxSleep, guardWhoSleepsTheMost, minWithMaxSleep * guardWhoSleepsTheMost);

//part 2

let mins2 = {

}

for (let i2 = 0; i2 < 60; i2++) {
    if (!mins2[i2]) {
        mins2[i2] = {}
    }

    for (let day in dates) {
        let {guard, map} = dates[day];

        if (!mins2[i2][guard]) {
            mins2[i2][guard] = 0
        }
        if (map[i2] === '#') {
            mins2[i2][guard]++
        }
    }
}

for (let minute in mins2) {
    let minsSleeping = Object.values(mins2[minute]);
    let mostTimesSlept = Math.max.apply(null, minsSleeping);

    let guardWhoRockedThisMinute = parseInt(
        Object.keys(mins2[minute])
            .filter(k => mins2[minute][k] === mostTimesSlept)[0]
    );

    console.log(minute, guardWhoRockedThisMinute, mostTimesSlept)
}
// console.log(mins2);