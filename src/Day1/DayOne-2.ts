let data = require('./DayOne-1.ts'); // Provide the correct path to file1

const regex = /(one|two|three|four|five|six|seven|eight|nine|(\d))/g;
const regexreverse = /(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|(\d))/g;

let runningtotal: number = 0

// console.log(data[1].match(regex))

data.forEach( (el: string) => {
    let datareversed: string = el.split('').reverse().join('')
    // console.log(datareversed)
    // console.log(datareversed.match(regexreverse))
    let matchesreversed = datareversed.match(regexreverse)
    
    if (matchesreversed !== null) {
        matchesreversed  = datareversed.match(regexreverse)
    } 
    
    let allNumbersreversed: string[] = []
    
    if ((matchesreversed !== null)) {
        matchesreversed.forEach( el => {
            if (el !== '') {
                allNumbersreversed.push(el)
            }
        })
    }
    
    
    // console.log(matchesreversed)
    
    
    allNumbersreversed.forEach((el, index) => {
        if (el === 'eno') {
            allNumbersreversed[index] = '1';
        } else if (el === 'owt') {
            allNumbersreversed[index] = '2';
        } else if (el === 'eerht') {
            allNumbersreversed[index] = '3';
        } else if (el === 'ruof') {
            allNumbersreversed[index] = '4';
        } else if (el === 'evif') {
            allNumbersreversed[index] = '5';
        } else if (el === 'xis') {
            allNumbersreversed[index] = '6';
        } else if (el === 'neves') {
            allNumbersreversed[index] = '7';
        } else if (el === 'thgie') {
            allNumbersreversed[index] = '8';
        }  else if (el === 'enin') {
            allNumbersreversed[index] = '9';
        } 
    });
    
    // console.log(allNumbersreversed)
    
    let lastnumber: number = parseInt(allNumbersreversed[0])
    
    
    let matches = el.match(regex)


    if ((matches !== null)) {
        matches = el.match(regex)
    }

    let allNumbers: string[] = []
    
    
    
    if ((matches !== null)) {
        matches.forEach( el => {
            if (el !== '') {
                allNumbers.push(el)
            }
        })
    }


allNumbers.forEach((el, index) => {
    if (el === 'one') {
        allNumbers[index] = '1';
    } else if (el === 'two') {
        allNumbers[index] = '2';
    } else if (el === 'three') {
        allNumbers[index] = '3';
    } else if (el === 'four') {
        allNumbers[index] = '4';
    } else if (el === 'five') {
        allNumbers[index] = '5';
    } else if (el === 'six') {
        allNumbers[index] = '6';
    } else if (el === 'seven') {
        allNumbers[index] = '7';
    } else if (el === 'eight') {
        allNumbers[index] = '8';
    }  else if (el === 'nine') {
        allNumbers[index] = '9';
    } 
});


let firstnumber: string = allNumbers[0]


runningtotal += parseInt(firstnumber + lastnumber)
console.log(parseInt(firstnumber + lastnumber))
console.log(runningtotal)

})




console.log(runningtotal)


