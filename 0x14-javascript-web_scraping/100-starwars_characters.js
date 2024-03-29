#!/usr/bin/node

const request = require('request');
const process = require('process');
const movieId = process.argv[2];
const reqUrl = ('https://swapi-api.alx-tools.com/api/films/' + movieId);

request(reqUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const movies = JSON.parse(body).characters;
    movies.forEach((character) => {
      request(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
