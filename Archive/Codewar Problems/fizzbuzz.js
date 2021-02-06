// Eloquent JavaScript, Exercise 2.1

function FizzBuzz() {
  for (let i = 1; i < 101; i++) {
    let str = "";
    if (i % 3) str += "Fizz";
    if (i % 5) str += "Buzz";
    console.log(str || i);
  }
}

FizzBuzz();
