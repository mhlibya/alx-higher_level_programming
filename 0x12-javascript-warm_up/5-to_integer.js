#!/usr/bin/node
const num = Number(process.argv[2]);
console.log(!isNaN(process.argv[2]) ? 'Not a number' : `My number: ${process.argv[2]}`)