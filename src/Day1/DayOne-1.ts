const fs = require('fs');
// import { promises as fsPromises } from 'fs';

// Read the content of the file
const filePath = './src/Day1/data.txt';
const fileContent = fs.readFileSync(filePath, 'utf-8'); // this reads the file synchronously



// Split the content into lines
const lines: string[]  = fileContent.split('\n');
module.exports = lines; 


let runningTotal: number = 0



lines.forEach(el => {
    let firstnumberarray = /(\d)/.exec(el)
    let lastnumberarray = /(\d)/.exec(el.split('').reverse().join(''))
    let firstnumber: string = ''
    let lastnumber: string = ''
    
    if (firstnumberarray !== null) {
        firstnumber = firstnumberarray[0];
      } else {
        console.log("No match found");
      }
    
    if (lastnumberarray !== null) {
        lastnumber = lastnumberarray[0];
        } else {
        console.log("No match found");
        }

    runningTotal += parseInt(firstnumber + lastnumber)
})


console.log(runningTotal)

