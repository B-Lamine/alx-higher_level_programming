#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');
const options = {
  url: argv[2],
  method: 'GET'
};
request(options, function (err, response, body) {
  if (err) {
    console.error(err);
  } else console.log('code:', response.statusCode);
});
