// Write a function that takes in a string and checks if all letters of the alphabet are included
// Cool use of .every

function isPangram(string) {
  string = string.toLowerCase();
  return "abcdefghijklmnopqrstuvwxyz".split("").every(function (x) {
    return string.indexOf(x) !== -1;
  });
}

console.log(isPangram("The red house is riding"));

// Accessing values in getting, deleting, and assigning in objects is O(1)

// Array: Adding or deleting from beginning --> O(n). From end is O(1)
// shift, unshift O(n)
// push, pop O(1)
