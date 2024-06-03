#!/usr/bin/node

const argument = process.argv.length;
console.log(argument === 2 ? 'No argument' : argument === 3 ? 'Argument found' : 'Arguments found');
