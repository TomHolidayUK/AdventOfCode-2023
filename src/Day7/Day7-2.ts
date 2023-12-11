
const testdata7_2: [string, number][] = 
[
    ['32T3K', 765],
    ['T55J5', 684],
    ['KK677', 28],
    ['JJJQT', 220],
    ['QQQJA', 483]
]

let fs7_2 = require('fs');


// Read the content of the file
const filePath7_2 = './src/Day7/data7.txt';
const fileContent7_2 = fs7_2.readFileSync(filePath7_2, 'utf-8'); // this reads the file synchronously

// const fileContent7 = "some content";
const lines7_2: string[]  = fileContent7_2.split('\n');

let newLines_2: string[][] = lines7_2.map( el => el.split(' '))
let newLines2_2: [string, number][] = newLines_2.map( el => [el[0], Number(el[1])])

// console.log(newLines2_2)

// PLAN 
// apply quick sort algorithm:
// select as element roughly in the middle to be the pivot
// rearrange so elements less than the pivot go to the left and ones higher go to the right 
// then recursively do this again on the sub arrays, picking a new pivot
// recursion ends when the sub array has zero or one elements and the arrya will be sorted 




function cardCompare2(pivot: string, cardToCompare: string): boolean {
    let cardScore: number = scoreCalculator2(cardToCompare)
    let pivotScore: number = scoreCalculator2(pivot)

    

    function scoreCalculator2(card: string): number {

        // add amount of jokers to the number of the most frequent card

        const jokerFrequency: number = findMaxCharCounts2(card)[2]
        const highestFrequency: number = findMaxCharCounts2(card)[0]
        const secondHighestFrequency: number = findMaxCharCounts2(card)[1]

        // problems when the highest frquency is for 'J' because then it is being counted twice 

        if ((highestFrequency + jokerFrequency) >= 5) { // five of a kind
            return 7
        } else if ((highestFrequency + jokerFrequency) === 4) { // four of a kind
            return 6
        } else if (((highestFrequency + jokerFrequency) === 3) && (secondHighestFrequency === 2)) { // full house
            return 5
        } else if (((highestFrequency + jokerFrequency) === 3) && (secondHighestFrequency === 1)) { // three of a kind
            return 4
        } else if (((highestFrequency + jokerFrequency) === 2) && (secondHighestFrequency === 2)) { // two pair
            return 3
        } else if (((highestFrequency + jokerFrequency) === 2) && (secondHighestFrequency === 1)) { // one pair
            return 2
        } else {
            return 1
        }
    }

    if (cardScore > pivotScore) {
        console.log('card 2 has stronger type')
        return true
    } else if (cardScore < pivotScore) {
        console.log('card 2 has weaker type')
        return false
    } else if (cardScore === pivotScore) {
        const pivotCards: string[] = pivot.split('')
        const cardsCards: string[] = cardToCompare.split('')
        return compareCardsWithSameType2(pivotCards,cardsCards)
    }

    return false

}

console.log(cardCompare2('AA8AA', 'QJJQ2'))


function compareCardsWithSameType2(pivot: string[], cardToCompare: string[]): boolean {

    const cardValues: Record<string, number> = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
        'J': 1,
    };
    for (let i = 0; i < 5; i++) {
        const pivotValue: number = cardValues[pivot[i]];
        const cardValue: number = cardValues[cardToCompare[i]];

    if (cardValue > pivotValue) {
        console.log('cards have equal type but card 2 is stronger')
        return true; 
    } else if (cardValue < pivotValue) {
        console.log('cards have equal type but card 2 is weaker')
        return false; 
    } 
}
return false
}





function findMaxCharCounts2(str: string): number[] {

    // remove Jokers
    // console.log('test', str.split('').filter(el => el !== 'J').join(''))
    const jokerNumber: number = str.split('').reduce((acc, el) => {
        return (el === 'J') ? acc + 1 : acc;
        
    }, 0)
    const stringWithoutJokers: string = str.split('').filter(el => el !== 'J').join('')

    const charCount: { [key: string]: number } = {};

    // Count the frequency of each character
    for (const char of stringWithoutJokers) {
        charCount[char] = (charCount[char] || 0) + 1;
    }
    
    // Sort characters by frequency in descending order
    const sortedChars = Object.keys(charCount).sort((a, b) => charCount[b] - charCount[a]);

    // Return the counts of the top two characters
    const topTwoCounts: number[] = [
        charCount[sortedChars[0]] || 0,
        charCount[sortedChars[1]] || 0,
    ];

    // Also find how many jokers there are
    // let jokerNumber: number = 0

    // let searchCriteria: string = "J"
    // if (charCount[searchCriteria]) {
    //     // console.log(charCount[searchCriteria])
    //     jokerNumber = charCount[searchCriteria]
    // } else 
    // jokerNumber = 0

    let countsWithJoker: number[] = topTwoCounts.concat(jokerNumber)
    console.log(countsWithJoker)
    return countsWithJoker;
}

function quickSortCards2(arr: [string, number][]): [string, number][] {
    if (arr.length <= 1) {
        return arr;
    }

    const pivotIndex = Math.floor(arr.length / 2);
    const pivot = arr[pivotIndex];
    // need to not include pivot element in subarrays otherwise it will iterate infinitely
    const left = arr.filter((element, index) => index !== pivotIndex && cardCompare2(pivot[0], element[0]) === false);
    const right = arr.filter((element, index) => index !== pivotIndex && cardCompare2(pivot[0], element[0]) === true);
    // console.log('left', left)
    // console.log('right', right)
    return [...quickSortCards2(left), pivot, ...quickSortCards2(right)];
}

const sortedArray_2 = quickSortCards2(newLines2_2);
console.log("Sorted Array Cards:", sortedArray_2);

let reversedLines2_2: string[] = sortedArray_2.map(([str, num]) => `${str} ${num}`);
let reversedContent7_2: string = reversedLines2_2.join('\n');

fs7_2.writeFile('sorted_data.txt', reversedContent7_2, (err: any) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log('File has been written successfully.');
});

const finalScore_2: number = sortedArray_2.reduce((acc, el, index) => acc + (el[1] * (index + 1)), 0)
console.log(finalScore_2)
