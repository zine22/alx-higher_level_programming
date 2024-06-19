#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.height = h;
      this.width = w;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let x = '';
      for (let j = 0; j < this.width; j++) {
        x += 'X';
      }
      console.log(x);
    }
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    let value = null;
    value = this.width;
    this.width = this.height;
    this.height = value;
  }
}

module.exports = Rectangle;
