const testdata: string[] = [
    '467*.114..',
    '...*......',
    '..35..633.',
    '...6..#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..'
];

// map numbers and their indices (as an array of objects)
// (represent index as single symbol; index + row * 140 )

// console.log('...317..........214.....................................751.................................630...479..205....41.993............416.........'.length)
// const linelength: number = 140

type MyType = Array<[number, number[]]>;
let numbersandindices: MyType = []


// search for *, for each one check if it is surrounded by exactly 2 numbers, if so return the indices of these numbers
// for each pair of indices find the relevant number and multiply them 

const regexasterisk = /\*/g
const regexnumber = /\d+/g;
let indicesToFind:  string[] = []



for (let i = 0; i < testdata.length; i++) {
    const linelength: number = testdata[i].length

    type MatchExecType = RegExpExecArray | null;
    let match: MatchExecType;
    while ((match = regexnumber.exec(testdata[i])) !== null) {
        // console.log("Result:", match[0]); 
        // console.log("Index:", match.index);
        // console.log('i:', i)

        const numberlength: number = match[0].length
    

        function createArrayofAscendingNumbers(n: number, m: number): number[] {
            let result: number[] = [];
            for (let i = n; i <= m; i++) {
            result.push(i);
            }
            return result;
        }

        function calculateSingleIndex(i: number, matchindex: number): number {
            return (i * linelength) + matchindex
        }

        const singleDigitIndex: number = calculateSingleIndex(i, match.index)
        // console.log(singleDigitIndex)
        let indicesofnumbers: number[] = []
        indicesofnumbers.push(...createArrayofAscendingNumbers(singleDigitIndex, singleDigitIndex + numberlength - 1))
        numbersandindices.push([Number(match[0]), indicesofnumbers])

    }
    const regexasterisk = /\*/g
    let match2: MatchExecType;
    while ((match2 = regexasterisk.exec(testdata[i])) !== null) {
        console.log("Result:", match2[0]); 
        console.log("Index:", match2.index);
        console.log('i:', i)
        const length: number = match2[0].length
        let twonumberspresent: boolean = false
        let numbersCount: number = 0

        function aboveCheck(i: number, matchindex: number, matchvalue: string, length: number, linelength: number, twonumberspresent: boolean) {
            if ((matchindex === 0) && (regexnumber.test(testdata[i-1].split('').slice(0, length + 1).join(''))) && (numbersCount < 2)) { // above (if number at start of line)
                console.log(`symbol present for ${matchvalue} (above)`)
                console.log('number count before', numbersCount)
                numbersCount++
                console.log('number count after', numbersCount)
                if (numbersCount === 2) {indicesToFind.push(matchvalue)}
            } else if ((0 < matchindex) && (matchindex + length <= linelength) && (numbersCount < 2) && (regexnumber.test(testdata[i-1].split('').slice(matchindex - 1, matchindex + length + 1).join('')))) { // above
                console.log(`symbol present for ${matchvalue} (above)`)
                console.log('number count before', numbersCount)
                numbersCount++
                console.log('number count after', numbersCount)
                if (numbersCount === 2) {indicesToFind.push(matchvalue)}
            } else if ((matchindex + length === linelength) && (regexnumber.test(testdata[i-1].split('').slice(matchindex - 1, matchindex + length).join(''))) && (numbersCount < 2)) { // above (if number at end of line)
                console.log(`symbol present for ${matchvalue} (above)`)
                console.log('number count before', numbersCount)
                numbersCount++
                console.log('number count after', numbersCount)
                if (numbersCount === 2) {indicesToFind.push(matchvalue)}
            }
        }
        function belowCheck(i: number, matchindex: number, matchvalue: string, length: number, linelength: number, twonumberspresent: boolean) {
            if ((matchindex === 0) && (regexnumber.test(testdata[i+1].split('').slice(0, length + 1).join(''))) && (numbersCount < 2)) { // below (if number at start of line)
                console.log(`symbol present for ${matchvalue} (below)`)
                console.log('number count before', numbersCount)
                numbersCount++
                console.log('number count after', numbersCount)
                if (numbersCount === 2) {indicesToFind.push(matchvalue)}
            } else if ((0 < matchindex) && (matchindex + length <= linelength) && (regexnumber.test(testdata[i+1].split('').slice(matchindex - 1, matchindex + length + 1).join(''))) && (numbersCount < 2)) { // below
                console.log(`symbol present for ${matchvalue} (below)`)
                console.log('number count before', numbersCount)
                numbersCount++
                console.log('number count after', numbersCount)
                if (numbersCount === 2) {indicesToFind.push(matchvalue)}
            } else if ((matchindex + length === linelength) && (regexnumber.test(testdata[i+1].split('').slice(matchindex - 1, matchindex + length).join(''))) && (numbersCount < 2)) { // below (if number at end of line)
                console.log(`symbol present for ${matchvalue} (below)`)
                console.log('number count before', numbersCount)
                numbersCount++
                console.log('number count after', numbersCount)
                if (numbersCount === 2) {indicesToFind.push(matchvalue)}
            }
        }
        
        function leftandrightCheck(i: number, matchindex: number, matchvalue: string, length: number, linelength: number, twonumberspresent: boolean) {
            console.log(regexnumber.test(testdata[i].split('')[matchindex - 1]))
            console.log(testdata[i].split('')[matchindex - 1])
            console.log(matchindex)
            if ((matchindex > 0) && (regexnumber.test(testdata[i].split('')[matchindex - 1])) && (numbersCount < 2)) { // left
                console.log('hello')
                console.log(`symbol present for ${matchvalue} (left)`)
                console.log('number count before', numbersCount)
                numbersCount++
                console.log('number count after', numbersCount)
                if (numbersCount === 2) {indicesToFind.push(matchvalue)}
            } else if ((matchindex + length < linelength) && (regexnumber.test(testdata[i].split('')[matchindex + length ])) && (numbersCount < 2)) { // right
                console.log(`symbol present for ${matchvalue} (right)`)
                console.log('number count before', numbersCount)
                numbersCount++
                console.log('number count after', numbersCount)
                if (numbersCount === 2) {indicesToFind.push(matchvalue)}
            }
        }

        if (i === 0) { // for top row
            leftandrightCheck(i, match2.index, match2[0], length, linelength, twonumberspresent)
            belowCheck(i, match2.index, match2[0], length, linelength, twonumberspresent)
        } else if (0 < i && i < testdata.length - 1) { // for middle rows
            aboveCheck(i, match2.index, match2[0], length, linelength, twonumberspresent)
            leftandrightCheck(i, match2.index, match2[0], length, linelength, twonumberspresent)
            belowCheck(i, match2.index, match2[0], length, linelength, twonumberspresent)
        } else if (i === testdata.length - 1) { // for bottom row
            aboveCheck(i, match2.index, match2[0], length, linelength, twonumberspresent)
            leftandrightCheck(i, match2.index, match2[0], length, linelength, twonumberspresent)
        }
    }
}

console.log(numbersandindices)
console.log(indicesToFind)

// const searchValue = 63;

// const result = numbersandindices.find(([value, indices]) => indices.includes(searchValue));

// if (result) {
//   const [foundNumber, correspondingIndices] = result;
//   console.log(`Value ${searchValue} found at indices: ${correspondingIndices} for number ${foundNumber}`);
// } else {
//   console.log(`Value ${searchValue} not found in the array.`);
// }