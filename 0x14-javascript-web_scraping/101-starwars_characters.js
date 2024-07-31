#!/usr/bin/node
// A script that prints all characters of a Star Wars movie
// Displays characters' names in the same order as the "characters" list in the /films/ response

const request = require('request');

const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

function printCharacters(characters, index) {
  if (index >= characters.length) {
    return;
  }

  request(characters[index], (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    } else {
      console.log(JSON.parse(body).name);
      printCharacters(characters, index + 1);
    }
  });
}

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});
