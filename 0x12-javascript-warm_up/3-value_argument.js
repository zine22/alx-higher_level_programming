#!/usr/bin/node
const { argv } = require('process');

const firstArg = argv[2];

if (firstArg === undefined) {
  console.log('No argument');
} else {
  console.log(firstArg);
}
