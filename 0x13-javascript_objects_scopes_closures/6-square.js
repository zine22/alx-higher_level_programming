#!/usr/bin/node
const Sqr = require('./5-square');

class Square extends Sqr {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c=undefined) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.size; i++) {
        let x = '';
        for (let j = 0; j < this.size; j++) {
          x += String(c);
        }
        console.log(x);
      }
    }
  }
}

module.exports = Square;
