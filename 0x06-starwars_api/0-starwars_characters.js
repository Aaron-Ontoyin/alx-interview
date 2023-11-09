#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID as the first argument.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    process.exit(1);
  }

  const filmData = JSON.parse(body);

  if (!filmData.characters || filmData.characters.length === 0) {
    console.error('No characters found for this movie.');
    process.exit(1);
  }

  const charactersUrls = filmData.characters;

  // Fetch character names in order
  let count = 0;
  charactersUrls.forEach((characterUrl, index) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (!charError && charResponse.statusCode === 200) {
        const characterData = JSON.parse(charBody);
        console.log(characterData.name);
        count++;

        // Check if all characters have been printed
        if (count === charactersUrls.length) {
          process.exit(0);
        }
      } else {
        console.error('Error fetching character:', charError || `Status Code: ${charResponse.statusCode}`);
        process.exit(1);
      }
    });
  });
});
