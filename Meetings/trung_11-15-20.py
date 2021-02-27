
// // Take string input coming from a calculator and output the right value
// // Start with just + or -, *, /, (, )
// // Input  -> '5 + 6 - 3 + 10'
// // Output -> 18

// split into array
// loop through array and check if something is a number or operator
// do each computation (like 5+6) and save it to a global variable
// output final number
// CS265
// 1 * (2 + 3) / 4
// 1 2 3 + * 4 /
// stack = [5 4]


function outputCalcuator(str) {
  let numArr = str.split(" "); // turns it into arr
  let operators = numArr.filter(val => isNaN(val))
  let operants = numArr.filter(val => !isNaN(val))
  console.log(operators);
  console.log(operants);
  
  let init = parseInt(operants[0], 10)
  for (let i = 0; i < operators.length; i++){
    if (operators[i] == "+") {
      init += parseInt(operants[i + 1], 10)
    } else {
      init -= parseInt(operants[i + 1], 10);
    }
  }
  return init
}

console.log(outputCalcuator('5 + 6 - 3 + 10'));