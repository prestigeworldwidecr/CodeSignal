/*

After becoming famous, the CodeBots decided to move into a new building together. Each of the rooms has a different cost, and some of them are free, but there's a rumour that all the free rooms are haunted! Since the CodeBots are quite superstitious, they refuse to stay in any of the free rooms, or any of the rooms below any of the free rooms.

Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms that are suitable for the CodeBots (ie: add up all the values that don't appear below a 0).

Example

For

matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
the output should be
solution(matrix) = 9.

example 1

There are several haunted rooms, so we'll disregard them as well as any rooms beneath them. Thus, the answer is 1 + 5 + 1 + 2 = 9.

For

matrix = [[1, 1, 1, 0], 
          [0, 5, 0, 1], 
          [2, 1, 3, 10]]
the output should be
solution(matrix) = 9.

example 2

Note that the free room in the final column makes the full column unsuitable for bots (not just the room directly beneath it). Thus, the answer is 1 + 1 + 1 + 5 + 1 = 9.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.array.integer matrix

A 2-dimensional array of integers representing the cost of each room in the building. A value of 0 indicates that the room is haunted.

Guaranteed constraints:
1 ≤ matrix.length ≤ 5,
1 ≤ matrix[i].length ≤ 5,
0 ≤ matrix[i][j] ≤ 10.

[output] integer

The total price of all the rooms that are suitable for the CodeBots to live in.

*/

function solution(matrix)
{
    var i = 0;
    var j = 0;
    var rowLength = matrix.length;
    var columnLength = matrix[i].length;
    cnt = 0;

    // console.log("rowLength:", rowLength, " columnLength: ", columnLength);
    // console.log("i", "\t", "j", "\t", "matrix[i][j]");

    for (i; i < rowLength; i++)
    {
        j = 0;
        
        for (j; j < columnLength; j++)
        {
            if (matrix[i][j] == 0)
            {
                for (k = i; k < rowLength; k++)
                {
                    cnt = cnt + matrix[k][j];
                }
            }

            else
            {

            }
            
        }

    }

    return cnt;

}

m1 = [[0, 1, 1, 2], 
        [0, 5, 0, 0], 
        [2, 0, 3, 3]];

m2 = [[1, 1, 1, 0], 
        [0, 5, 0, 1],
        [2, 1, 3, 10]];

console.log(solution(m1));
// printMatrix(m2);

/*

********
BONEYARD
********

*/

// console.log("row: ", i, "\tcolumn: ", j);
                // var tmp = i + ", ", j;
                // console.log("row: ", i, "\tcolumn: ", j);
                    // console.log(k, ", ", j, "\t", matrix[k][j]);
                    // k = rowLength; // break

// console.log(tmp);
            // console.log(i," \t", j);
            // tmp = "\t" + tmp
            // console.log(i, "\t", j, "\t", tmp);
            // console.log("tmp", tmp);

            // tmp = tmp + "\t" + matrix[i][j]; 
        
