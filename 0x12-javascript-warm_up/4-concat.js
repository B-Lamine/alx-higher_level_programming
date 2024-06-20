#!/usr/bin/node
const { argv } = require('node:process');
let argString;
let i = 2;
while (argv[i] && i < argv.length - 1) {
  argString += argv[i];
  if (i === 2) argString = argv[2];
  i++;
  if (argv[i] && i !== argv.length - 1) argString += ' is ';
}
if (argv.length === 3) {
  console.log(argv[i] + ' is ' + argString);
} else {
  console.log(argString + ' is ' + argv[i]);
}
