// Leetcode problem 832: Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.
// To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].
// To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

// Input:
// Output:
// Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
// Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
var assert = require('assert');

function flipImage(A) {
    // O(N^2) time | O(1) space

    // loop through rows and for each row, run a .reverse() operation. Then use binary XOR on each
    for (let row of A) {
        row = row.reverse()
        for (let i = 0; i < row.length; i++) {
            row[i] = row[i]^1
        }
    }
    return A
}

let image = [[1,1,0],[1,0,1],[0,0,0]];

console.log(flipImage(image));
