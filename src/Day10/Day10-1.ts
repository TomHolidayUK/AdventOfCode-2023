import { start } from "repl";

let fs10 = require('fs');


// Read the content of the file
const filePath10 = './src/Day10/data10.txt';
const fileContent10 = fs10.readFileSync(filePath10, 'utf-8'); // this reads the file synchronously

const lined_data10: string[]  = fileContent10.split('\n');
const matrix: string[][]  = lined_data10.map(el => el.split(''))

// const testdata10: string[][] = [
//     ['-', 'L', '|', 'F', '7'],
//     ['7', 'S', '-', '7', '|'],
//     ['L', '|', '7', '|', '|'],
//     ['-', 'L', '-', 'J', '|'],
//     ['L', '|', '-', 'J', 'F']
// ]

const testdata10: string[][] = [
    ['.', '.', 'F', '7', '.'],
    ['7', 'F', 'J', '|', '|'],
    ['S', 'J', '7', 'L', '7'],
    ['|', 'F', '-', '-', 'J'],
    ['L', 'J', '-', 'J', 'F']
]
    

// console.log(lined_data10)
// console.log(matrix[0])

// find start 
// write function to find surrounding nodes
// move to one then repeat, take note of nodes that have already travelled on so they don't repeat (nodes are unidirectional)
// records number of steps 
// midpoint is steps / 2

let start_y: number = 0
let start_x: number = 0

matrix.forEach((el, index) => {
    if (el.includes('S')) {
        start_y = index
    }
})

matrix[start_y].forEach((el, index) => {
    if (el.includes('S')) {
        start_x = index
    }
})

let start_position: number[] = [start_y, start_x]
console.log('start position:', start_position)


// coordinate system = [y, x] (direction of y is reversed, to match row numbers)
// to index the matrix: [y][x]


function findNextNode(position: number[], direction: number): number[] {
    // take position and direction as arguments, find valid next positions and next directions

    let next_node_data: number[] = [] // next position y, next position x, direction (1 = above, 2 = right, 3 = below, 4 = left)

    if (direction === 1) {
        let above_value: string = matrix[position[0] - 1][position[1]]
        // console.log('above value', above_value)
        if (above_value === '|') {
            // console.log(`above is valid with '|', next index: [${position[0] - 2}]${position[1]}]`)
            next_node_data = [position[0] - 1, position[1], 1]
        } else if (above_value === '7') {
            // console.log(`above is valid with '7', next index: [${position[0] - 1}][${position[1] - 1}]`)
            next_node_data = [position[0] - 1, position[1], 4]
        } else if (above_value === 'F') {
            // console.log(`above is valid with 'F', next index: [${position[0] - 1}][${position[1] + 1}]`)
            next_node_data = [position[0] - 1, position[1], 2]
        } else if (above_value === 'S') {
            return [start_position[0], start_position[1], 3]
        }
    }

    if (direction === 3) {
        let below_value: string = matrix[position[0] + 1][position[1]]
        // console.log('below value', below_value)
        if (below_value === '|') {
            // console.log(`below is valid with '|', next index: [${position[0] + 2}]${position[1]}]`)
            next_node_data = [position[0] + 1, position[1], 3]
        } else if (below_value === 'L') {
            // console.log(`below is valid with 'L', next index: [${position[0] + 1}][${position[1] + 1}]`)
            next_node_data = [position[0] + 1, position[1], 2]
        } else if (below_value === 'J') {
            // console.log(`below is valid with 'J', next index: [${position[0] + 1}][${position[1] - 1}]`)
            next_node_data = [position[0] + 1, position[1], 4]
        } else if (below_value === 'S') {
            return [start_position[0], start_position[1], 3]
        }
    }

    if (direction === 4) {
        let left_value: string = matrix[position[0]][position[1] - 1]
        // console.log('left value', left_value)
        if (left_value === '-') {
            // console.log(`left is valid with '-', next index: [${position[0]}][${position[1] - 2}]`)
            next_node_data = [position[0], position[1] - 1, 4]
        } else if (left_value === 'L') {
            // console.log(`left is valid with 'L', next index: [${position[0] - 1}][${position[1] - 1}]`)
            next_node_data = [position[0], position[1] - 1, 1]
        } else if (left_value === 'F') {
            // console.log(`left is valid with 'F', next index: [${position[0] + 1}][${position[1] - 1}]`)
            next_node_data = [position[0], position[1] - 1, 3]
        } else if (left_value === 'S') {
            return [start_position[0], start_position[1], 4]
        }
    }

    if (direction === 2) {
        let right_value: string = matrix[position[0]][position[1] + 1]
        // console.log('right value', right_value)
        if (right_value === '-') {
            // console.log(`right is valid with '-', next index: [${position[0]}][${position[1] + 2}]`)
            next_node_data = [position[0], position[1] + 1, 2]
        } else if (right_value === 'J') {
            // console.log(`right is valid with 'J', next index: [${position[0] - 1}][${position[1] + 1}]`)
            next_node_data = [position[0], position[1] + 1, 1]
        } else if (right_value === '7') {
            // console.log(`right is valid with '7', next index: [${position[0] + 1}][${position[1] + 1}]`)
            next_node_data = [position[0], position[1] + 1, 3]
        } else if (right_value === 'S') {
            return [start_position[0], start_position[1], 3]
        }
    }

    return next_node_data  // next position y, next position x, direction (1 = above, 2 = right, 3 = below, 4 = left)
}



// console.log(findNextNode([1, 1], 3))


// need a recursive function that accepts a current position and previous position 
// it uses findSurroundingNodes to find potential next nodes
// this cannot be the previous node so it has to be the other one, this will be the next node, this will be fed as the current position in the recursion 
// if the current position = starting position , stop function
// count steps

let steps_total: number = 10000
let perimeter: number[][] = []
let perimeterWithDirections: (string|number)[][] = []
let current_direction_global: number = 0

function recursiveFunction(currentPosition: number[], direction: number): number {

        perimeter.push(currentPosition)
        perimeterWithDirections.push([currentPosition[0], currentPosition[1], direction, matrix[currentPosition[0]][currentPosition[1]]])
        current_direction_global = direction
        console.log('current value:', matrix[currentPosition[0]][currentPosition[1]])

        const next_position_data: number[] = findNextNode(currentPosition, direction)
        const next_y: number = next_position_data[0];
        const next_x: number = next_position_data[1];
        const next_direction: number = next_position_data[2];
        const next_position: number[] = [next_y, next_x];
        console.log(next_position, next_direction)

        if ((matrix[next_y][next_x] === 'S') || (steps_total >= 15000)) { // end condition
            steps_total++
            console.log('end')
            return steps_total
        } 


        steps_total++
        console.log('steps_total', steps_total)
        return recursiveFunction(next_position, next_direction)

}

// console.log(recursiveFunction(start_position, 3))
// recursiveFunction([107, 117], 2) // 5000
recursiveFunction([73, 53], 4) // 10000


// ----------------Export perimeter data for part 2------------------------
// console.log(perimeter)
console.log(perimeterWithDirections)
const stringData = perimeterWithDirections.map(pair => pair.join(', ')).join('\n'); 
console.log(stringData);
fs10.writeFileSync('src/Day10/perimeterWithDirections3.txt', stringData, 'utf-8');
// console.log(current_direction_global)


