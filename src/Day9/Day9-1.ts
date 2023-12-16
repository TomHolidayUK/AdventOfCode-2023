let fs9 = require('fs');


// Read the content of the file
const filePath9 = './src/Day9/data9.txt';
const fileContent9 = fs9.readFileSync(filePath9, 'utf-8'); // this reads the file synchronously

const lined_data9: string[]  = fileContent9.split('\n');

let data9_array: string[][] = []
lined_data9.map(el => data9_array.push(el.split(' ')))
let data9_array_numbers: number[][] = data9_array.map(el => el.map(el2 => Number(el2)))

const testdata9: number[][] = [
[0, 3, 6, 9, 12, 15],
[1, 3, 6, 10, 15, 21],
[10, 13, 16, 21, 30, 45]
]

// PLAN
// find differences between each value
// continue until difference are 0 
// then extrapolate: leveli(x - final) = leveli-1
// find final values
// DO THIS IN TYPESCRIPT AND PYTHON FOR PRACTICE
let all_all_differences: number[][][] = []

for (let i = 0; i < testdata9.length; i++) {

    let all_differences: number[][] = [testdata9[i]];

    function findDifferences(array: number[]): number[][] {
        let differences: number[] = [];
        for (let i = 0; i < array.length - 1; i++) {
            differences.push(array[i+1] - array[i])
        }
        all_differences.push(differences)
        if (differences.every(el => el === 0)) {
            return all_differences
        } else {
            findDifferences(differences)
        }

        return all_differences
    }

    all_all_differences.push(findDifferences(testdata9[i]))
}

console.log(all_all_differences)

function findNewEnd(input: number[][]): number {
    let final_value: number = 0 

    input[input.length - 1].push(0)

    for (let i = input.length - 2; i >= 0; i--) { // add the two ends and push it on to the array
        // console.log(i)

        let length_current: number = input[i].length;
        // console.log('length_current', length_current)
        // console.log('current end', input[i][length_current - 1])
        // console.log('previous end', input[i+1][length_current - 1])
        let new_value: number = input[i][length_current - 1] + input[i+1][length_current - 1]
        if (i === 0) {
            final_value = new_value
        }
        // console.log('new value', new_value)
        input[i].push(new_value)
    }

    return final_value

}

// console.log(findNewEnd(all_all_differences[2]))

let accululator: number = 0

for (let i = 0; i < testdata9.length; i++) {
    accululator += findNewEnd(all_all_differences[i])
}

console.log(accululator)