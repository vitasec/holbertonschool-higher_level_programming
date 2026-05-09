#!/usr/bin/node
const value = process.argv.slice(2)
  .sort(function (a, b) { return b - a; });

if (value.length > 1) {
  console.log(value[1]);
} else {
  console.log(0);
}
