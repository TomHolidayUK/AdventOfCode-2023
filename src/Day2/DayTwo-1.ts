let fs2 = require('fs');

// Read the content of the file
const filePath2 = './src/Day2/data2.txt';
const fileContent2 = fs2.readFileSync(filePath2, 'utf-8'); // this reads the file synchronously



// Split the content into lines
const lines2: string[]  = fileContent2.split('\n');

// find maximum value of a colour for each game and write this to an object (use regular expressions)
// loop through object and find which ones work for: 12 red cubes, 13 green cubes, and 14 blue cubes

interface GameData {
    Game: number,
    RedMax: number,
    BlueMax: number,
    GreenMax: number
}

let allData: GameData[] = []

// console.log(lines2[99])

lines2.forEach( el => {
    
    let gameNumber: number = 0

    const gameNumberMatch = /(\d+)/.exec(el)
    if (gameNumberMatch) {
        gameNumber = parseInt(gameNumberMatch[0]);
        // console.log(gameNumber)
    }   

    const regexBlue = /\b(\d+) blue\b/g;
    let blueNumbers: number[] = [];
    let matchBlue: RegExpExecArray | null;

    while ((matchBlue = regexBlue.exec(el)) !== null) {
      blueNumbers.push(parseInt(matchBlue[1], 10));
    }

    const regexgreen = /\b(\d+) green\b/g;
    let greenNumbers: number[] = [];
    let matchgreen: RegExpExecArray | null;

    while ((matchgreen = regexgreen.exec(el)) !== null) {
      greenNumbers.push(parseInt(matchgreen[1], 10));
    }

    const regexred = /\b(\d+) red\b/g;
    let redNumbers: number[] = [];
    let matchred: RegExpExecArray | null;

    while ((matchred = regexred.exec(el)) !== null) {
      redNumbers.push(parseInt(matchred[1], 10));
    }

    // console.log('blue:', blueNumbers);
    // console.log('red:', redNumbers);
    // console.log('green:', greenNumbers);

    const redMax: number = Math.max(...redNumbers)
    const blueMax: number = Math.max(...blueNumbers)
    const greenMax: number = Math.max(...greenNumbers)
      
    allData.push({
        Game: gameNumber,
        RedMax: redMax,
        BlueMax: blueMax,
        GreenMax: greenMax,
    })
})

// console.log(allData);
module.exports = allData; 


let total: number = 0

allData.forEach( el => {
    if (el.RedMax <= 12 && el.BlueMax <= 14 && el.GreenMax <= 13) {
        total += el.Game
    }
})

console.log('Total:', total)