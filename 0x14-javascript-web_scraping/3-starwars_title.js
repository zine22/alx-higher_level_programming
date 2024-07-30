#!/usr/bin/node

const request = require('request');

const movieID = String(process.argv[2]);

const URL = 'https://swapi-api.alx-tools.com/api/films/' + movieID;

request(URL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
