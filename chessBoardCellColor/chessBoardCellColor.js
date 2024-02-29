/*

Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
solution(cell1, cell2) = true.

For cell1 = "A1" and cell2 = "H3", the output should be
solution(cell1, cell2) = false.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string cell1

Guaranteed constraints:
cell1.length = 2,
'A' ≤ cell1[0] ≤ 'H',
1 ≤ cell1[1] ≤ 8.

[input] string cell2

Guaranteed constraints:
cell2.length = 2,
'A' ≤ cell2[0] ≤ 'H',
1 ≤ cell2[1] ≤ 8.

[output] boolean

true if both cells have the same color, false otherwise.

*/

function chessBoardCellColor(cell1, cell2)
{
    let val1 = cell1.charCodeAt(0) + cell1.charCodeAt(1);
    let val2 = cell2.charCodeAt(0) + cell2.charCodeAt(1);
    let result = "";

    // console.log("val1: ", val1, " val2: ", val2);

    if (val1 % 2 == 0 && val2 % 2 == 0)
    {
        result = true;
    }

    else if (val1 % 2 == 1 && val2 % 2 == 1)
    {
        result = true;
    }

    else
    {
        result = false;
    }

    return result;

}

function solution(cell1, cell2) 
{
    return chessBoardCellColor(cell1, cell2);
}

let cell1 = "A1";
let cell2 = "C3";    // the output should be solution(cell1, cell2) = true

let cell3 = "A1"; 
let cell4 = "H3";    // the output should be solution(cell1, cell2) = false

console.log(chessBoardCellColor(cell3, cell4));

/*

********
BONEYARD
********

STRAT
-----

ASCII 65-72
ABCDEFGH

12345678
ASCII 49-57

A1  11  2
C3  33  6

A1  11  2
H3  83  11

*/