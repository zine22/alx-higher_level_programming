#!/usr/bin/node
const { argv } = require('process');
const numInt = Number(argv[2]);

if (isNaN(numInt)) {
  console.log('Not a number');
} else if (typeof numInt === 'number') {
  console.log('My number:', String(Math.floor(numInt)));
} else {
  console.log('Not a number');
}
