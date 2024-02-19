/*

Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

solution(picture) = ["*****",
                     "*abc*",
                     "*ded*",
                     "*****"]
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.string picture

A non-empty array of non-empty equal-length strings.

Guaranteed constraints:
1 ≤ picture.length ≤ 100,
1 ≤ picture[i].length ≤ 100.

[output] array.string

The same matrix of characters, framed with a border of asterisks of width 1

*/

function addBorder(picture)
{
    var i = 0;
    var tmp = "";
    var bottomTopBorder = "**";
    var result = [];
    
    for (i; i < picture[0].length; i++)
    {
        bottomTopBorder = bottomTopBorder + "*";
    }

    result.push(bottomTopBorder);

    for (i = 0; i < picture.length; i++)
    {
        tmp = "*" + picture[i] + "*";
        result.push(tmp);
    }

    result.push(bottomTopBorder);

    return result;
}

function solution(picture) 
{
    // return addBorder(picture);
}

picture = ["abc",
            "ded"];

// console.log(picture);
console.log(addBorder(picture));

/*

********
BONEYARD
********

picture = ["abc",
            "ded"];

addBorder(picture);

// solution(picture) = ["*****",
//                      "*abc*",
//                      "*ded*",
//                      "*****"];

// console.log("i: ", picture[i]);
    // console.log(result);

*/