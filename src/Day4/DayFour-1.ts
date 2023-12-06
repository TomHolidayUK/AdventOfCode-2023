let fs4 = require('fs');


// Read the content of the file
const filePath4 = './src/Day4/data4.txt';
const fileContent4 = fs4.readFileSync(filePath4, 'utf-8'); // this reads the file synchronously

const lines4: string[]  = fileContent4.split('\n');

// read data and create array of winning numbers and personal numbers
// find how many numbers match

const testdata4: string[] = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'
    ]


// console.log(lines4)

let allNumberData: number[][][] = []
let part2Data: number[][] = []

let split1_1: string[] = []
let split1_2: string[] = []


lines4.forEach( (element: string)  => {
    const [before, after] = element.split(' | ');

    split1_1.push(before);
    split1_2.push(after);
})

// console.log(split1_1) 
// console.log(split1_2)

let split2_1: string[] = []

split1_1.forEach( (element: string)  => {
    const [before, after] = element.split(': ');

    split2_1.push(after);
})

// console.log(split2_1)

// split1_2 =  personal numbers
// split2_1 = winning numbers


for (let i = 0; i < split2_1.length; i++) {
    let personalNumbers: number[] = split1_2[i].split(' ').map(Number).filter(num => num !== 0)
    let winningNumbers: number[] = split2_1[i].split(' ').map(Number).filter(num => num !== 0)
    allNumberData.push([[...winningNumbers], [...personalNumbers]])
}

// console.log(split1_2);
console.log(allNumberData);

let sumOfPoints: number = 0

for (let i = 0; i < allNumberData.length; i++) {
    let winningNumbers: number[] = allNumberData[i][0]
    let personalNumbers: number[] = allNumberData[i][1]
    let matches: number = 0
    // let totalPoints: number = 0
    for (let j = 0; j < winningNumbers.length; j++) {
        if (personalNumbers.includes(winningNumbers[j])) {
            matches++
        }
    }
    let totalPoints = (matches === 0) ? 0 : Math.pow(2, matches - 1)
    sumOfPoints += totalPoints
    console.log(`Game ${i+1}: ${matches} matches and ${totalPoints} points`)
    part2Data.push([1, matches])
}

console.log(`Total points: ${sumOfPoints}`)

// -------------------------------------------PART 2------------------------------------------------

// 1 - find number of matching number for each card
// 2 - have an array that captures how many instances there are of each card
// 3 - as you go through the cards and find how many matches it has, update the number of each card
// 4 - when going to a new card, first read how many instances there are of that card
// 5 - sum total number of cards/instances

// 1 + 2
// make array of [copies, matches] = part2Data
console.log(part2Data)

// 3 

for (let i = 0; i < part2Data.length; i++) { // loop through all cards
    // copies = part2Data[i][0]
    let matches: number = part2Data[i][1]
    for (let j = i + 1 ; j < i + 1 + matches; j++) { // for each card add 1 copies to the following n cards, n = matches  
        for (let k = 0; k < part2Data[i][0]; k++) {
        // console.log(`Card ${i + 1} has ${matches} matches. This process should be done ${part2Data[i][0]} times`)
        part2Data[j][0]++
        }
    }
}

console.log(part2Data)

const finalTotal: number = part2Data.reduce((acculmulator, data) => acculmulator + data[0], 0)
console.log(finalTotal)



