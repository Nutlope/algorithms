// ['a','b','c','d','f'] -> 'e'
// ['O','Q','R','S'] -> 'P'

function findMissingLetter(array) {
  let lowerarray = array.map((val) => val.toLowerCase());
  let alphabet = "abcdefghijklmnopqrstuvwxyz".split("");
  let startingIndex = alphabet.indexOf(lowerarray[0]);

  let counter = 0;
  for (let i = startingIndex; i < array.length + startingIndex; i++) {
    if (alphabet[i] != lowerarray[counter]) {
      console.log("something is not equal");
      if (array[0] != lowerarray[0]) {
        return alphabet[i].toUpperCase();
      } else {
        return alphabet[i];
      }
    }
    counter++;
  }
}

console.log(findMissingLetter(["O", "Q", "R", "S"]));

// Smart solution
// function findMissingLetter(array) {
//     let first = array[0].charCodeAt(0)
//     for (let i = 1; i < array.length; i++) {
//       if (first + i !== array[i].charCodeAt(0)) {
//         return String.fromCharCode(first + i)
//       }
//     }
//     throw new Error("Invalid input")
//   }
