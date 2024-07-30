#!/usr/bin/node

const fs = require('fs');

const arg = process.argv[2];
/* console.log(arg[2]); */

fs.readFile(String(arg), 'utf-8', (err, inputD) => {
  if (err) throw err;
  console.log(inputD.toString());
});
