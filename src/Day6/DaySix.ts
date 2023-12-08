// Part 1 Data
// let times: number[] = [55, 82, 64, 90];
// let distance: number[] = [246, 1441, 1012, 1111];

// Part 2 Data
let times: number[] = [55826490];
let distance: number[] = [246144110121111];

let test_times: number[] = [7, 15, 30];
let test_distance: number[] = [9, 40, 200];

// distance covered if you hold button for x seconds = (duration - x) * x 

let distances: number[][] = []

for (let i = 0; i < times.length; i++) {
    let distance: number[] = []
    for (let j = 0; j < times[i]; j++) {
    distance.push((times[i] - j) * j)
    }
    distances.push(distance)
}

console.log(distances)

let validDistances = distances.map((el, index) => el.filter(value => value > distance[index]))

console.log(validDistances)

let daySixFinal: number = 1

validDistances.forEach( el => {
    daySixFinal *= el.length 
})

console.log(daySixFinal)