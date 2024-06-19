#!/usr/bin/node
const { argv } = require('process');
const numInt = Number(argv[2]);

if ((isNaN(numInt)) || (typeof numInt !== 'number')) {
  console.log('Missing size');
} else if (typeof numInt === 'number') {
  if (numInt > 0) {
    for (let i = 0; i < numInt; i++) {
      let row = '';
      for (let j = 0; j < numInt; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
