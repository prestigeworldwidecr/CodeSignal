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
    let tmp = "";

    console.log("matrix[i][j]");
    console.log("============");

    for (let i = 0; i < matrix.length; i++)
    {
        tmp = "";

        for (let j = 0; j < matrix[0].length; j++)
        {
            tmp = tmp + matrix[i][j] + "\t";
        }

        console.log(tmp);

    }

}

function createAll2x2s(matrix)
{
    const all2x2s = new Array();

    for (let i = 0; i < matrix.length - 1; i++)
    {
        for (let j = 0; j < matrix[0].length - 1; j++)
        {
            let tmp = [ [1, 2],
                        [3, 4]];

            tmp[0][0] = matrix[i][j];
            tmp[0][1] = matrix[i][j + 1];
            tmp[1][0] = matrix[i + 1][j];
            tmp[1][1] = matrix[i + 1][j + 1];

            // console.log(all2x2s.includes(tmp), tmp);
            
            all2x2s.push(tmp);
        }

    }

    return all2x2s;

}

function differentSquares(a)
{
    // a = [...new Set(a)].join("");
    // console.log(a.toString());
    let tmp = a.toString();
    let i = 0;
    // for (let i = 0; i % 4 == 0; i++)
    console.log(tmp.length)
    while (i < tmp.length)
    {
        // console.log(i);
        i = i + 4;
    }

}

function solution(matrix) 
{
    
}

let matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],    // height: 5
          [1, 2, 3],    // width: 3
          [2, 2, 1]];   // the output should be solution(matrix) = 6.

let m1 = [  [1, 1],
        [1, 1]  ];
let m2 = [  [2, 2],
        [2, 2]  ];

let matrix1 = [ [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],    // height: 5
                [10, 11, 12],    // width: 3
                [13, 14, 15]];   // the output should be solution(matrix) = 6.

let tmp = createAll2x2s(matrix);
differentSquares(tmp);

/*

********
BONEYARD
********


function removeDuplicates(s)
{
    let tmp = [...new Set(s)].join("");

    return tmp;
}

// let tmp = createAll2x2s
    // const result =

    
    // return result;
// console.log(is2x2Different(m1, m1));
// printMatrix(matrix);
// createAll2x2s(matrix);

// console.log(i, j, tmp);
        // all2x2s(i) = tmp;
    // console.log(all2x2s);

 // all2x2s.length = (matrix.length - 1) * (matrix[0].length - 1);
    // console.log(all2x2s.length);

// console.log(tmp, "cnt:", cnt);
            // all2x2s.push(tmp);
            // console.log("(", i, ",", j, ")", "(", i, ",", j + 1, ")", "(", i + 1, ",", j, ")", "(", i + 1, ",", j + 1, ")");
            // console.log(matrix[i][j], "\t", matrix[i][j + 1], "\t", matrix[i + 1][j], "\t", matrix[i + 1][j + 1])
            // cnt++;
            // console.log(tmp[0][0], tmp[0][1], tmp[1][0], tmp[1][1]);

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