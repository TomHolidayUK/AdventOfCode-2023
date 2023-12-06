let fs3 = require('fs');
// import * as fs3 from 'fs';

// Read the content of the file
const filePath3 = './src/Day3/data3.txt';
const fileContent3 = fs3.readFileSync(filePath3, 'utf-8'); // this reads the file synchronously


const testdata: string[] = 
[
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..'
]

// Split the content into lines
const lines3: string[]  = fileContent3.split('\n');

let validNumbers: number[] = []

const regexsymbol = /[=*#+$/@&%-]/;

let symbolpresent: boolean = false

for (let i = 0; i < lines3.length; i++) {
    let linelength: number = lines3[i].length

    const regexnumber = /\d+/g; // search for any number
    type MatchExecType = RegExpExecArray | null;
    let match: MatchExecType;


    while ((match = regexnumber.exec(lines3[i])) !== null) {
      console.log("Result:", match[0]); 
      console.log("Index:", match.index);

    const length: number = match[0].length

    function createArrayofAscendingNumbers(n: number, m: number): number[] {
        let result: number[] = [];
        for (let i = n; i <= m; i++) {
        result.push(i);
        }
        return result;
    }

    function aboveCheck(i: number, matchindex: number, matchvalue: string, length: number, linelength: number, symbolpresent: boolean) {
        if ((matchindex === 0) && (regexsymbol.test(lines3[i-1].split('').slice(0, length + 1).join('')))) { // above (if number at start of line)
            // console.log(`symbol present for ${matchvalue} (above)`)
            symbolpresent = true
            validNumbers.push(Number(matchvalue))
        } else if ((0 < matchindex) && (matchindex + length <= linelength) && (symbolpresent === false) && (regexsymbol.test(lines3[i-1].split('').slice(matchindex - 1, matchindex + length + 1).join('')))) { // above
            // console.log(`symbol present for ${matchvalue} (above)`)
            symbolpresent = true
            validNumbers.push(Number(matchvalue))
        } else if ((matchindex + length === linelength) && (regexsymbol.test(lines3[i-1].split('').slice(matchindex - 1, matchindex + length).join(''))) && (symbolpresent === false)) { // above (if number at end of line)
            // console.log(`symbol present for ${matchvalue} (above)`)
            symbolpresent = true
            validNumbers.push(Number(matchvalue))
        }
    }
    function belowCheck(i: number, matchindex: number, matchvalue: string, length: number, linelength: number, symbolpresent: boolean) {
        if ((matchindex === 0) && (regexsymbol.test(lines3[i+1].split('').slice(0, length + 1).join('')))) { // below (if number at start of line)
            // console.log(`symbol present for ${matchvalue} (below)`)
            symbolpresent = true
            validNumbers.push(Number(matchvalue))
        } else if ((0 < matchindex) && (matchindex + length <= linelength) && (regexsymbol.test(lines3[i+1].split('').slice(matchindex - 1, matchindex + length + 1).join(''))) && (symbolpresent === false)) { // below
            // console.log(`symbol present for ${matchvalue} (below)`)
            symbolpresent = true
            validNumbers.push(Number(matchvalue))
        } else if ((matchindex + length === linelength) && (regexsymbol.test(lines3[i+1].split('').slice(matchindex - 1, matchindex + length).join(''))) && (symbolpresent === false)) { // below (if number at end of line)
            // console.log(`symbol present for ${matchvalue} (below)`)
            symbolpresent = true
            validNumbers.push(Number(matchvalue))
        }
    }

    function leftandrightCheck(i: number, matchindex: number, matchvalue: string, length: number, linelength: number, symbolpresent: boolean) {
        if ((matchindex > 0) && (regexsymbol.test(lines3[i].split('')[matchindex - 1])) && (symbolpresent === false)) { // left
            // console.log(`symbol present for ${matchvalue} (left)`)
            symbolpresent = true
            validNumbers.push(Number(matchvalue))
        } else if ((matchindex + length < linelength) && (regexsymbol.test(lines3[i].split('')[matchindex + length ])) && (symbolpresent === false)) { // right
            // console.log(`symbol present for ${matchvalue} (right)`)
            symbolpresent = true
            validNumbers.push(Number(matchvalue))
        }
    }

    if (i === 0) { // for top row
        leftandrightCheck(i, match.index, match[0], length, linelength, symbolpresent)
        belowCheck(i, match.index, match[0], length, linelength, symbolpresent)
    } else if (0 < i && i < lines3.length - 1) { // for middle rows
        aboveCheck(i, match.index, match[0], length, linelength, symbolpresent)
        leftandrightCheck(i, match.index, match[0], length, linelength, symbolpresent)
        belowCheck(i, match.index, match[0], length, linelength, symbolpresent)
    } else if (i === lines3.length - 1) { // for bottom row
        aboveCheck(i, match.index, match[0], length, linelength, symbolpresent)
        leftandrightCheck(i, match.index, match[0], length, linelength, symbolpresent)
    }
    }
   
}

// console.log(validNumbers)

const sum = validNumbers.reduce((a, b) => a + b);
console.log(sum)











