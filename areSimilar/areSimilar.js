/*

Two arrays are called similar if one can be obtained from another by swapping at most one pair of elements in one of the arrays.

Given two arrays a and b, check whether they are similar.

Example

For a = [1, 2, 3] and b = [1, 2, 3], the output should be
solution(a, b) = true.

The arrays are equal, no need to swap any elements.

For a = [1, 2, 3] and b = [2, 1, 3], the output should be
solution(a, b) = true.

We can obtain b from a by swapping 2 and 1 in b.

For a = [1, 2, 2] and b = [2, 1, 1], the output should be
solution(a, b) = false.

Any swap of any two elements either in a or in b won't make a and b equal.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.integer a

Array of integers.

Guaranteed constraints:
3 ≤ a.length ≤ 105,
1 ≤ a[i] ≤ 1000.

[input] array.integer b

Array of integers of the same length as a.

Guaranteed constraints:
b.length = a.length,
1 ≤ b[i] ≤ 1000.

[output] boolean

true if a and b are similar, false otherwise.

*/

/*
    *****
    STRAT
    *****

    immediate no if length not equal    x
    immediate no if sorted elements arent equal x
    immediate no if elements removed arent equal    x
    check if elements are in same position
    first strike, let pass
    2nd reject
*/

function onePairSwap(a, b)
{
    var i = 0;
    var cnt = 0;

    for (i; i < a.length; i++)
    {
        if (cnt > 2)
        {
            return false;
        }

        else
        {
            if (a[i] != b[i])
            {
                cnt++;
            }

            else
            {
                //
            }
        }
    }

    return true;
}

function removeDuplicates(s)
{
    var tmp = [...new Set(s)].join("");

    return tmp;
}

function isArrayEqual(a, b)
{
    var i = 0;
    
    for (i; i < a.length; i++)
    {
        if (a[i] != b[i])
        {
            return false;
        }

        else
        {
            //
        }
    }

    return true;
}

function areSimilar(a, b)
{
    var aCopy =  [...a];
    var bCopy =  [...b];
    
    if (a.length != b.length)
    {
        console.log("*1");
        return false;
    }

    else if (!isArrayEqual(aCopy.sort(), bCopy.sort()))
    {
        console.log("*2");
        return false;
    }

    else if (!isArrayEqual(removeDuplicates(aCopy), removeDuplicates(bCopy)))
    {
        console.log("*3");
        return false;
    }

    else
    {
        console.log("*4");
        return onePairSwap(a, b);
    }

}

function solution(a, b) 
{
    return areSimilar(a, b);
}

/*

********
BONEYARD
********


    console.log("a: ", a, " b: ", b);
    console.log("i: ", i, " a[i]: ", a [i], " b[i]", b[i], " cnt: ", cnt);

a = [832, 998, 148, 570, 533, 561, 894, 147, 455, 279];
b = [832, 570, 148, 998, 533, 561, 455, 147, 894, 279];

// aCopy.sort();
    // bCopy.sort();

console.log(areSimilar(a, b));

// a = [1, 2, 3] and b = [1, 2, 3] solution(a, b) = true.
// a = [1, 2, 3] and b = [2, 1, 3] solution(a, b) = true.
// a = [1, 2, 2] and b = [2, 1, 1] solution(a, b) = false.

// a = [1, 2, 3];
// b = [1, 2, 3];
// a = [1, 2, 3];
// b = [2, 1, 3];
// a = [1, 2, 2];
// b = [2, 1, 1];

// console.log(a == b);
// console.log(a.eq)

// console.log("*4");
        // console.log("*3");
        // else if (a.sort() != )
        // console.log("i: ", i, " cnt: ", cnt, "a[i]: ", a[i], " b[i]: ", b[i]);
        // console.log("*1");
        // console.log("*2", " a sorted: ", a.sort(), " b sorted: ", b.sort());
        // console.log("*2: ", a.sort() == b.sort());



*/