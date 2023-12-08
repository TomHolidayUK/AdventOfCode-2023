// order or rank hands based on rules
// bid amount * rank

type ArrayType7 = [string, number][];

const testdata7: ArrayType7 = 
[
['32T3K', 765],
['T55J5', 684],
['KK677', 28],
['KTJJT', 220],
['QQQJA', 483]
]

let fs7 = require('fs');


// Read the content of the file
const filePath7 = './src/Day7/data7.txt';
const fileContent7 = fs7.readFileSync(filePath7, 'utf-8'); // this reads the file synchronously

// const fileContent7 = "some content";
const lines7: string[]  = fileContent7.split('\n');



let newLines = lines7.map( el => el.split(' '))
let newLines2 = newLines.map( el => [el[0], Number(el[1])])

console.log(newLines2)