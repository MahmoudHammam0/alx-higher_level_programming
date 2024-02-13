#!/usr/bin/node
const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const dest = process.argv[4];
const contentA = fs.readFileSync(fileA, 'utf8');
const contentB = fs.readFileSync(fileB, 'utf8');
const destContent = contentA + contentB;
fs.writeFileSync(dest, destContent, 'utf8');
