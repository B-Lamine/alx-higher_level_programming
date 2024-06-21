#!/usr/bin/node
const { argv } = require('node:process');
function fact (a) {
  if ((a == null) || (a === 0)) return 1;
  return a * fact(a - 1);
}
console.log(fact(argv[2]));
