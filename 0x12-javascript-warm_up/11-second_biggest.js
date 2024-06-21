#!/usr/bin/node
const { argv } = require('node:process');
let maxFirst = parseInt(argv[2]);
let maxSecond = parseInt(argv[2]);
if (argv.length <= 3) {
  console.log(0);
} else {
  for (let i = 2; i < argv.length; i++) {
    if (maxFirst < parseInt(argv[i])) {
      maxFirst = parseInt(argv[i]);
    }
  }
  for (let i = 2; i < argv.length; i++) {
    if (parseInt(argv[i]) > maxSecond && parseInt(argv[i]) < maxFirst) {
      maxSecond = parseInt(argv[i]);
    }
  }
  console.log(maxSecond);
}
