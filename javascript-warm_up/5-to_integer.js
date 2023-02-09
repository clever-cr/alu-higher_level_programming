#!/usr/bin/node
const argument = process.argv[2];
if (isNaN(arg)) {
    console.log('Not a number');
} else {
    console.log('My number: ' + argument);
}