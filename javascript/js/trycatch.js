'use strict';

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.trim().split('\n').map(string => {
        return string.trim();
    });
    
    main();    
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the reverseString function
 * Use console.log() to print to stdout.
 */
function reverseString(s) {

    try {
        let s_new = s.split('');
        let s_new_rev = s_new.reverse();
        let s_return = s_new_rev.join('');

        console.log(s_return);
    }
    catch(error) {
        console.log('s.split is not a function');
        console.log(s);
    }
}


function main() {
    const s = eval(readLine());
    
    reverseString(s);
}