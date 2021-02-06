// Frequency Counter Pattern

// Ineffecient solution - O(n^2)

function same(arr1, arr2) {
  if (arr1.length !== arr2.length) {
    return false;
  }
  for (let char of arr1) {
    let foundOne = false;
    for (let square of arr2) {
      if (char ** 2 === square) {
        arr2.splice(arr2.indexOf(square), 1);
        foundOne = true;
      }
    }
    if (foundOne == false) {
      return false;
    }
  }
  return true;
}

// Optimal Solution - O(N)

function sameBetter(arr1, arr2) {
  if (arr1.length !== arr2.length) {
    return false;
  }
  let freqCounter1 = {};
  let freqCounter2 = {};

  for (let val of arr1) {
    freqCounter1[val] = (freqCounter1[val] || 0) + 1;
  }
  for (let val of arr2) {
    freqCounter2[val] = (freqCounter2[val] || 0) + 1;
  }

  for (let key in freqCounter1) {
    if (!(key ** 2 in freqCounter2)) {
      return false;
    }
    if (freqCounter2[key ** 2] !== freqCounter1[key]) {
      return false;
    }
  }
  return true;
}

console.log(sameBetter([1, 2, 4], [1, 4, 16]));

// Anagrams Problem: Given 2 strings, write a function to determine if the second string is an anagram of the first.
// Assume everything is lowercase and no special characters including spaces

function validAnagram(str1, str2) {
  if (str1.length !== str2.length) {
    return false;
  }
  let freqCounter1 = {};
  let freqCounter2 = {};

  for (let char of str1) {
    freqCounter1[char] = (freqCounter1[char] || 0) + 1;
  }
  for (let char of str2) {
    freqCounter2[char] = (freqCounter2[char] || 0) + 1;
  }

  for (let key in freqCounter1) {
    if (!(key in freqCounter2)) {
      return false;
    }
    if (freqCounter2[key] !== freqCounter1[key]) {
      return false;
    }
  }
  return true;
}

console.log(validAnagram("hello", "hello"));
