#!/usr/bin/node

const request = require('request');

async function fetchAndPrintCharacters(filmId) {
  try {
    const filmUrl = `https://swapi-api.hbtn.io/api/films/${filmId}`;
    const filmResponse = await promisifiedRequest(filmUrl);

    for (const characterId of filmResponse.characters) {
      const characterResponse = await promisifiedRequest(characterId);
      console.log(JSON.parse(characterResponse).name);
    }
  } catch (error) {
    console.error(error);
  }
}

function promisifiedRequest(url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(body);
      }
    });
  });
}

const filmId = process.argv[2];
if (!filmId) {
  console.error('Please provide a Film ID as the first argument.');
} else {
  fetchAndPrintCharacters(filmId);
}
