#!/usr/bin/node

let arguments = process.argv.slice(2);
if (arguments.length == 1) {
        console.log('Argument found')
    }
    else if (arguments.length == 0) {
        console.log('No argument')
    }
    else {
        console.log('Arguments found')
    }
