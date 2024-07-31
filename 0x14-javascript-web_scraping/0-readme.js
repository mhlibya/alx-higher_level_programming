#!/usr/bin/node
// A script that reads and prints the content of a file

const fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf8', (error, data) => {
  if (error) {
    console.error(error);
  } else {
    console.log(data);
  }
});
