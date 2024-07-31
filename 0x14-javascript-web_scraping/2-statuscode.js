#!/usr/bin/node
// A script that displays the status code of a GET request

const request = require('request');
const url = process.argv[2];

request(url, (error, response) => {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  } else {
    console.log('code:', response && response.statusCode);
  }
});
