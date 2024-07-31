#!/usr/bin/node
// A script that computes the number of tasks completed by user id.

const request = require('request');

const reqURL = process.argv[2];

request(reqURL, (error, response, body) => {
  if (error) {
    console.error('error:', error);
  } else {
    const todos = JSON.parse(body);
    const dash = {};

    todos.forEach((todo) => {
      const { completed, userId } = todo;
      const key = userId.toString();

      if (completed) {
        if (dash[key]) {
          dash[key]++;
        } else {
          dash[key] = 1;
        }
      }
    });

    console.log(dash);
  }
});
