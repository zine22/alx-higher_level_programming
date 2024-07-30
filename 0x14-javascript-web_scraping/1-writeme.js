#!/usr/bin/node

const fs = require('fs');

const filePath = String(process.argv[2]);
const stringToWrite = String(process.argv[3]);

fs.writeFile(filePath, stringToWrite, { encoding: 'utf-8' }, (err) => {
  if (err) throw err;
});
