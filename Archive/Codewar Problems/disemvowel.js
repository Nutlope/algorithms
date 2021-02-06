// Write a function that takes in a str, gets rid of vowels, and returns it

function disemvowel(str) {
  let vowels = ["a", "e", "i", "o", "u"];

  return str
    .split("")
    .filter(function (el) {
      return vowels.indexOf(el.toLowerCase()) == -1;
    })
    .join("");
}

console.log(disemvowel("this is not a normal thing"));
