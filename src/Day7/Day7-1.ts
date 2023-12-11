// order or rank hands based on rules
// bid amount * rank


const testdata7: [string, number][] = 
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

let newLines: string[][] = lines7.map( el => el.split(' '))
let newLines2: [string, number][] = newLines.map( el => [el[0], Number(el[1])])

console.log(newLines2)

// PLAN 
// apply quick sort algorithm:
// select as element roughly in the middle to be the pivot
// rearrange so elements less than the pivot go to the left and ones higher go to the right 
// then recursively do this again on the sub arrays, picking a new pivot
// recursion ends when the sub array has zero or one elements and the arrya will be sorted 


function quickSortNumber(arr: number[]): number[] {
    if (arr.length <= 1) {
        return arr;
    }

    const pivot = arr[Math.floor(arr.length / 2)];
    const left = arr.filter(element => element < pivot);
    const middle = arr.filter(element => element === pivot);
    const right = arr.filter(element => element > pivot);
    return quickSortNumber(left).concat(middle, quickSortNumber(right));
}

const unsortedArrayNumbers = [42, 15, 7, 29, 53, 18, 66, 2, 37, 94, 61, 25, 80, 5, 49, 12, 33, 77, 51, 23];
const sortedArrayNumbers = quickSortNumber(unsortedArrayNumbers);

console.log("Unsorted Array Numbers:", unsortedArrayNumbers);
console.log("Sorted Array Numbers:", sortedArrayNumbers);


// write a function that compares two cards and decides if one is higher than the other



function cardCompare(pivot: string, cardToCompare: string): boolean {
    let cardScore: number = scoreCalculator(cardToCompare)
    let pivotScore: number = scoreCalculator(pivot)

    function scoreCalculator(card: string): number {
        if (findMaxCharCounts(card)[0] === 5) { // five of a kind
            return 7
        } else if (findMaxCharCounts(card)[0] === 4) { // four of a kind
            return 6
        } else if ((findMaxCharCounts(card)[0] === 3) && (findMaxCharCounts(card)[1] === 2)) { // full house
            return 5
        } else if ((findMaxCharCounts(card)[0] === 3) && (findMaxCharCounts(card)[1] === 1)) { // three of a kind
            return 4
        } else if ((findMaxCharCounts(card)[0] === 2) && (findMaxCharCounts(card)[1] === 2)) { // two pair
            return 3
        } else if ((findMaxCharCounts(card)[0] === 2) && (findMaxCharCounts(card)[1] === 1)) { // two pair
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
        return compareCardsWithSameType(pivotCards,cardsCards)
    }

    return false

}

console.log(cardCompare('AA8AA', 'QQQQ3'))


function compareCardsWithSameType(pivot: string[], cardToCompare: string[]): boolean {

    const cardValues: Record<string, number> = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'J': 11,
        'T': 10,
        '9': 9,
        '8': 8,
        '7': 7,
        '6': 6,
        '5': 5,
        '4': 4,
        '3': 3,
        '2': 2,
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





function findMaxCharCounts(str: string): [number, number] {
    const charCount: { [key: string]: number } = {};

    // Count the frequency of each character
    for (const char of str) {
        charCount[char] = (charCount[char] || 0) + 1;
    }

    // Sort characters by frequency in descending order
    const sortedChars = Object.keys(charCount).sort((a, b) => charCount[b] - charCount[a]);

    // Return the counts of the top two characters
    const topTwoCounts: [number, number] = [
        charCount[sortedChars[0]] || 0,
        charCount[sortedChars[1]] || 0,
    ];

    return topTwoCounts;
}

function quickSortCards(arr: [string, number][]): [string, number][] {
    if (arr.length <= 1) {
        return arr;
    }

    const pivotIndex = Math.floor(arr.length / 2);
    const pivot = arr[pivotIndex];
    // need to not include pivot element in subarrays otherwise it will iterate infinitely
    const left = arr.filter((element, index) => index !== pivotIndex && cardCompare(pivot[0], element[0]) === false);
    const right = arr.filter((element, index) => index !== pivotIndex && cardCompare(pivot[0], element[0]) === true);
    // console.log('left', left)
    // console.log('right', right)
    return [...quickSortCards(left), pivot, ...quickSortCards(right)];
}

const sortedArray = quickSortCards(newLines2);
console.log("Sorted Array Cards:", sortedArray);

const finalScore: number = sortedArray.reduce((acc, el, index) => acc + (el[1] * (index + 1)), 0)
console.log(finalScore)
