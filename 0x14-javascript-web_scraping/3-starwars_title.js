#!/usr/bin/node

const request = require('request');
const process = require('process');
const id = process.argv[2];
const url = ('https://swapi-api.alx-tools.com/api/films/' + id);
request(url, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
