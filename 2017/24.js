const fs = require('fs');
const path = require('path');

let allBridges = [];

class Component {
  constructor({ input, index }) {
    let [a, b] = input.split('/');
    this.id = index;

    this.a = parseInt(a, 10);
    this.b = parseInt(b, 10);

    this.has = this.has.bind(this);
    this.clone = this.clone.bind(this);
    this.getOtherSide = this.getOtherSide.bind(this);
    this.toString = this.toString.bind(this);
  }

  clone() {
    let { toString, id } = this;
    let input = `${a}/${b}`, index = id;
    return new Component({input, index});
  }

  has(number) {
    return (this.a === number || this.b === number);
  }

  getOtherSide(number) {
    let {a, b} = this;

    if (number === a) return b;
    return a;
  }

  getStrength() {
    return this.a + this.b;
  }

  toString() {
    return `${this.a}/${this.b}`;
  }
}

class Bridge {
  constructor(options) {
    let { component } = options;

    this.facing = 0;
    this.components = [];
    this.strength = 0;

    this.add = this.add.bind(this);
    this.has = this.has.bind(this);
    this.clone = this.clone.bind(this);
    this.build = this.build.bind(this);

    if (component) this.add(component);
    allBridges.push(this);
  }

  add(component) {
    let { facing } = this;

    if (!component.has(facing)) throw new Error('Tried to add invalid component.');

    this.components.push(component);
    this.facing = component.getOtherSide(facing);
  }

  has(component) {
    let { components } = this;
    let { id } = component;

    return !!components.find(comp => comp.id === id);
  }

  clone() {
    let {facing, components} = this;
    let bridge = new Bridge({});

    bridge.facing = facing;
    bridge.components = components.slice();

    return bridge;
  }

  build(components) {
    let { facing, add, has, build, clone } = this;

    let validNextComponents = components.filter(component =>
      !has(component) && component.has(facing));

    if (!validNextComponents.length) return;
    // if (this.components.length > 4) return;

    if (validNextComponents.length === 1) {
      add(validNextComponents[0]);
      build(components);
    } else if (validNextComponents.length > 1) {
      let firstValidComponent = validNextComponents.shift();

      validNextComponents.forEach(component => {
        let bridge = clone();
        bridge.add(component);
        bridge.build(components);
      });

      add(firstValidComponent);
      build(components);
    }
  }

  toString() {
    return this.components.map(component => component.toString()).join('--');
  }

  getStrength() {
    let { components } = this;

    return components
      .map(component => component.getStrength())
      .reduce((a, b) => a + b);
  }

  getLength() {
    return this.components.length;
  }
}

let components = fs.readFileSync(path.join(__dirname, './input.txt'), 'utf8')
  .split('\n')
  .map((line, index) => new Component({input: line, index}));

let bridges = components.filter(component => component.has(0))
  .map(component => new Bridge({component}));

bridges.forEach(bridge => bridge.build(components));

let maxStrength = allBridges
  .map(bridge => bridge.getStrength())
  .reduce((a, b) => Math.max(a, b));

let maxLength = allBridges
  .map(bridge => bridge.getLength())
  .reduce((a, b) => Math.max(a, b));

let bridgesWithMaxLength = allBridges
  .filter(bridge => bridge.getLength() === maxLength);

let strongestBridgesWithMaxLength = bridgesWithMaxLength
  .map(bridge => bridge.getStrength())
  .reduce((a, b) => Math.max(a, b));

console.log(`Maximum strength: ${maxStrength}`);
console.log(`Strength of strongest bridge with max length: ${strongestBridgesWithMaxLength}`);