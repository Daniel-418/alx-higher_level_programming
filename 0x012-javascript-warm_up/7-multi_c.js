#!/usr/bin/node
const args = process.argv.slice(2);
const times  = Number(args[0]);

if (!isNaN(times)) {
  for (let i = 0; i < times; i++) {
    console.log('C is fun');
  }
}
else {
  console.log('Missing number of occurrences');
}
