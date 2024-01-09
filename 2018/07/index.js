const fs = require("fs");
const input = fs.readFileSync("./input.txt", "utf-8");
const inputSteps = input.split("\n");

class Worker {
    workingOn = null;
    freeAt = 0;

    constructor(steps) {
        this.steps = steps;
    }

    engage(step, currentTime) {
        this.workingOn = step;
        this.freeAt = currentTime + step.time;
    }

    free() {
        this.steps.complete(this.workingOn.name);
        this.workingOn = null;
    }
}

class Steps {
    steps = [];
    completed = [];
    time = -1;
    workers = [...new Array(5)].map((_) => new Worker(this));

    addStep(name) {
        const stepExists = this.findStep(name);
        if (!!stepExists) {
            return stepExists;
        }

        const newStep = new Step(name);

        this.steps.push(newStep);
        return newStep;
    }

    tick() {
        this.time++;

        this.workers.forEach((w) => {
            if (w.workingOn === null) return;

            if (w.freeAt <= this.time) {
                w.free();
            }
        });
        const a = this.findAvailable();

        this.workers
            .filter((w) => w.workingOn === null)
            .forEach((w, i) => {
                if (!a[i]) {
                    return;
                }

                w.engage(a[i], this.time);
            });
    }

    findStep(findName) {
        return this.steps.find(({ name }) => name === findName);
    }

    complete(step) {
        this.findStep(step).completed = true;
        this.completed = Array.from(new Set([...this.completed, step]));

        this.steps.forEach((s) => {
            s.checkReady(this.completed);
        });
    }

    findNext() {
        // pt1
        const n = this.steps
            .filter((s) => s.ready && !s.completed)
            .map(({ name }) => name)
            .sort()[0];

        return this.findStep(n);
    }

    findAvailable() {
        // pt2
        const n = this.steps
            .filter((s) => s.ready && !s.completed)
            .filter((s) => {
                for (let i = 0, ii = this.workers.length; i < ii; i++) {
                    if (this.workers[i].workingOn?.name === s.name) {
                        return false;
                    }
                }
                return true;
            })
            .map(({ name }) => name)
            .sort();

        return n.map((nn) => this.findStep(nn));
    }
}
class Step {
    requirements = [];
    completed = false;
    ready = true;
    time = -1;

    constructor(name) {
        this.name = name;
        this.time = this.name.charCodeAt(0) - 64 + 60;
    }

    registerReq(req) {
        this.ready = false;

        if (this.requirements.includes(req)) return;
        this.requirements.push(req);
    }

    checkReady(completed) {
        for (let i = 0, ii = this.requirements.length; i < ii; i++) {
            if (!completed.includes(this.requirements[i])) {
                return;
            }
        }

        this.ready = true;
    }

    toString() {
        return `Step ${this.name} requires ${this.requirement}`;
    }
}

function initialise() {
    const steps = new Steps();

    inputSteps.forEach((s) => {
        const ss = s.split(" ");
        const sReq = ss[1];
        const sName = ss[7];

        steps.addStep(sName).registerReq(sReq);
        steps.addStep(sReq);
    });

    return steps;
}

// part 1

const steps1 = initialise();
const order = [];

while (true) {
  const next = steps1.findNext();
  if (!next) {
    break;
  }

  order.push(next.name);
  steps1.complete(next.name);
}

console.log("part 1", order.join(""));

// part 2

const steps2 = initialise();

while (steps2.completed.length < steps2.steps.length) {
    steps2.tick();
}

console.log("part 2", steps2.time)
