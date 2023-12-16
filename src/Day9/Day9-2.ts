let fs9_2 = require('fs');


// Read the content of the file
const filePath9_2 = './src/Day9/data9.txt';
const fileContent9_2 = fs9_2.readFileSync(filePath9_2, 'utf-8'); // this reads the file synchronously

const lined_data9_2: string[]  = fileContent9_2.split('\n');

let data9_2_array: string[][] = []
lined_data9_2.map(el => data9_2_array.push(el.split(' ')))
let data9_2_array_numbers: number[][] = data9_2_array.map(el => el.map(el2 => Number(el2)))

const testdata9_2: number[][] = [
[0, 3, 6, 9, 12, 15],
[1, 3, 6, 10, 15, 21],
[10, 13, 16, 21, 30, 45]
]

let all_all_differences_2: number[][][] = []

for (let i = 0; i < data9_2_array_numbers.length; i++) {

    let all_differences: number[][] = [data9_2_array_numbers[i]];

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

    all_all_differences_2.push(findDifferences(data9_2_array_numbers[i]))
}

console.log(all_all_differences_2)

function findNewEnd_2(input: number[][]): number {
    let final_value: number = 0 

    input[input.length - 1].unshift(0)

    for (let i = input.length - 2; i >= 0; i--) { // add the two ends and push it on to the array
        console.log(i)

        let length_current: number = input[i].length;
        // console.log('length_current', length_current)
        console.log('current start', input[i][0])
        console.log('previous start', input[i+1][0])
        let new_value: number = input[i][0] - input[i+1][0]
        if (i === 0) {
            final_value = new_value
        }
        console.log('new value', new_value)
        input[i].unshift(new_value)
    }

    return final_value

}

// console.log(findNewEnd_2(all_all_differences_2[0]))

let accululator_2: number = 0

for (let i = 0; i < data9_2_array_numbers.length; i++) {
    accululator_2 += findNewEnd_2(all_all_differences_2[i])
}

console.log(accululator_2)