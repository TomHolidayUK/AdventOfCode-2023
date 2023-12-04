"use strict";
const fs = require('fs');
const filePath = 'data.txt';
const fileContent = fs.readFileSync(filePath, 'utf-8');
const lines = fileContent.split('\n');
console.log(lines);
lines.forEach((line, index) => {
    console.log(`Line ${index + 1}: ${line}`);
});
const nonEmptyLines = lines.filter((line) => line.trim() !== '');
console.log(nonEmptyLines);
