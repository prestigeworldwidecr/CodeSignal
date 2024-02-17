/*

Some people are standing in a row in a park. There are trees between them which cannot be moved. Your task is to rearrange the people by their heights in a non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.integer a

If a[i] = -1, then the ith position is occupied by a tree. Otherwise a[i] is the height of a person standing in the ith position.

Guaranteed constraints:
1 ≤ a.length ≤ 1000,
-1 ≤ a[i] ≤ 1000.

[output] array.integer

Sorted array a with all the trees untouched.

*/

function stringToIntArray(a)
{
    var i = 0;
    var tmp = new Int32Array(a.length);

    for (i; i < a.length; i++)
    {
        tmp[i] = parseInt(a[i]);
    }

    return tmp;
}

function sortedArrayNoTrees(a)
{
    var i = 0;
    var tmp = [];

    for (i; i < a.length; i++)
    {        
        if (a[i] == -1)
        {
            //
        }

        else
        {
            tmp.push(a[i]);
        }
    }

    return stringToIntArray(tmp).sort();
}

function treeLocation(a)
{
    var i = 0;
    var tmp = [];

    for (i; i < a.length; i++)
    {
        if (a[i] == -1)
        {
            tmp.push(i);
        }

        else
        {
            //
        }
    }

    return tmp;
}

function separateTrees(a, b)
{
    var i = 0;  // counter for a
    var j = 0;  // counter for b
    var k = 0;
    var l = a.length + b.length;
    var tmp = [];

    while (k < l)
    {        
        if (b[j] == k)
        {
            tmp.push(-1);
            j++;
        }

        else
        {
            tmp.push(a[i]);
            i++;
        }

        k++;
    }

    console.log(tmp);
    return tmp;
}

function solution(a) 
{
    return separateTrees(sortedArrayNoTrees(a), treeLocation(a));
}

a = [-1, 150, 190, 170, -1, -1, 160, 180]; // [-1, 150, 160, 170, -1, -1, 180, 190]
a1 = [4, 2, 9, 11, 2, 16]; 
a2 = [23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3];

solution(a2);

/*

********
BONEYARD
********

// stringToIntArray(tmp);
    // tmp[i] = parseInt(a[i]);
    // tmp = tmp.sort();
    // tmp.push(i);
    // console.log(tmp);
    // console.log(a[i]);
    // return tmp;

// tmp[k] = -1;
// tmp[k] = a[i];
// console.log("b[j]: ", b[j], " a[i]: ", a[i]);


    // var tmp = new Float64Array(a);
    // var numArray = new Float64Array([140000, 104, 99]);
    // tmp = Array.from(a, Number);

    // console.log(tmp);

// console.log(a, b);
// for (i; i < (a.length + b.length); i++)

*/