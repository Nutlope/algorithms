// Frequency Counter

// Ineffecient solution - O(n^3)

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

function same(arr1, arr2) {
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

console.log(same([1, 2, 4], [1, 4, 16]));

// Multiple Pointers

// Sliding Window

// Divide and Conquer

// Dynamic Programming

// Greedy Algorithms

// Backtracking
