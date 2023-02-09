#!/usr/bin/node
const arguments = process.argv.slice(2);
if (arguments.length <= 1) {
    console.log(0);
} else {
    console.log(arguments.sort((a, b) => b - a)[1]);
}