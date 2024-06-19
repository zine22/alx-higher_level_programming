#!/usr/bin/node

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
for (let i = 0; myObject.value < 89; i += 1) {
  myObject.value++;
}
console.log(myObject);
