#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');
request(argv[2], function (err, response, body) {
  console.log('code :', response.statusCode);
});
