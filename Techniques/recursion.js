function power(base, exponent) {
  if (exponent == 0) {
    return 1
  } else {
    return base * power(base, exponent - 1)
  }
}

console.log(power(2, 3))
/*
How does this function work?

1. Add console.log to call stack

2. Add power(2,3) to call stack
3. Execute power(2,3) which returns 2 * power(2,2)

4. Add 2 * power(2,2) to call stack
5. Execute 2 * power(2,2) which returns 2 * 2 * power(2,1)

6. Add 4 * power(2,1) to call stack
7. Execute 4 * power(2,1) which returns 4 * 2 * power(2,0)

8. Add 8 * power(2,0) to call stack
9. Execute 8 * power(2,0) which returns 8 * 1

10. Pop power(2,0) off call stack
11. Pop power(2,1) off call stack
12. Pop power(2,2) off call stack
13. Pop power(2,3) off call stack

14. Execute console.log(8) and pop off call stack
*/
