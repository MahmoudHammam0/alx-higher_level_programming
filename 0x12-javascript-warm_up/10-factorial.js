#!/usr/bin/node
const arg = process.argv;
const num = parseInt(arg[2]);
function fact (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  } else {
    return num * fact(num - 1);
  }
}
console.log(fact(num));
