#!/usr/bin/node
const arg = process.argv;
const array = [];
if (!arg[2] || arg.length === 3) {
  console.log(0);
} else {
  for (let i = 2; i < arg.length; i++) {
    array.push(parseInt(arg[i]));
  }
  array.sort();
  console.log(array[array.length - 2]);
}
