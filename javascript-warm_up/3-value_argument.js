#!/usr/bin/node
const arguments = process.argv.slice(2)

if (arguments[0] === undefined) {
    console.log("No arguments")
}
else {
    console.log(arguments)
}