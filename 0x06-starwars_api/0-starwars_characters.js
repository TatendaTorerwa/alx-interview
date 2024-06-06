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

  if (response.statusCode === 200) {
    // Parse the response body to JSON
    const data = JSON.parse(body);
    const characters = data.characters;

    // Create an array of promises for fetching character details
    const characterPromises = characters.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (error, response, body) => {
          if (error) {
            reject(error);
          } else if (response.statusCode === 200) {
            resolve(JSON.parse(body).name);
          } else {
            reject(`Failed to fetch character: ${response.statusCode}`);
          }
        });
      });
    });

    // Use Promise.all to wait for all promises to resolve
    Promise.all(characterPromises)
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(error => {
        console.error('Error:', error);
      });
  } else {
    console.error(`Failed to fetch movie: ${response.statusCode}`);
  }
});
