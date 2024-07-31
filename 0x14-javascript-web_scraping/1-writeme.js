#!/usr/bin/node
// A script that writes a string to a file

const fs = require('fs');
const file = process.argv[2];
const writeData = process.argv[3];

fs.writeFile(file, writeData, 'utf8', (error) => {
  if (error) {
    console.error(error);
  }
});
