#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.log('Usage: ./0-starwars_characters.js <movieId>');
  process.exit(1);
}

// URL of the Star Wars API endpoint for films
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Parse the response body to JSON
  const data = JSON.parse(body);
  const characters = data.characters;

  // Fetch and print each character's name
  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
