#!/usr/bin/node

const request = require('request');
const process = require('process');
const url = process.argv[2];
let count = 0;
request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const results = JSON.parse(body).results;
    const charId = 'https://swapi-api.alx-tools.com/api/people/18/';
    results.forEach(results => {
      if (results.characters.includes(charId)) {
        count++;
      }
    });
    console.log(count);
  }
});
