#!/usr/bin/node

const request = require('request');

const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(url, async (error, response, body) => {
  if (error) {
    console.log(error);
  }

  for (const charId of JSON.parse(body).characters) {
    await new Promise((resolve, reject) => {
      request(charId, (error, response, body) => {
        if (error) {
          reject(error);
        }
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
