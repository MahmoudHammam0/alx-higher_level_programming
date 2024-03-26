#!/usr/bin/node

const request = require('request');
const process = require('process');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  const list = JSON.parse(body);
  const res = {};
  if (error) {
    console.log(error);
  } else {
    list.forEach((task) => {
      if (task.completed) {
        if (!res[task.userId]) {
          res[task.userId] = 1;
        } else {
          res[task.userId]++;
        }
      }
    });
    console.log(res);
  }
});
