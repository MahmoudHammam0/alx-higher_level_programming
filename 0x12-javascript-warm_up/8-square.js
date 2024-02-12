#!/usr/bin/node
const arg = process.argv;
const test = parseInt(arg[2]);
if (arg[2] && (!isNaN(test))) {
  let str = "";
  for (let i = 0; i < test; i++) {
    for (let j = 0; j < test; j++) {
      str += 'X';
    }
    if (i !== test - 1) {
      str += '\n';
    }
  }
  if (str !== "") {
    console.log(str);
  }
} else {
  console.log('Missing size');
}
