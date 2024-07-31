#!/usr/bin/node
// A script that prints the number of movies where the character Wedge Antilles is present

const request = require('request');
const reqURL = process.argv[2];

request(reqURL, (error, response, body) => {
  if (error) {
    console.error('error:', error); // Print the error if one occurred
  } else {
    const data = JSON.parse(body);
    const results = data.results;
    let count = 0;

    results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.endsWith('18/')) {
          count++;
        }
      });
    });

    console.log(count);
  }
});
