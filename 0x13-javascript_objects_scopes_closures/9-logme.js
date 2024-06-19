#!/usr/bin/node
const arrVal = [];
let i = 0;

exports.logMe = function (item) {
  arrVal[i] = item;
  console.log(`${i}: ${arrVal[i]}`);
  i++;
};
