let fs8_2 = require('fs');


// Read the content of the file
const filePath8_2 = './src/Day8/data8.txt';
const fileContent8_2 = fs8_2.readFileSync(filePath8_2, 'utf-8'); // this reads the file synchronously

// const fileContent7 = "some content";
const lined_data8_2: string[]  = fileContent8_2.split('\n');

const instructions_2: string[] = lined_data8_2[0].split('')
// console.log(instructions_2)

// const networkDetails_2: string[] = lined_data8_2.slice(2,9)
// const networkDetails_2: string[] = lined_data8_2.slice(2,5)
// const networkDetails_2: string[] = lined_data8_2.slice(2,10)
const networkDetails_2: string[] = lined_data8_2.slice(2,800)


type NetworkObject_2 = Record<string, string[]>;

const networkObject_2: NetworkObject_2= {};

networkDetails_2.forEach(data => {
  const [key, values] = data.split(' = ');
  const parsedValues = values
    .replace(/^\(|\)$/g, '') // Remove parentheses
    .split(', ')
    .map(val => val.trim());
    networkObject_2[key] = parsedValues;
});

// console.log(networkObject_2);

let stepNumber_2: number = 0 // count the nuber of steps

// find starting nodes

let startingNodes: string[] = []

// Loop through the networkObject
Object.entries(networkObject_2).forEach(([key]) => {
    if (key.split('')[2] === 'A') {
        startingNodes.push(key)
    }
});

console.log('starting nodes', startingNodes)

let currentNode: string = ''

function runInstructions_2(step: string): number {

    let currentNode: string = step
    let nextStep: string = '' // the next element bases on the left right instructions
    
    for (let i = 0; i < instructions_2.length; i++) {
        console.log(`current step: ${currentNode}, total steps: ${stepNumber_2}`)
        if (instructions_2[i] === 'L') {
            // console.log(network.currentNode)
            nextStep = networkObject_2[currentNode][0]
            stepNumber_2++
        } else if (instructions_2[i] === 'R') {
            nextStep = networkObject_2[currentNode][1]
            stepNumber_2++
        }
    
        currentNode = nextStep

        if (ZCheck(currentNode)) {
            return stepNumber_2
        }
        
    }
    console.log(currentNode)
    if (ZCheck(currentNode)) {
        return stepNumber_2
    } else {
        return runInstructions_2(currentNode)
    }
    
    }


console.log(runInstructions_2(startingNodes[0]))


function ZCheck (input: string): boolean {
    return (input[2] === 'Z');
}

// run to find how many steps it takeseach starting node to get to a node that ends in Z
// then find the LCM of these numbers

// [ 'AAA', 'XDA', 'XSA', 'CFA', 'HJA', 'HPA' ]
// AAA - 21409 (ZZZ)
// XDA - 14363 (MPZ)
// XSA - 15989 (FNZ)
// CFA - 16531 (BQZ)
// HJA - 19241 (RSZ)
// HPA - 19783 (XXZ)


// Now find Lowest Common Multiple (LCM)
[21409, 14363, 15989, 16531, 19241, 19783]

function findLCM(array: number[]): number {
    // (x / all elements of array) % 1 === 0
    let x: number = 21409;


    let solutionFound: boolean = false


    while (!solutionFound) {
        x+=21409
        let divisions: number[] = array.map(el => x / el)
        // console.log(divisions)
        let check: boolean = divisions.every(el => el % 1 === 0)
        if (check) {
            solutionFound = true
        }
    }

    return x
}

console.log(findLCM([21409, 14363, 15989, 16531, 19241, 19783]))
// console.log(findLCM([6, 7, 21]))


// Final answer: 21165830176709

// function tryIfFails(start: string) {
//     try {
//         return runInstructions_2(start)
//     } catch (error) {
//         if (error instanceof RangeError && error.message.includes('Maximum call stack size exceeded')) {
//         // console.log('error', error)
//         console.log(stepNumber_2)
//         console.log(currentNodes)
//         return tryIfFails(currentNodes)
//         } else {
//             // throw error
//             console.log(error)
//         }
//     }
// }

// console.log(tryIfFails(startingNodes[0]))

