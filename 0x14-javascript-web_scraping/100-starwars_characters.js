#!/usr/bin/node
// A script that prints all characters of a Star Wars movie

const request = require('request');

const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const characters = JSON.parse(body).characters;

  characters.forEach((character) => {
    request(character, (err, res, charBody) => {
      if (err) {
        console.error('Error:', err);
        return;
      }
      console.log(JSON.parse(charBody).name);
    });
  });
});
