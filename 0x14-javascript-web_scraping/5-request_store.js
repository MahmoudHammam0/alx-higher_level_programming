#!/usr/bin/node

const request = require('request');
const process = require('process');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];

request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
