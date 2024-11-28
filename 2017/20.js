'use strict';

const fs = require('fs');
const path = require('path');

class Particle {
    constructor({data, index}) {
        let [position, velocity, acceleration] = data.split(', ');

        this.id = index;

        this.position = position.split('<')[1].split(',').map(number => parseInt(number, 10));
        this.velocity = velocity.split('<')[1].split(',').map(number => parseInt(number, 10));
        this.acceleration = acceleration.split('<')[1].split(',').map(number => parseInt(number, 10));

        this.iterations = 0;
        this.distances = [];

        this.getAcceleration();
    }

    getAcceleration() {
        let [aX, aY, aZ] = this.acceleration;

        this.accelerationMagnitude = Math.abs(aX) + Math.abs(aY) + Math.abs(aZ);
    }

    move() {
        this.iterations++;

        let [aX, aY, aZ] = this.acceleration;
        let [vX, vY, vZ] = this.velocity;
        let [pX, pY, pZ] = this.position;

        vX += aX;
        vY += aY;
        vZ += aZ;

        pX += vX;
        pY += vY;
        pZ += vZ;

        this.velocity = [vX, vY, vZ];
        this.position = [pX, pY, pZ];

        this.registerDistance();
    }

    registerDistance() {
        let [pX, pY, pZ] = this.position;
        let distance = Math.abs(pX) + Math.abs(pY) + Math.abs(pZ);

        this.distances.push(distance);
    }
}

function checkCollisions(particles) {
    let occupiedPositions = particles.map(particle => particle.position.join(','));

    return particles.map(particle => {
        let position = particle.position.join(',');

        if (occupiedPositions.indexOf(position) !== occupiedPositions.lastIndexOf(position)) {
            particle.destroyed = true;
        }

        return particle;
    });
}

let particles = fs.readFileSync(path.join(__dirname, './input.txt'), 'utf8')
    .split('\n')
    .map((data, index) => new Particle({data, index}));

let lowestAccelerationMagnitude = particles
    .reduce((a, b) => (
        a.accelerationMagnitude >= b.accelerationMagnitude) ? b : a
    ).id;

console.log(`Particle ${lowestAccelerationMagnitude} probably stays closest to the origin.`);

let iterator = 0;
let iterations = 50;

while (iterator++ < iterations) {
    particles.forEach(particle => {
        if (!particle.destroyed) particle.move();
    });
    checkCollisions(particles);
}

let particlesRemaining = particles.filter(particle => !particle.destroyed).length;

console.log(`${particlesRemaining} particles remaining.`);