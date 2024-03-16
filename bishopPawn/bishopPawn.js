/*

Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:

Example

For bishop = "a1" and pawn = "c3", the output should be
solution(bishop, pawn) = true

For bishop = "h1" and pawn = "h3", the output should be
solution(bishop, pawn) = false

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string bishop

Coordinates of the white bishop in the chess notation.

Guaranteed constraints:
bishop.length = 2,
'a' ≤ bishop[0] ≤ 'h',
1 ≤ bishop[1] ≤ 8.

[input] string pawn

Coordinates of the black pawn in the same notation.

Guaranteed constraints:
pawn.length = 2,
'a' ≤ pawn[0] ≤ 'h',
1 ≤ pawn[1] ≤ 8.

[output] boolean

true if the bishop can capture the pawn, false otherwise.

*/

function slopeBetweenTwoPoints(pos1, pos2)
{
    var m = Number.MIN_SAFE_INTEGER;

    m = pos2 [1] - pos1 [1] / pos2 [0] - pos1 [0]   // slope equation: y2-y1/x2-x1
}

// convert chess position letter, number to [x, y]
function convertXYPosition(pos)
{
    var x = pos.charAt(0);
    var y = Number(pos.charAt(1));
    var xyPos = [-1, -1];

    switch (x)
    {
        case 'a':
            x = 1;
            break;
        case 'A':
            x = 1;
            break;
        case 'b':
            x = 2;
            break;
        case 'B':
            x = 2;
            break;
        case 'c':
            x = 3;
            break;
        case 'C':
            x = 3;
            break;
        case 'd':
            x = 4;
            break;
        case 'D': 
            x = 4;
            break;
        case 'e':
            x = 5;
            break;
        case 'E':
            x = 5;
            break;
        case 'f':
            x = 6;
            break;
        case 'F':
            x = 6;
            break;
        case 'g':
            x = 7;
            break;
        case 'G':
            x = 7;
            break;
        case 'h':
            x = 8;
            break;
        case 'H': 
            x = 8;
            break;          
    }

    xyPos[0] = Number(x);
    xyPos[1] = y;

    return xyPos;
        
}

function solution(bishop, pawn) 
{

}

var bishop = "a1";  // 146
var pawn = "c3";    // 150  the output should be solution(bishop, pawn) = true

var bishop = "h1";   // 153
var pawn = "h3";    // 155     the output should be solution(bishop, pawn) = false

// good
var bishop = "c4";  // 151
var pawn = "f7";    // 157

var bishop = "e8";  // 157
var pawn = "a4";    // 149

// bad
var bishop = "c4";  // 151
var pawn = "f7";    // 157

var bishop = "e8";  // 157
var pawn = "a4";    // 149

console.log(convertXYPosition(bishop));

/*

********
BONEYARD
********

console.log(pos);
    console.log(pos.charAt(0));
    console.log(pos.charAt(1));

chessCheckPosition (bishop, pawn);

function chessCheckPosition(bishop, pawn)
{
    var numBishop = bishop.charCodeAt(0) + bishop.charCodeAt(1);
    var numPawn = pawn.charCodeAt(0) + pawn.charCodeAt(1);
    // let result = "";

    console.log("numBishop: ", numBishop, " numPawn: ", numPawn);

    if (val1 % 2 == 0 && val2 % 2 == 0)
    {
        result = true;
    }

    else if (val1 % 2 == 1 && val2 % 2 == 1)
    {
        result = true;
    }

}

*/