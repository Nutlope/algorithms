"""
Divide and conquer strategy: The idea of breaking a problem into subproblems, solving each one individually, then combine them.
Divide and conquer problems are recursive in nature. You should also have a method of combining the solutions of subproblems.
Examples: Binary search, finding max and min, mergesort, quicksort

Recurrance relations: How to find the time complexity of a recursive algorithm

function F ( n: integer ) : integer;
    begin
        if n <= 1 then
            return (2) # O(1)
        else
            result = F(n-1)
            return result * result
 end; { F }

Recurrance equations:
When n == 1: T(N) = 1 
When n > 1: T(N) = 2*T(N-1)

We want to replace T(N-1) | T(N-1) = 2T(N-1-1) = 2T(N-2). Therefore T(N-1) = 2T(N-2)
We want to replace T(N-2) | T(N-2) = 2*T(N-2-1) = 2*T(N-3)
T(N) =                2^1 * T(N-1)
T(N) = 2 * 2T(N-2) = 2^2 * T(N-2)
T(N) = 2^2 * 2*T(N-3) = 2^3 * T(N-3)
                T(N) = 2^k * T(N-k)
                We want T(N-k) == 1, therefore N-k = 1. k = N - 1
                T(N) = 2^(n-1)* T(1)
                T(N) = 2^(n-1)


                F(N) = 2^(2^(N-1))
                F(4) = 2^(2^3)

                                 2^0   F(3)=16
          2^1      F(2)=4    *    F(2)=4
       2^2     F(1)=2 * F(1)=2  F(1) * F(1)
              2  *  2      2  * 2
              
 """

def comb(n,m):
    if n == 1 or m == 0 or m == n:
        return 1
    else:
        return comb(n-1,m) + comb(n-1,m-1)

def comb2(n,m):
    count = 0
    while n != 1 and m != 0 and m != n:
        