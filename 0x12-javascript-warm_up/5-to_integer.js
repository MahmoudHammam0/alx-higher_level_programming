#!/usr/bin/node
const arg = process.argv;
const test = parseInt(arg[2]);
if (arg[2] && (!isNaN(test))) {
  console.log('My number: ' + arg[2]);
} else {
  console.log('Not a number');
}
