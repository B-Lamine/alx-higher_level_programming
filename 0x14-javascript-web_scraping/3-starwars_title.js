#!/usr/bin/node
const { argv } = require('node:process');
const request = require('request');
const options = {
  url: 'https://swapi-api.alx-tools.com/api/films/' + argv[2],
  method: 'GET'
};
request(options, function (err, response, body) {
  if (err) {
    console.error(err);
  } else console.log(JSON.parse(body).title);
});
