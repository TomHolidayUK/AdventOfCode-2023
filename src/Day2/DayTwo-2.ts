let data3 = require('./DayTwo-1.ts');

let totalpower2: number = 0

interface GameData {
    Game: number,
    RedMax: number,
    BlueMax: number,
    GreenMax: number
}

data3.forEach( (element: GameData)  => {     
    const totalmax = element.RedMax * element.BlueMax * element.GreenMax
    totalpower2 += totalmax
})

console.log('Total Powers:', totalpower2)