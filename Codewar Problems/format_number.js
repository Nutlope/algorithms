// Create a function that takes in an input of numbers and returns "(123) 456-7890"
// Smart solution, using .replace for any format

function createPhoneNumber(numbers) {
  let format = "(xxx) xxx-xxxx";

  for (var i = 0; i < numbers.length; i++) {
    format = format.replace("x", numbers[i]);
  }

  return format;
}

console.log(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]));
