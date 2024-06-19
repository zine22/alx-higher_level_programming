#!/usr/bin/node
const { argv } = require('process');
const numInt = Number(argv[2]);

function factorial (value) {
  if (isNaN(value) || value <= 1) {
    return 1;
  } else {
    return value * factorial(value - 1);
  }
}

console.log(factorial(numInt));
