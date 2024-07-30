#!/usr/bin/node

const fs = require('fs');
const request = require('request');
const URL = String(process.argv[2]);
const filePath = String(process.argv[3]);

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const content = body;
    fs.writeFile(filePath, content, { encoding: 'utf-8' }, (err) => {
      if (err) throw err;
    });
  }
});
