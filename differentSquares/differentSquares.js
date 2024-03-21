/*

Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
solution(matrix) = 6.

Here are all 6 different 2 × 2 squares:

1 2
2 2

2 1
2 2

2 2
2 2

2 2
1 2

2 2
2 3

2 3
2 1

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.array.integer matrix

Guaranteed constraints:
1 ≤ matrix.length ≤ 100,
1 ≤ matrix[i].length ≤ 100,
0 ≤ matrix[i][j] ≤ 9.

[output] integer

The number of different 2 × 2 squares in matrix.

*/

function is2x2Different(m1, m2)
{
    var result = false;
    
    for (var i = 0; i < 2; i++)
    {
        for (var j = 0; j < 2; j++)
        {
            if (m1 [i] [j] != m2 [i] [j])
            {
                return false;
            }

            else
            {
                result = true;
            }
        }

    }

    return result;
}

function printMatrix(matrix)
{
    var tmp = "";

    console.log("matrix[i][j]");
    console.log("============");

    for (var i = 0; i < matrix.length; i++)
    {
        tmp = "";

        for (var j = 0; j < matrix[0].length; j++)
        {
            tmp = tmp + matrix[i][j] + "\t";
        }

        console.log(tmp);

    }

}

function createAll2x2s(matrix)
{
    // var tmp = [ [1, 2],
    //             [3, 4]];

    const all2x2s = new Array();
    var cnt = 0;

    for (var i = 0; i < matrix.length - 1; i++)
    {
        var tmp = [ [0, 0],
                    [0, 0]];

        for (var j = 0; j < matrix[0].length - 1; j++)
        {
            tmp[0][0] = matrix[i][j];
            tmp[0][1] = matrix[i][j + 1];
            tmp[1][0] = matrix[i + 1][j];
            tmp[1][1] = matrix[i + 1][j + 1];
            console.log(tmp, "cnt:", cnt);
            all2x2s.push(tmp);
            // cnt++;
        }

    }

    console.log(all2x2s[1]);

}

function solution(matrix) 
{

}

var matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],    // height: 5
          [1, 2, 3],    // width: 3
          [2, 2, 1]];   // the output should be solution(matrix) = 6.

var m1 = [  [1, 1],
        [1, 1]  ];
var m2 = [  [2, 2],
        [2, 2]  ];

matrix = [  [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],    // height: 5
            [10, 11, 12],    // width: 3
            [13, 14, 15]];   // the output should be solution(matrix) = 6.

// console.log(is2x2Different(m1, m1));
// printMatrix(matrix);
createAll2x2s(matrix);

/*

********
BONEYARD
********

// tmp = ;
        // const all2x2s = new Array();
    // all2x2s.push(1);
    // console.log(all2x2s.includes(1));
            // all2x2s.push(tmp);
        // console.log(tmp);
        // all2x2s.push(tmp);

    // console.log(tmp);

    console.log(matrix[0][0]);
    console.log(matrix[0][1]);
    console.log(matrix[1][0]);
    console.log(matrix[1][1]);

    // printMatrix(tmp);

sumof2x2s(matrix);

function sumof2x2s(matrix)
{
    var width = matrix[0].length;
    var height = matrix.length;

    console.log("width: ", width, " height: ", height);
    
    // console.log(matrix);
}

*/