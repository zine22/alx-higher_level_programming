#!/usr/bin/node
const importedVal = require('./100-data.js');

const listVal = importedVal.list;

const map1 = listVal.map((value, index) => value * index);

console.log(listVal);
console.log(map1);
