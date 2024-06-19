#!/usr/bin/node
exports.esrever = function (list) {
  const newArr = [];
  let j = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    newArr[j] = list[i];
    j++;
  }
  return newArr;
};
