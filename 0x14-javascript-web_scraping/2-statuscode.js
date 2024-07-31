#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');
const options = {
  url: argv[2],
  method: 'GET'
};
request(options, function (err, response, body) {
  console.log('code :', response.statusCode);
});
