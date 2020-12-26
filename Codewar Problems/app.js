// Take string input coming from a calculator and output the right value
// Start with just + or -
// Input  -> '5 + 6 - 3 + 10'
// Output -> 18

// Approach:
// Filter with isNan to filter out to numbers and operators
// Then for loop where you do each thing, if it's + you add it if i you subtract

function outputCalcuator(str) {
  let numArr = str.split(" "); // turns it into arr

console.log(outputCalcuator("5 + 6 - 3 + 10")); // should return 18

// one liner way to solve it --> eval("5 + 6 - 3 + 10");