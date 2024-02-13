#!/usr/bin/node
const list = require('./100-data.js');
const new_list = list.list.map((x) => x * list.list.indexOf(x));
console.log(list.list);
console.log(new_list);
