#!/usr/bin/node

const request = require('request');
const process = require('process');
const url = process.argv[2];
const charId = '18';
let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    results.forEach((movie) => {
      movie.characters.forEach((character) => {
        if (character.includes(charId)) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
