#!/usr/bin/node

const inputVal = Math.floor(Number(process.argv[2]));
console.log(isNaN(inputVal) ? 'Not a number' : `My number: ${inputVal}`);
