# 0x06. Star Wars API

## Description
This project focuses on interacting with an external API to fetch and display information about Star Wars characters based on the movie ID provided as an argument. To successfully complete this project, you need to be familiar with key concepts related to web programming, API interaction, and asynchronous programming in JavaScript.

## Concepts Needed
- HTTP Requests in JavaScript
- Working with APIs
- Asynchronous Programming
- Command Line Arguments in Node.js
- Array Manipulation and Iteration

## Resources
- [A Complete Guide to Making HTTP Requests in Node.js](link_here)
- [Working with APIs in JavaScript](link_here)
- [Asynchronous Programming in JavaScript](link_here)
- [How to Parse Command Line Arguments in Node.js](link_here)
- [JavaScript Array Methods](link_here)

## Requirements
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted on Ubuntu 20.04 LTS using `node` (version 10.14.x)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A `README.md` file at the root of the project folder is mandatory
- Code should be `semistandard` compliant with additional rules from AirBnB style
- All files must be executable
- Use `let` and `const` instead of `var`

## More Info
- [Install Node 10](installation_instructions_here)
- [Install semi-standard](installation_instructions_here)
- [Install and use the `request` module](installation_instructions_here)

## Tasks
### 0. Star Wars Characters
Write a script that prints all characters of a Star Wars movie:
- The first positional argument passed is the Movie ID (e.g., 3 for "Return of the Jedi")
- Display one character name per line in the same order as the `characters` list in the `/films/` endpoint
- Use the Star Wars API
- Use the `request` module

Example:
```bash
$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
...
