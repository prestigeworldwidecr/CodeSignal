/*

Given a position of a knight on the standard chessboard, find the number of different moves the knight can perform.

The knight can move to a square that is two squares horizontally and one square vertically, or two squares vertically and one square horizontally away from it. The complete move therefore looks like the letter L. Check out the image below to see all valid moves for a knight piece that is placed on one of the central squares.

Example

For cell = "a1", the output should be
solution(cell) = 2.

For cell = "c2", the output should be
solution(cell) = 6.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string cell

String consisting of 2 letters - coordinates of the knight on an 8 × 8 chessboard in chess notation.

Guaranteed constraints:
cell.length = 2,
'a' ≤ cell[0] ≤ 'h',
1 ≤ cell[1] ≤ 8.

[output] integer

*/

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

function countMoves(xyPos)
{
    var moves = [ [xyPos[0] - 2, xyPos[1] + 1], 
                  [xyPos[0] - 1, xyPos[1] + 2],
                  [xyPos[0] + 1, xyPos[1] + 2], 
                  [xyPos[0] + 2, xyPos[1] + 1],    
                  [xyPos[0] + 2, xyPos[1] - 1], 
                  [xyPos[0] + 1, xyPos[1] - 2],
                  [xyPos[0] - 1, xyPos[1] - 2], 
                  [xyPos[0] - 2, xyPos[1] - 1] ];

    for (var i = 0; i < moves.length; i++)
    {
        console.log(moves[i]);
    }
                  
}

function solution(cell) 
{

}

var cell = "a1"; //the output should be solution(cell) = 2.
var cell = "c2"; // the output should be solution(cell) = 6.

console.log(convertXYPosition(cell));

/*

********
BONEYARD
********

*/