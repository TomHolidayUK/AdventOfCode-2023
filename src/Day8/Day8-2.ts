// read data - save instructions and network details seperately
// start at AAA and follow instructions, record the number of steps taken, if end result is ZZZ return the number of steps

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

const networkObject_2: NetworkObject_2= {
    // '11A': [ '11B', 'XXX' ],
    // '11B': [ 'XXX', '11Z' ],
    // '11Z': [ '11B', 'XXX' ],
    // '22A': [ '22B', 'XXX' ],
    // '22B': [ '22C', '22C' ],
    // '22C': [ '22Z', '22Z' ],
    // '22Z': [ '22B', '22B' ],
    // 'XXX': [ 'XXX', 'XXX' ]
  }

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

function runInstructions_2(starting: string[]): number {

    let currentNodes: string[] = starting // define starting nodes
    let nextNodes: string [] = [] 

    for (let i = 0; i < instructions_2.length; i++) { // run through all instructions
        currentNodes.map((el) => { // map for all nodes 
        // console.log(`current step: ${el}, total steps: ${stepNumber_2}`)
        if (instructions_2[i] === 'L') {
            nextNodes.push(networkObject_2[el][0])
        } else if (instructions_2[i] === 'R') {
            nextNodes.push(networkObject_2[el][1])
        }
        // console.log('next', nextNodes)
        // currentNodes[index] = nextNodes[index]
        // console.log(currentNodes)
        
    })
    currentNodes = nextNodes
    // console.log('next', nextNodes)
    nextNodes = []
    stepNumber_2++
    if (stepNumber_2 % 100000 === 0) {
        console.log('stepNumber', stepNumber_2)
    }
    if ((checkCurrentNodes(currentNodes)) ) {
        // console.log('test')
        return stepNumber_2
    }

    }
    // console.log('end of instructions', currentNodes)
    return runInstructions_2(currentNodes)

}

let startingNodes: string[] = []

// Loop through the networkObject
Object.entries(networkObject_2).forEach(([key]) => {
    if (key.split('')[2] === 'A') {
        startingNodes.push(key)
    }
});

// console.log('complete start', startingNodes)


function checkCurrentNodes(currentNodes: string[]) {
    return currentNodes.every((element) => element.split('')[2] === 'Z')
}

// console.log(checkCurrentNodes([ '11Z', '22Z' ]))

console.log(runInstructions_2(startingNodes))

// need to find nodes that end in A to be starting nodes
// finish when all nodes end in Z

// instructions = 271
// endingNodes = [ 'FNZ', 'MPZ', 'BQZ', 'RSZ', 'XXZ', 'ZZZ' ]

// [ 'KVH', 'NGP', 'QNP', 'DBX', 'PRL', 'LXM' ]

