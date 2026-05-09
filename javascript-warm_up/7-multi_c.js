#!/usr/bin/node
const number = parseInt(Number(process.argv[2]));

if (isNaN(number)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < number; i++) {
    console.log('C is fun');
  }
}
