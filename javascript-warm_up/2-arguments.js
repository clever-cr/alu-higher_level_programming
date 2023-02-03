#!/usr/bin/node
function ar() {
    if (arguments.length == 1) {
        console.log("Argument found")
    }
    else if (arguments.length == 0) {
        console.log("No argument")
    }
    else {
        console.log("Arguments found")
    }
}