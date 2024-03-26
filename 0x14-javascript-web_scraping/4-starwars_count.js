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
    for (const result of results) {
      for (const character of result.characters) {
        if (character === charId) {
          count++;
          break;
        }
      }
    }
    console.log(count);
  }
});
