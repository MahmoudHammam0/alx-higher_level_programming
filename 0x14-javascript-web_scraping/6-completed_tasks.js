#!/usr/bin/node

const request = require('request');
const process = require('process');
const url = process.argv[2];

request.get(url, (error, response, body) => {
  const list = JSON.parse(body);
  const res = {};
  if (error) {
    console.log(error);
    return;
  }
  for (const task of list) {
    if (!(task.userId in res)) {
      if (task.completed === true) {
        res[task.userId] = 1;
      } else {
        res[task.userId] = 0;
      }
    } else if (task.userId in res && task.completed === true) {
      res[task.userId]++;
    }
  }
  console.log(res);
});
