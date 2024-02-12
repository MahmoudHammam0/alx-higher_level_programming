#!/usr/bin/node
const arg = process.argv;
const test = parseInt(arg[2]);
if (arg[2] && (!isNaN(test))) {
  for (let i = 0; i < test; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
