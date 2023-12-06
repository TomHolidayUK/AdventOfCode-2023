let fs3_2 = require('fs');


// Read the content of the file
const filePath3_2 = './src/Day3/data3.txt';
const fileContent3_2 = fs3_2.readFileSync(filePath3_2, 'utf-8'); // this reads the file synchronously

const lines3_2: string[]  = fileContent3_2.split('\n');


// map numbers and their indices (as an array of objects)
// (represent index as single symbol; index + row * 140 )
// search for *, for each one check if it is surrounded by exactly 2 numbers, if so return the indices of these numbers
// for each pair of indices find the relevant number and multiply them 


type MyType = Array<[number, number[]]>;
let numbersandindices: MyType = []


const regexasterisk = /\*/g
const regexnumber2 = /\d+/g;
const regexnumber = /^[0-9]$/;
let indicesToFind:  number[][] = []
let indexRowPairs: number[][] = []

function calculateSingleIndex(i: number, matchindex: number, linelength: number): number {
    return (i * linelength) + matchindex
}


for (let i = 0; i < lines3_2.length; i++) {
    const linelength: number = lines3_2[i].length

    type MatchExecType = RegExpExecArray | null;
    let match: MatchExecType;
    while ((match = regexnumber2.exec(lines3_2[i])) !== null) {
        // console.log("Result:", match[0]); 
        // console.log("Index:", match.index);
        // console.log('i:', i)

        const numberlength: number = match[0].length
    

        function createArrayofAscendingNumbers2(n: number, m: number): number[] {
            let result: number[] = [];
            for (let i = n; i <= m; i++) {
            result.push(i);
            }
            return result;
        }


        const singleDigitIndex: number = calculateSingleIndex(i, match.index, linelength)
        // console.log(singleDigitIndex)
        let indicesofnumbers: number[] = []
        indicesofnumbers.push(...createArrayofAscendingNumbers2(singleDigitIndex, singleDigitIndex + numberlength - 1))
        numbersandindices.push([Number(match[0]), indicesofnumbers])

    }
    
    let match2: MatchExecType;
    
    while ((match2 = regexasterisk.exec(lines3_2[i])) !== null) {
        // console.log("Result:", match2[0]); 
        console.log(`Index: ${match2.index}, Row: ${i}`);
        indexRowPairs.push([match2.index, i])
    
    }
}

console.log(numbersandindices)
console.log('indexRowPairs:', indexRowPairs)

    

function testIfNumber (i: number, matchindex: number ): boolean {
    // console.log('i:', i)
    // console.log('matchindex:', matchindex)
    // console.log('lines3_2[i]:', lines3_2[i].split('')[matchindex])
    // console.log('state', regexnumber.test(lines3_2[i].split('')[matchindex]))
    if (regexnumber.test(lines3_2[i].split('')[matchindex])) {
        return true
    } else {
        return false
    }
}

// iterate through indexRowPairs, for each one check if it is surrounded by exactly 2 numbers, if so return the indices of these numbers
for (let j = 0; j < indexRowPairs.length; j++) {
        const linelength2: number = lines3_2[indexRowPairs[j][1]].length

        let numbersCount: number = 0
        let indexPair: number[] = []
        // console.log('left', lines3_2[indexRowPairs[j][1]].split('')[indexRowPairs[j][0] - 1])
        // console.log('left', regexnumber.test(lines3_2[indexRowPairs[j][1]].split('')[indexRowPairs[j][0] - 1]))
        // console.log('test', testIfNumber(indexRowPairs[j][1], indexRowPairs[j][0] - 1))
        // if (regexnumber.test(lines3_2[indexRowPairs[j][1]].split('')[indexRowPairs[j][0] - 1])) {
        if (testIfNumber(indexRowPairs[j][1], indexRowPairs[j][0] - 1)) { // LEFT
            // console.log('number found left')
            numbersCount += 1
            // console.log('numbersCount', numbersCount)
            indexPair.push(calculateSingleIndex(indexRowPairs[j][1], indexRowPairs[j][0] - 1, linelength2))
        }
        // console.log('right', lines3_2[indexRowPairs[j][1]].split('')[indexRowPairs[j][0] + 1])
        // console.log('right', regexnumber.test(lines3_2[indexRowPairs[j][1]].split('')[indexRowPairs[j][0] + 1]))
        // console.log(indexRowPairs)
        if (testIfNumber(indexRowPairs[j][1], indexRowPairs[j][0] + 1)) { // RIGHT
            // console.log('number found right')
            numbersCount += 1
            // console.log('numbersCount', numbersCount)
            indexPair.push(calculateSingleIndex(indexRowPairs[j][1], indexRowPairs[j][0] + 1, linelength2))
        }

        if (indexRowPairs[j][1] === 0) { // ABOVE
            // console.log('no above')
        } else {
            let arrayabove: string[] = lines3_2[indexRowPairs[j][1] - 1].split('').slice(indexRowPairs[j][0] - 1, indexRowPairs[j][0] + 2 )
            // console.log('arrayabove', arrayabove)
            if ((regexnumber.test(arrayabove[0])) && (regexnumber.test(arrayabove[1])) && ((regexnumber.test(arrayabove[2])))) {
                // console.log('1')
                numbersCount += 1;
                indexPair.push(calculateSingleIndex(indexRowPairs[j][1] - 1, indexRowPairs[j][0] - 1, linelength2))
            } else if ((regexnumber.test(arrayabove[0])) && (!regexnumber.test(arrayabove[1])) && ((regexnumber.test(arrayabove[2])))) {
                // console.log('2')
                numbersCount += 2;
                indexPair.push(calculateSingleIndex(indexRowPairs[j][1] - 1, indexRowPairs[j][0] - 1, linelength2))
                indexPair.push(calculateSingleIndex(indexRowPairs[j][1] - 1, indexRowPairs[j][0] + 1, linelength2))
            } else if ((regexnumber.test(arrayabove[0])) && (regexnumber.test(arrayabove[1])) && ((!regexnumber.test(arrayabove[2])))) {
                // console.log('1')
                numbersCount += 1;
                indexPair.push(calculateSingleIndex(indexRowPairs[j][1] - 1, indexRowPairs[j][0] - 1, linelength2))
            } else if ((!regexnumber.test(arrayabove[0])) && (regexnumber.test(arrayabove[1])) && ((regexnumber.test(arrayabove[2])))) {
                // console.log('1')
                numbersCount += 1;
                indexPair.push(calculateSingleIndex(indexRowPairs[j][1] - 1, indexRowPairs[j][0], linelength2))
            } else if ((!regexnumber.test(arrayabove[0])) && (!regexnumber.test(arrayabove[1])) && ((regexnumber.test(arrayabove[2])))) {
                // console.log('1')
                numbersCount += 1;
                indexPair.push(calculateSingleIndex(indexRowPairs[j][1] - 1, indexRowPairs[j][0] + 1, linelength2))
            } else if ((regexnumber.test(arrayabove[0])) && (!regexnumber.test(arrayabove[1])) && ((!regexnumber.test(arrayabove[2])))) {
                // console.log('1')
                numbersCount += 1;
                indexPair.push(calculateSingleIndex(indexRowPairs[j][1] - 1, indexRowPairs[j][0] - 1, linelength2))
            } else if ((!regexnumber.test(arrayabove[0])) && (regexnumber.test(arrayabove[1])) && ((!regexnumber.test(arrayabove[2])))) {
                // console.log('1')
                numbersCount += 1;
                indexPair.push(calculateSingleIndex(indexRowPairs[j][1] - 1, indexRowPairs[j][0], linelength2))
            } else  {
                // console.log('0')
            }
            // console.log('test1', numbersCount)
        }


        if (indexRowPairs[j][1] === lines3_2.length - 1) { // BELOW
            // console.log('no below')
        } else {
            let arraybelow: string[] = lines3_2[indexRowPairs[j][1] + 1].split('').slice(indexRowPairs[j][0] - 1, indexRowPairs[j][0] + 2 )
            // console.log('arraybelow', arraybelow)
            if ((regexnumber.test(arraybelow[0])) && (regexnumber.test(arraybelow[1])) && ((regexnumber.test(arraybelow[2])))) {
                // console.log('1')
                numbersCount += 1;
                indexPair.push(calculateSingleIndex(indexRowPairs[j][1] + 1, indexRowPairs[j][0] - 1, linelength2))
            } else if ((regexnumber.test(arraybelow[0])) && (!regexnumber.test(arraybelow[1])) && ((regexnumber.test(arraybelow[2])))) {
                // console.log('2')
                numbersCount += 2;
                indexPair.push(calculateSingleIndex(indexRowPairs[j][1] + 1, indexRowPairs[j][0] - 1, linelength2))
                indexPair.push(calculateSingleIndex(indexRowPairs[j][1] + 1, indexRowPairs[j][0] + 1, linelength2))
            } else if ((regexnumber.test(arraybelow[0])) && (regexnumber.test(arraybelow[1])) && ((!regexnumber.test(arraybelow[2])))) {
                // console.log('1')
                numbersCount += 1;
                indexPair.push(calculateSingleIndex(indexRowPairs[j][1] + 1, indexRowPairs[j][0] - 1, linelength2))
            } else if ((!regexnumber.test(arraybelow[0])) && (regexnumber.test(arraybelow[1])) && ((regexnumber.test(arraybelow[2])))) {
                // console.log('1')
                numbersCount += 1;
                indexPair.push(calculateSingleIndex(indexRowPairs[j][1] + 1, indexRowPairs[j][0], linelength2))
            } else if ((!regexnumber.test(arraybelow[0])) && (!regexnumber.test(arraybelow[1])) && ((regexnumber.test(arraybelow[2])))) {
                // console.log('1')
                numbersCount += 1;
                indexPair.push(calculateSingleIndex(indexRowPairs[j][1] + 1, indexRowPairs[j][0] + 1, linelength2))
            } else if ((regexnumber.test(arraybelow[0])) && (!regexnumber.test(arraybelow[1])) && ((!regexnumber.test(arraybelow[2])))) {
                // console.log('1')
                numbersCount += 1;
                indexPair.push(calculateSingleIndex(indexRowPairs[j][1] + 1, indexRowPairs[j][0] - 1, linelength2))
            } else if ((!regexnumber.test(arraybelow[0])) && (regexnumber.test(arraybelow[1])) && ((!regexnumber.test(arraybelow[2])))) {
                // console.log('1')
                console.log('SUCCESS')
                numbersCount += 1;
                indexPair.push(calculateSingleIndex(indexRowPairs[j][1] + 1, indexRowPairs[j][0], linelength2))
            } else  {
                // console.log('0')
            }
            // console.log('test2', numbersCount)
        }
    

    // console.log('numbersCount', numbersCount)
    if (numbersCount === 2) {
        indicesToFind.push(indexPair)
    }


    }


console.log('indicies to find', indicesToFind) // indices of valid numbers
    


function findValuefromIndex (index: number): number {
    return numbersandindices.find(([value, indices]) => indices.includes(index))![0];
}

let products: number[] = []
for (let i = 0; i < indicesToFind.length; i++) {
    products.push(findValuefromIndex(indicesToFind[i][0]) * findValuefromIndex(indicesToFind[i][1]))
    console.log('values to multiply', findValuefromIndex(indicesToFind[i][0]), findValuefromIndex(indicesToFind[i][1]))
}

console.log('products', products)
const sum2 = products.reduce((a, b) => a + b, 0);
console.log(sum2)

