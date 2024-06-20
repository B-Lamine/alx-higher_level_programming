#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] && Number(argv[2])) {
  for (let i = 0; i < parseInt(argv[2]); i++) {
    console.log('X'.repeat(parseInt(argv[2])));
  }
} else {
  console.log('Missing size');
}
