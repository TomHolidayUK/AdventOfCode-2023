// read data - save instructions and network details seperately
// start at AAA and follow instructions, record the number of steps taken, if end result is ZZZ return the number of steps

let fs8 = require('fs');


// Read the content of the file
const filePath8 = './src/Day8/data8.txt';
const fileContent8 = fs8.readFileSync(filePath8, 'utf-8'); // this reads the file synchronously

// const fileContent7 = "some content";
const lined_data8: string[]  = fileContent8.split('\n');

const instructions: string[] = lined_data8[0].split('')
console.log(instructions)

// const networkDetails: string[] = lined_data8.slice(2,9)
// const networkDetails: string[] = lined_data8.slice(2,5)
const networkDetails: string[] = lined_data8.slice(2,800)

type NetworkObject = Record<string, string[]>;

const networkObject: NetworkObject= {};

networkDetails.forEach(data => {
  const [key, values] = data.split(' = ');
  const parsedValues = values
    .replace(/^\(|\)$/g, '') // Remove parentheses
    .split(', ')
    .map(val => val.trim());
    networkObject[key] = parsedValues;
});

console.log(networkObject);

let stepNumber: number = 0 // count the nuber of steps

function runInstructions(instructions: string[], network: NetworkObject, step: string): number {

let currentStep: string = step
let nextStep: string = '' // the next element bases on the left right instructions

for (let i = 0; i < instructions.length; i++) {
    console.log(`current step: ${currentStep}, total steps: ${stepNumber}`)
    if (instructions[i] === 'L') {
        // console.log(network.currentStep)
        nextStep = networkObject[currentStep][0]
        stepNumber++
    } else if (instructions[i] === 'R') {
        nextStep = networkObject[currentStep][1]
        stepNumber++
    }

    currentStep = nextStep
    
}
console.log(currentStep)
if (currentStep === 'ZZZ') {
    return stepNumber
} else {
    return runInstructions(instructions, networkObject, currentStep)
}

}


// while current step is no 'ZZZ' step through instructions 

console.log(runInstructions(instructions, networkObject, 'AAA'))




