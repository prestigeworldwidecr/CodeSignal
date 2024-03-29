// almostIncreasingSequence.js

/*

Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence by removing no more than one element from the array.

Note: sequence a0, a1, ..., an is considered to be a strictly increasing if a0 < a1 < ... < an. Sequence containing only one element is also considered to be strictly increasing.

Example

For sequence = [1, 3, 2, 1], the output should be
solution(sequence) = false.

There is no one element in this array that can be removed in order to get a strictly increasing sequence.

For sequence = [1, 3, 2], the output should be
solution(sequence) = true.

You can remove 3 from the array to get the strictly increasing sequence [1, 2]. Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.integer sequence

Guaranteed constraints:
2 ≤ sequence.length ≤ 105,
-105 ≤ sequence[i] ≤ 105.

[output] boolean

Return true if it is possible to remove one element from the array in order to get a strictly increasing sequence, otherwise return false.

*/

// flatRun goes through sequence less one element
// one element out of order returns false
function flatRun(sequence)
{    
    for (i = 0; i < sequence.length - 1; i++)
    {
        // console.log("i: ", i, " sequence[i]: ", sequence[i], " sequence[i + 1]: ", sequence[i + 1])
        
        if (sequence[i] < sequence[i + 1])
        {
            //
        }

        else
        {
            return false;
        }
    }

    return true;
}

function copyArraySansElement(sequence, n)
{
    i = 0;
    j = 0;
    tmp = [];

    for(i; i < sequence.length; i++)
    {
        if (i == n)
        {
            //
        }
        
        else
        {
            tmp [j] = sequence [i];
            j++;
        }
    }

    return tmp;
}

function solution1(sequence)
{
    cnt = 0;            // count out of sequence
    currCnt = 0;        // count when currentMax overwhelmed
    currentMax = -999999;

    for (i = 0; i < sequence.length; i++)
    {
        if (sequence [i] >= sequence [i + 1])
        {
            cnt++;
        }

        else if (cnt > 1 || currCnt > 1)
        {
            return false;
        }

        else if (sequence [i + 1] <= currentMax)
        {
            // 
        }

        else
        {
            currentMax = sequence [i + 1];
            currCnt++;
        }

        console.log("i: ", i, " sequence [i]: ", sequence [i], " sequence [i + 1]: ", sequence [i + 1], " cnt: ", cnt,  " currCnt: ",  currCnt, " currentMax: ", currentMax);
    }

    return true;
}

// different strategy using prevMax, currMax
function solution2(sequence)
{
    prevMax = -999999;
    currentMax = -999999;

    for (i = 0; i < sequence.length; i++)
    {
        if (i == 0)
        {
            console.log("*1");
            
            if (sequence [i] < sequence [i + 1])
            {
                prevMax = sequence [i + 1];
                currentMax = sequence [i + 1];
            }

            else
            {
                prevMax = sequence [i];
                currentMax = sequence [i];
            }
        }

        else if ( (sequence [i] >= sequence [i + 1]) &&
                (sequence [i] >= currentMax) &&
                (sequence [i] >= prevMax) )
        {
            console.log("*2");
            return false;
        }

        else
        {
            console.log("*3");
            prevMax = currentMax;
            currentMax = sequence [i + 1];
        }

        console.log("i: ", i, " sequence [i]: ", sequence [i], " sequence [i + 1]: ", sequence [i + 1], " currentMax: ", currentMax, " prevMax: ", prevMax);

        /*

        if (sequence [i] >= sequence [i + 1])
        {
            cnt++;
        }

        
        else if (sequence [i + 1] <= currentMax)
        {
            // 
        }

        else
        {
            currentMax = sequence [i + 1];
        }

        */

    }

    return true;
}

// read sequence backwards
// check repeats
function solution3(sequence)
{
    cnt = 0;                                    // count out of sequence
    rptCnt = 0;                                 // count of repeat
    currMax = sequence[sequence.length - 1];
    
    for (i = sequence.length; i > 0; i--)
    {
        console.log("i: ", i, " sequence [i]: ", sequence [i], " sequence [i - 1]: ", sequence [i - 1], " currMax: ", currMax, " cnt: ", cnt);
        
        if (cnt > 1)
        {
            return false;
        }
        
        else if (rptCnt > 1)
        {
            return false;
        }

        else if (sequence [i] == sequence[i - 1])
        {
            rptCnt++;
        }

        else if (sequence [i] > sequence[i - 1])
        {
            // 
        }

        else if (sequence [i] < sequence[i - 1])
        {
            currMax = sequence[i - 1];
            cnt++;
        }

        else
        {

        }
        
    }

    return true;
}

// remove element, run again
function solution4(sequence)
{
    cnt = 0;    // count out of sequence

    for (i = 0; i < sequence.length; i++)
    {
        console.log("i: ", i, " sequence [i]: ", sequence [i], " sequence [i + 1]: ", sequence [i + 1], " cnt: ", cnt);

        if (cnt >= 1)
        {
            sequence.pop(sequence[i + 1]);
            return flatRun(sequence);
        }

        else if(sequence[i] >= sequence[i + 1])
        {
            // sequence.pop(sequence[i]);
            cnt++;
        }

        else
        {
            //
        }

    }

    return true;
}

// create array of arrays missing one element
// flatRun each
function solution5(sequence)
{
    for (z = 0; z < sequence.length; z++)
    {
        if (flatRun(copyArraySansElement(sequence, z)))
        {
            return true;
        }
    }

    return false;
}

// run through array backwards
// out of sequence, remove element
// send to flatrun
function solution6(sequence)
{
    // console.log("prev\t\t", "curr\t\t", "next");
    // console.log("----\t\t", "----\t\t", "----");

    for (x = sequence.length - 1; x > 0; x--)
    {   
        // 0...(x - 1)...x...x + 1...sequence.length
        // 0....prev...next...curr....sequence.length

        prev = x - 1;
        curr = x;
        next = x + 1;

        // console.log(sequence[prev], "\t\t", sequence[curr], "\t\t", sequence[next]);        

        // last element
        // if ((x == sequence.length - 1) && (sequence[x] <= sequence[x - 1]))
        // if ((x == sequence.length - 1) && (sequence[x - 1] >= sequence[x]))
        if ((curr == sequence.length - 1) && (sequence[prev] >= sequence[curr]))
        {
            console.log("check #1");
            return flatRun(copyArraySansElement(sequence, curr));
        }
        
        // first element
        // else if ((x == 1) && (sequence[x] >= sequence[x - 1]))
        else if ((curr == 1) && (sequence[prev] >= sequence[curr]))
        {
            console.log("check #2");
            return flatRun(copyArraySansElement(sequence, prev));
        }
        
        // look both ways
        // else if ((sequence[x] >= sequence[x - 1]) && (sequence[x] >= sequence[x + 1]))
        else if ((sequence[prev] <= sequence[curr]) && (sequence[curr] >= sequence[next]))
        {
            console.log("check #3\t");

            // doubles
            if (sequence.includes(sequence[next]))
            {
                console.log("a");
                return flatRun(copyArraySansElement(sequence, next));
            }
            
            else
            {
                console.log("b");
                return flatRun(copyArraySansElement(sequence, curr));
            }
        }

        // look left
        // else if ((sequence[x] <= sequence[x - 1]) && (sequence[x] <= sequence[x + 1]))
        // else if ((sequence[x - 1] >= sequence[x]) && (sequence[x] <= sequence[x + 1]))
        else if ((sequence[prev] >= sequence[curr]) && (sequence[curr] <= sequence[next]))
        {
            console.log("check #4\t");
            
            // doubles
            if (sequence.includes(sequence[curr]))
            {
                console.log("a");
                return flatRun(copyArraySansElement(sequence, curr));
            }
            else
            {
                console.log("b");
                return flatRun(copyArraySansElement(sequence, prev));
            }
        }
        
        /*
        // look right
        else if ((sequence[x] >= sequence[x - 1]) && (sequence[x] <= sequence[x + 1]))
        {
            return flatRun(copyArraySansElement(sequence, x));
        }
        */

        // peachy
        else
        {
            // 
        }
    }

    return true;

}

/*
    run through array backwards
    out of sequence, leverage flatrun for criteria
    the truth is out there
    
    prev    curr    next
    curr-2  curr-1  curr
    a       b       c
    
    1 a == c
    2 a < b && b < c
    3 a > b && b < c
    4 a < b && b > c
    5 a > b && b > c
    6 a == b
    7 b == c
    8 a > b && a > c

    0...(x - 1)...x...x + 1...sequence.length
    0....prev...next...curr...sequence.length
    0.....a......b......c.....sequence.length

*/
function solution7(sequence)
{
    c = sequence.length;
    b = null;
    a = null;

    // console.log("  a  \t\t", "  b  \t\t", "  c  ");
    // console.log("-----\t\t", "-----\t\t", "-----");

    for (w = sequence.length - 1; w > 1; w--)
    {   
        c = w;
        b = c - 1;
        a = b - 1;

        // console.log(sequence[a], "\t\t", sequence[b], "\t\t", sequence[c]);
        
        if (sequence[a] == sequence[c])
        {
            // console.log("*1")
            return flatRun(copyArraySansElement(sequence, a));
        }

        else if (sequence[b] == sequence[c])
        {
            // console.log("*2")
            return flatRun(copyArraySansElement(sequence, c));
        }

        else if (sequence[a] == sequence[c])
        {
            // console.log("*3")
            return flatRun(copyArraySansElement(sequence, c));
        }
        
        else if (sequence[a] < sequence[b] && sequence[b] < sequence[c])
        {
            // console.log("*4");
        }
        
        else if (sequence[a] > sequence[b] && sequence[a] > sequence[c])
        {
            // console.log("*5")
            return flatRun(copyArraySansElement(sequence, a));
        }

        else if (sequence[a] > sequence[b] && sequence[b] < sequence[c])
        {
            // console.log("*6")
            return flatRun(copyArraySansElement(sequence, b));
        }

        else if (sequence[a] < sequence[b] && sequence[b] > sequence[c])
        {
            // console.log("*7")
            return flatRun(copyArraySansElement(sequence, c));
        }

        else if (sequence[a] > sequence[b] && sequence[b] > sequence[c])
        {
            // console.log("*8")
            return false;
        }

        // peachy
        else
        {
            // 
        }
        
    }

    return true;

}

s1 = [1, 3, 2, 1];                          // false
s2 = [1, 3, 2];                             // true
s3 = [1, 2, 1, 2];                          // false
s4 = [1, 2, 3, 4, 5, 3, 5, 6];              // false
s5 = [40, 50, 60, 10, 20, 30];              // false
s6 = [1, 2, 5, 3, 5];                       // true
s7 = [1, 2, 3, 4, 99, 5, 6];                // true
s8 = [123, -17, -5, 1, 2, 3, 12, 43, 45]    // true
s9 = [1, 2, 3, 4, 3, 6];                    // true
s10 = [3, 5, 67, 98, 3];                    // true

s = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10];

// console.log(solution7(s10));

for (y = 0; y < s.length; y++)
{
    console.log(s[y], solution7(s[y]));
}

/*

********
BONEYARD
********

// console.log(solution6(s[1]));
// console.log(s9.includes(3));

        /*
        // doubles
        
        else if (sequence.includes(sequence[x], x - 1))
        {
            return flatRun(copyArraySansElement(sequence, x));
        }
        */

// console.log("***", flatRun(copyArraySansElement(sequence, x)));
            // tmp = copyArraySansElement(sequence, x - 1);
            // console.log(tmp);
            /*
        if (currMax <= sequence[i - 1]) 
        {

        }
        */
        
        // console.log("x: ", x, " sequence[i]: ", sequence[x], "sequence[i - 1]: ", sequence[x - 1]);

        // if (flatRun(copyArraySansElement(sequence, z)))
        // {
            // console.log(true);
        // }    
    // console.log(false);
    
    /*
    for (z = 0; z < sequence.length; z++)
    {
        if (flatRun(copyArraySansElement(sequence, 0)))
        {
            return true;
        }

        else
        {
            //
            return false;
        }
    }

    return false;
    */

// console.log(flatRun([1, 2]));

// for (i = 0; i < s.length; i++)
// {
// console.log(s[1]);
// }

// for (i = 0; i < sequence.length; i++)
    // {
        // tmp = copyArraySansElement(sequence, 1);
        // console.log(sequence, tmp);
    // }

    // return false;

    // i = 6;
    // all = [];
    // tmp = [];

// function hi(i)
// {
    //return "*" + i;
// }

// console.log(all);

// console.log(solution5(s1));

// console.log(i);
    
        
        
        /*
        if (flatRun(sequence.slice(i)))
        {
            return true;
        }

        else
        {
            //
        }

tmp = copyArray(sequence);
        console.log("j: ", j, " ", tmp, " sequence.length: ", sequence.length);
        tmp = tmp.splice(i)
        console.log("j: ", j, " ", tmp);

// [1, 3, 2, 1]     // false
// [1, 3, 2]        // true

// one element outta order, cnt++
// > 1, outta order return false

*/