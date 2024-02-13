#!/usr/bin/node
const dict = require('./101-data.js').dict;
const new_dict = {};
for (const [id, occ] of Object.entries(dict)) {
  if (new_dict[occ] === undefined) {
    new_dict[occ] = [];
  }
  new_dict[occ].push(id);
}
console.log(new_dict);
