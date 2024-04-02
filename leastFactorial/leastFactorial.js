/*

Given an integer n, find the minimal k such that

k = m! (where m! = 1 * 2 * ... * m) for some integer m;
k >= n.
In other words, find the smallest factorial which is not less than n.

Example

For n = 17, the output should be
solution(n) = 24.

17 < 24 = 4! = 1 * 2 * 3 * 4, while 3! = 1 * 2 * 3 = 6 < 17).

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

A positive integer.

Guaranteed constraints:
1 ≤ n ≤ 120.

[output] integer

*/

function factorial(n)
{
    if (n == 1)
    {
        return 1 * n;
    }
    
    else 
    {
        return n * factorial (n - 1);
    }

}

function leastFactorial(n)
{
    let cur = 0;
    let i = 1;

    while (cur < n)
    {
        cur = factorial(i);
        i++;
    }

    // console.log(cur);
    return cur;
}

function solution(n) 
{
    return leastFactorial(n);
}

let n = 17;

// console.log(factorial(n))
// leastFactorial(n);


/*

********
BONEYARD
********

*/