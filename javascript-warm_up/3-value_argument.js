#!/usr/bin/node
const arguments = process.argv[2]

if (arguments[0] == 0) {
    console.log("No arguments")
}
else {
    console.log(arguments)
}