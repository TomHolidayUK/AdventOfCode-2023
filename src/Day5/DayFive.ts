let fs5 = require('fs');


// Read the content of the file
const filePath5 = './src/Day5/data5.txt';
const fileContent5 = fs5.readFileSync(filePath5, 'utf-8'); // this reads the file synchronously

// const fileContent5 = "some content";
const lines5: string[]  = fileContent5.split('\n');

// console.log(lines5)

const testdata5: string[] = [
'seeds: 79 14 55 13',

'seed-to-soil map:',
'50 98 2',
'52 50 48',

'soil-to-fertilizer map:',
'0 15 37',
'37 52 2',
'39 0 15',

'fertilizer-to-water map:',
'49 53 8',
'0 11 42',
'42 0 7',
'57 7 4',


'water-to-light map:',
'88 18 7',
'18 25 70',

'light-to-temperature map:',
'45 77 23',
'81 45 19',
'68 64 13',

'temperature-to-humidity map:',
'0 69 1',
'1 0 69',

'humidity-to-location map:',
'60 56 37',
'56 93 4',
]

// 1 - find seed numbers and map numbers
// 2 - write function to do mapping process
// 3 - run mapping process for all stages and seed numbers and find lowest location

// 1
let seedNumbers: number[] = []
let mapNumbers : number[][][] = []

const [before, after] = lines5[0].split(': ')

seedNumbers = after.split(' ').map(Number)

console.log(seedNumbers)

function findMapNumber (low: number, high: number): number[][] {
    let localMapNumber: number[][] = []
    for (let i = low; i <= high; i++) {
        localMapNumber.push(lines5[i].split(' ').map(Number))
    }
    return localMapNumber
}


// testdata5 values
mapNumbers.push(findMapNumber(3,9))
mapNumbers.push(findMapNumber(12,57))
mapNumbers.push(findMapNumber(60,108))
mapNumbers.push(findMapNumber(111,133))
mapNumbers.push(findMapNumber(136,181))
mapNumbers.push(findMapNumber(184,199))
mapNumbers.push(findMapNumber(202,225))

// lines5 values
// mapNumbers.push(findMapNumber(2,3))
// mapNumbers.push(findMapNumber(5,7))
// mapNumbers.push(findMapNumber(9,12))
// mapNumbers.push(findMapNumber(14,15))
// mapNumbers.push(findMapNumber(17,19))
// mapNumbers.push(findMapNumber(21,22))
// mapNumbers.push(findMapNumber(24,25))

// console.log(mapNumbers)

// 2

// destination range start | source range start | range length

// source range = source range start - source range start + range length 
// destination range = destination range start - destination range start + range length 

// if value is between (source range start) and (source range start + range length) then it maps to number + (destination range start - source range start)
// if value is between (source range start) and (source range end) then it maps to number + (differentiator)


function mapping (allMappingNumbers: number[][], inputNumbers: number[]): number[] {
    let mapDetails: number [][] = []
    for (let i = 0; i < allMappingNumbers.length; i++) {
        let start: number = allMappingNumbers[i][1]
        let end: number = allMappingNumbers[i][1] + allMappingNumbers[i][2]
        let differentiator: number = allMappingNumbers[i][0] - allMappingNumbers[i][1]
        let mapDetail: number[] = [start, end, differentiator]
        mapDetails.push(mapDetail)
    }
    // console.log(mapDetails)
    let outputNumbers = inputNumbers.map( el => {
        for (let j = 0; j < mapDetails.length; j++) {
            if (mapDetails[j][0] <= el && el < mapDetails[j][1]) {
                // console.log(`edit: ${el}`)
                el = el + mapDetails[j][2]
                // console.log(el)
                return el
            } 
        }
        return el
    })

    return outputNumbers
}

// 3

let output: number[] = mapping(mapNumbers[0], seedNumbers)
// console.log(output)
let output2: number[] = mapping(mapNumbers[1], output)
// console.log(output2)
let output3: number[] = mapping(mapNumbers[2], output2)
// console.log(output3)
let output4: number[] = mapping(mapNumbers[3], output3)
// console.log(output4)
let output5: number[] = mapping(mapNumbers[4], output4)
// console.log(output5)
let output6: number[] = mapping(mapNumbers[5], output5)
// console.log(output6)
let output7: number[] = mapping(mapNumbers[6], output6)
console.log(output7)

let lowestLocationNumber: number = Math.min(...output7)
console.log(lowestLocationNumber)


// PART 2


// let highestSeedNumber: number = Math.max(...seedNumbers)
// console.log(highestSeedNumber)
// highestSeedNumber = 4116455504

// create array of all seed numbers from the ranges given
// run these through the functions created earlier


function mappingSingle (allMappingNumbers: number[][], inputNumber: number): number {
    let mapDetails: number [][] = []
    for (let i = 0; i < allMappingNumbers.length; i++) {
        let start: number = allMappingNumbers[i][1]
        let end: number = allMappingNumbers[i][1] + allMappingNumbers[i][2]
        let differentiator: number = allMappingNumbers[i][0] - allMappingNumbers[i][1]
        let mapDetail: number[] = [start, end, differentiator]
        mapDetails.push(mapDetail)
    }
    // console.log(mapDetails)
    let outputNumber: number = 0;
        for (let j = 0; j < mapDetails.length; j++) {
            if (mapDetails[j][0] <= inputNumber && inputNumber < mapDetails[j][1]) {
                // console.log(`edit: ${inputNumber}`)
                outputNumber = inputNumber + mapDetails[j][2]
                // console.log(inputNumber)
                return outputNumber
            } 
        }
        return inputNumber


    return outputNumber
}

let part2SeedNumbers: number[][] = []
let ranges: number[] = []
let times: number[] = []

for (let i = 0; i < seedNumbers.length; i+=2) {
    // let rangeStart: number = seedNumbers[i]
    // let rangeLength: number = seedNumbers[i+1]
    // for (let j = rangeStart; j < (rangeStart + rangeLength); j++) {
    //     part2SeedNumbers.push(j)
    // }
    part2SeedNumbers.push([seedNumbers[i], seedNumbers[i+1] + seedNumbers[i]])
    ranges.push(seedNumbers[i+1] / 1000000)
    times.push(((seedNumbers[i+1] / 1000000) * 60) / 411645550)
}

console.log('part2SeedNumbers', part2SeedNumbers)
console.log('ranges', ranges)
// console.log('times', times)


// -----------------------------------------------------

function findLowestValue(start: number, end: number): number {
    let lowestValue = Infinity; // Initialize with positive infinity as a placeholder

    for (let i = start; i <= end; i++) {
        let currentResult = yourFunctionToEvaluate(i); // Replace with your actual function
        // Check if the current result is lower than the current lowest value
        if (currentResult < lowestValue) {
            lowestValue = currentResult;
        }
    }

    return lowestValue;
}

// Example function to replace with your actual function
function yourFunctionToEvaluate(x: number): number {

    if (x % 10000000 === 0) {
        console.log(x)
    }

    let outputPart2_: number = mappingSingle(mapNumbers[0], x)
    // console.log(outputPart2_)
    let outputPart2_2: number = mappingSingle(mapNumbers[1], outputPart2_)
    // console.log(outputPart2_2)
    let outputPart2_3: number = mappingSingle(mapNumbers[2], outputPart2_2)
    // console.log(outputPart2_3)
    let outputPart2_4: number = mappingSingle(mapNumbers[3], outputPart2_3)
    // console.log(outputPart2_4)
    let outputPart2_5: number = mappingSingle(mapNumbers[4], outputPart2_4)
    // console.log(outputPart2_5)
    let outputPart2_6: number = mappingSingle(mapNumbers[5], outputPart2_5)
    // console.log(outputPart2_6)
    let outputPart2_7: number = mappingSingle(mapNumbers[6], outputPart2_6)
    // console.log(outputPart2_7)

    return outputPart2_7
    // let y: number = (x**2) - (5*x) + 3;
    // return y // Example: Squaring the input
}

// Example usage
console.log('start:', seedNumbers[4])
console.log('end:', seedNumbers[4] + seedNumbers[5])
let result = findLowestValue(seedNumbers[4], seedNumbers[5] + seedNumbers[4]);
console.log('start:', seedNumbers[4])
console.log('end:', seedNumbers[4] + seedNumbers[5])
console.log(result);


// speed = 70 / 10000000 = 411645550 iterations per second
// for section 0:
// for section 2: (682397438 - 712763395) =   12634632 (correct )
// for section 4: (665754577 - 678916875) = 415304203
// for section 5: (2687187253 - 2762178631) = 51752125 (too high)
// for section 6: (1782124901 - 1785315398) = 2540730089
// for section 8: (4116455504 - 4204263894) = 56017390 
// for section 9: (2403629707 - 2470222105) = 177537444


// -----------------------------------------------------

// function* generateRange(start: number, end: number) {
//     for (let i = start; i <= end; i++) {
//       yield i;
//     }
//   }
  
//   let part2SeedNumbers = [];
  
//   for (let i = 0; i < 2; i += 2) {
//     let rangeStart = seedNumbers[i];
//     let rangeLength = seedNumbers[i + 1];
//     let rangeEnd = rangeStart + rangeLength
  
//     part2SeedNumbers.push(...generateRange(rangeStart, rangeEnd));
//   }
  
//   console.log(part2SeedNumbers);

//   let rangeStart = seedNumbers[0];
//   let rangeLength = seedNumbers[1];
//   let rangeEnd = rangeStart + rangeLength

//   for (const value of generateRange(rangeStart, rangeEnd)) {
//     // Do something with each value
//     console.log(value);
// }

// let outputPart2_: number[] = mapping(mapNumbers[0], part2SeedNumbers)
// console.log(outputPart2_)
// let outputPart2_2: number[] = mapping(mapNumbers[1], outputPart2_)
// console.log(outputPart2_2)
// let outputPart2_3: number[] = mapping(mapNumbers[2], outputPart2_2)
// console.log(outputPart2_3)
// let outputPart2_4: number[] = mapping(mapNumbers[3], outputPart2_3)
// console.log(outputPart2_4)
// let outputPart2_5: number[] = mapping(mapNumbers[4], outputPart2_4)
// console.log(outputPart2_5)
// let outputPart2_6: number[] = mapping(mapNumbers[5], outputPart2_5)
// console.log(outputPart2_6)
// let outputPart2_7: number[] = mapping(mapNumbers[6], outputPart2_6)
// console.log(outputPart2_7)

// let lowestLocationNumberPart2: number = Math.min(...outputPart2_7)
// console.log(lowestLocationNumberPart2)

