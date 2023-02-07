#!/usr/bin/node
const arguments = process.argv[2]

if (arguments[0] === undefined) {
    console.log("No arguments")
}
else {
    console.log(arguments)
}