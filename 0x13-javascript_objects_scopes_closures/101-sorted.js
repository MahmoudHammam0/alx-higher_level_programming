#!/usr/bin/node
const dict = require('./101-data.js').dict;
const newDict = {};
for (const [id, occ] of Object.entries(dict)) {
  if (newDict[occ] === undefined) {
    newDict[occ] = [];
  }
  newDict[occ].push(id);
}
console.log(newDict);
