// draw perimeter in a .txt file
// make all other data = .
// go through manually and count area inside

let fs10_2 = require('fs');


// Read the content of the file
const filePath10_2 = './src/Day10/perimeterWithDirections.txt';
const fileContent10_2 = fs10_2.readFileSync(filePath10_2, 'utf-8'); // this reads the file synchronously

const lined_data10_2: string[]  = fileContent10_2.split('\n');
const matrix2: string[][]  = lined_data10_2.map(el => el.split(','))
type PositionDirectionValue = [number, number, number, string]
const matrixNumerical: PositionDirectionValue[] = matrix2.map(row => {
    const transformedRow: PositionDirectionValue = [
        Number(row[0]),
        Number(row[1]),
        Number(row[2]),
        row[3]
    ]
    return transformedRow
});
console.log(matrixNumerical)

const matrix_width: number = 140;
const matrix_height: number = 140;

// create matrix of dots
let dots_matrix: string[][] = []
for (let i = 0; i < matrix_height; i++) {
    let dots_row: string[] = [];
    for (let j = 0; j < matrix_width; j++) {
        dots_row.push('.')
    }
    dots_matrix.push(dots_row)
}



// Need to follow the loop/perimeter and add the empty nodes to the left of the line to the node inside the loop
// When adding, need to check that node hasn't already been added

let nodesInsideLoop: number[][] = []



// matrixNumerical.forEach(el => {
//     // console.log(el)
//     // const direction: number = el[2]
//     if (el[2] === 1) {
//         let left_position: number[] = [el[0], el[1] - 1] // check node to the left (depending on current position and direciton)
//         if (!isPartOfLoop(left_position) && !alreadyAdded(left_position)) { // check that it is not part of the loop AND check that it has not already been added to nodesInsideLoop
//             nodesInsideLoop.push(left_position)
//         }
//     } else if (el[2] === 3) {
//         let left_position: number[] = [el[0], el[1] + 1] 
//         if (!isPartOfLoop(left_position) && !alreadyAdded(left_position)) { 
//             nodesInsideLoop.push(left_position)
//         }
//     } else if (el[2] === 2) {
//         let left_position: number[] = [el[0] - 1, el[1]] 
//         if (!isPartOfLoop(left_position) && !alreadyAdded(left_position)) { 
//             nodesInsideLoop.push(left_position)
//         }
//     } else if (el[2] === 4) {
//         let left_position: number[] = [el[0] + 1, el[1]] 
//         if (!isPartOfLoop(left_position) && !alreadyAdded(left_position)) { 
//             nodesInsideLoop.push(left_position)
//         }
//     }
// })

matrixNumerical.forEach(el => {
    // console.log(el)
    // const direction: number = el[2]
    if ((el[2] === 1) && (el[3] !== ' J')) {
        let right_position: number[] = [el[0], el[1] + 1] // check node to the right (depending on current position and direciton)
        if (!isPartOfLoop(right_position) && !alreadyAdded(right_position)) { // check that it is not part of the loop AND check that it has not already been added to nodesInsideLoop
            nodesInsideLoop.push(right_position)
        }
    } else if ((el[2] === 1) && (el[3] === ' J')) {
        let right_position1: number[] = [el[0], el[1] + 1] 
        let right_position2: number[] = [el[0] + 1, el[1]] 
        let right_position3: number[] = [el[0] + 1, el[1] + 1]
        if (!isPartOfLoop(right_position1) && !alreadyAdded(right_position1)) { 
            nodesInsideLoop.push(right_position1)
        }
        if (!isPartOfLoop(right_position2) && !alreadyAdded(right_position2)) { 
            nodesInsideLoop.push(right_position2)
        }
        if (!isPartOfLoop(right_position3) && !alreadyAdded(right_position3)) { 
            nodesInsideLoop.push(right_position3)
        }
    } else if ((el[2] === 3) && (el[3] !== ' F')) {
        let right_position: number[] = [el[0], el[1] - 1] 
        if (!isPartOfLoop(right_position) && !alreadyAdded(right_position)) { 
            nodesInsideLoop.push(right_position)
        }
    } else if ((el[2] === 3) && (el[3] === ' F')) {
        let right_position1: number[] = [el[0], el[1] - 1] 
        let right_position2: number[] = [el[0] - 1, el[1]] 
        let right_position3: number[] = [el[0] - 1, el[1] - 1]
        if (!isPartOfLoop(right_position1) && !alreadyAdded(right_position1)) { 
            nodesInsideLoop.push(right_position1)
        }
        if (!isPartOfLoop(right_position2) && !alreadyAdded(right_position2)) { 
            nodesInsideLoop.push(right_position2)
        }
        if (!isPartOfLoop(right_position3) && !alreadyAdded(right_position3)) { 
            nodesInsideLoop.push(right_position3)
        }
    }
    else if ((el[2] === 2) && (el[3] !== ' L')) {
        let right_position: number[] = [el[0] + 1, el[1]] 
        if (!isPartOfLoop(right_position) && !alreadyAdded(right_position)) { 
            nodesInsideLoop.push(right_position)
        }
    } else if ((el[2] === 2) && (el[3] === ' L')) {
        let right_position1: number[] = [el[0] + 1, el[1]] 
        let right_position2: number[] = [el[0], el[1] - 1] 
        let right_position3: number[] = [el[0] + 1, el[1] - 1]
        if (!isPartOfLoop(right_position1) && !alreadyAdded(right_position1)) { 
            nodesInsideLoop.push(right_position1)
        }
        if (!isPartOfLoop(right_position2) && !alreadyAdded(right_position2)) { 
            nodesInsideLoop.push(right_position2)
        }
        if (!isPartOfLoop(right_position3) && !alreadyAdded(right_position3)) { 
            nodesInsideLoop.push(right_position3)
        }
    } else if ((el[2] === 4) && (el[3] !== ' 7')) {
        let right_position: number[] = [el[0] - 1, el[1]] 
        if (!isPartOfLoop(right_position) && !alreadyAdded(right_position)) { 
            nodesInsideLoop.push(right_position)
        }
    } else if ((el[2] === 4) && (el[3] === ' 7')) {
        let right_position1: number[] = [el[0] - 1, el[1]] 
        let right_position2: number[] = [el[0], el[1] + 1] 
        let right_position3: number[] = [el[0] - 1, el[1] + 1]
        if (!isPartOfLoop(right_position1) && !alreadyAdded(right_position1)) { 
            nodesInsideLoop.push(right_position1)
        }
        if (!isPartOfLoop(right_position2) && !alreadyAdded(right_position2)) { 
            nodesInsideLoop.push(right_position2)
        }
        if (!isPartOfLoop(right_position3) && !alreadyAdded(right_position3)) { 
            nodesInsideLoop.push(right_position3)
        }
    }
})

function isPartOfLoop(position_to_check: number[]): boolean {
    const isPartOfLoop = matrixNumerical.some(el =>
        el.length >= 2 && el.slice(0,2).every((value, index) => value === position_to_check[index])
        )
    return isPartOfLoop
}

function alreadyAdded(position_to_check: number[]): boolean {
    const alreadyAdded = nodesInsideLoop.some(el =>
        el.length === position_to_check.length && el.every((value, index) => value === position_to_check[index])
        )
    return alreadyAdded
}

console.log(nodesInsideLoop)

let final_result10_2: number = nodesInsideLoop.length
console.log(final_result10_2)


// Plot data
matrixNumerical.forEach(el => {
    // console.log(el[0], el[1])
    dots_matrix[el[0]][el[1]] = 'X'
    // nodesInsideLoop[el[0]][el[1]] = 'X'
})

nodesInsideLoop.forEach(el => {
    dots_matrix[el[0]][el[1]] = '-'
})


const stringData = dots_matrix.map(pair => pair.join('')).join('\n');
console.log(stringData);
fs10_2.writeFileSync('./src/Day10/data_visualised.txt', stringData, 'utf-8');

// nodesInsideLoop counts the nodes that are 1 step inside of the loop, this accounts for many of them 
// However if you visually represent the loop (with dots_matrix and data_visualised.txt) you see that there is a big area of nodes in the middle that are inside the loop but not a part of it 
// To get the final total, count the amount of nodes in this zone and add to nodesInsideLoop

// 291 + 274 = 565 too high
// 500 too low
