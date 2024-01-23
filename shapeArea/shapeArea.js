// shapeArea.js

/*

Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

Example

For n = 2, the output should be
solution(n) = 5;
For n = 3, the output should be
solution(n) = 13.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

Guaranteed constraints:
1 ≤ n < 10^4 (100000).

[output] integer

The area of the n-interesting polygon.

n   shapeArea   step    multiplier
----------------------------------
1   *  1        * 0     *   0
2   *  5        * 4     *   1
3   *  13       * 8     *   2
4   *  25       * 12    *   3
5   *  41       * 16    *   4
6   *  61       * 20    *   5
7   *  75       * 24    *   6

*/

function solution(n)
{
    step = 0;
    result = 0;
    prev = 1;       // previous shapeArea value
    
    if (n == 1)
    {
        return 1;
    }

    else
    {
        for (i = 1; i < n; i++)
        {
            step = i * 4;
            result = prev + step;
            prev = result;
        }
    }

    return result;
}

inputArray = [2, 3, 1, 5, 7000, 8000, 9999, 9998, 8999, 100];

for (i = 0; i < inputArray.length; i++)
{
    tmp = inputArray [i];
    console.log("tmp: ", tmp, " shapeArea: ", solution(tmp));
}

/*

********
BONEYARD
********

// console.log("i: ", i, " step: ", step, " result: ", result, " prev: ", prev);

            n = 2       i   step    result      prev
            m = 1       1   4       5           1
            step = 4
        
            n = 3       1   4       5           1
            m = 1       2   8       13          5
            step = 8
  

    // console.log("n: ", inputArray [i], " result: ", solution(i));

    seq 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 233
    n = 1   fib: 1      seq# 2, 3
    n = 2   fib: 5      seq# 6
    n = 3   fib: 13     seq# 8
    n = 4   fib: 34     seq# 10
    n = 5   fib: 89     seq# 12 // this is meant to be 41
    n = 6   fib: 233     seq# 14


    PROPER
    ******

    n: 5        result: 41
    n: 7000     result: 97986001
    n: 8000     result: 127984001
    n: 9999     result: 199940005
    n: 9998     result: 199900013
    n: 8999     result: 161946005
    n: 100      result: 19801

function solution(n) 
{
    if (n == 1)
    {
        return 1;
    }
    
    else 
    {
        step = 0;
        tmp = 6;

        if (n == 2)
        {
            return 5;
        }

        else
        {
            step = n - 3;
            // console.log("*1 n: ", n, " step: ", step);
            step = step * 2;
            // console.log("*2 n: ", n, " step: ", step);
        }

        tmp = tmp + step;
        return fibonacciIter(tmp);
    }

}

// fibonnaci recursive
function fibonacciRec(n)
{
    // console.log("n: ", n);
    
     if (n < 2) return n;

     return fibonacci(n - 1) + fibonacci(n - 2);

}

// fibonnaci iterative
function fibonacciIter(n)
{
    prev = 0;
    next  = 1;
    result = 0;
    i = 0;

    for (i; i < n; i++) 
    {
        // console.log("*1 i: ", i, " n: ", tmp, " result: ", fibonacciIter(tmp));
        
        result = prev + next;
        prev = next;
        next = result;

        // console.log("*2 i: ", i, " n: ", tmp, " result: ", fibonacciIter(tmp));
    }

    return result;
}

*/