/*

In the popular Minesweeper game you have a board with some mines and those cells that don't contain a mine have a number in it that indicates the total number of mines in the neighboring cells. Starting off with some arrangement of mines we want to create a Minesweeper game setup.

Example

For

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]]
the output should be

solution(matrix) = [[1, 2, 1],
                    [2, 1, 1],
                    [1, 1, 1]]
Check out the image below for better understanding:



Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.array.boolean matrix

A non-empty rectangular matrix consisting of boolean values - true if the corresponding cell contains a mine, false otherwise.

Guaranteed constraints:
2 ≤ matrix.length ≤ 100,
2 ≤ matrix[0].length ≤ 100.

[output] array.array.integer

Rectangular matrix of the same size as matrix each cell of which contains an integer equal to the number of mines in the neighboring cells. Two cells are called neighboring if they share at least one corner.

*/

function countNeighbors(matrix, i, j)
{
    cnt = 0;
    // tmp = [i, j];

    // up
    // [i - 1] [j]
    if (i - 1 >= 0)
    {
        cnt = matrix [i - 1] [j] ? cnt + 1 : cnt;
    }

    else
    {
        //
    }

    // down
    // [i + 1] [j]
    if (i + 1 < matrix.length)
    {
        cnt = matrix [i + 1] [j] ? cnt + 1 : cnt;
    }

    else
    {
        //
    }

    // left
    // [i] [j - 1]
    if (j - 1 >= 0)
    {
        cnt = matrix [i] [j - 1] ? cnt + 1 : cnt;
    }

    else
    {
        //
    }

    // right
    // [i] [j + 1]
    if (j + 1 < matrix[0].length)
    {
        cnt = matrix [i] [j + 1] ? cnt + 1 : cnt;
    }

    else
    {
        //
    }

    // up-left
    // [i - 1] [j - 1]
    if (i - 1 >= 0 && j - 1 >= 0)
    {
        cnt = matrix [i - 1] [j - 1] ? cnt + 1 : cnt;
    }

    else
    {
        // 
    }

    // up-right
    // [i - 1] [j + 1]
    if (i - 1 >= 0 && j + 1 < matrix[0].length)
    {
        cnt = matrix [i - 1] [j + 1] ? cnt + 1 : cnt;
    }

    else
    {
        // 
    }

    // down-left
    // [i + 1] [j - 1]
    if (i + 1 < matrix.length && j - 1 >= 0)
    {
        cnt = matrix [i + 1] [j - 1] ? cnt + 1 : cnt;
    }

    else
    {
        // 
    }

    // down-right
    // [i + 1] [j + 1]
    if (i + 1 < matrix.length && j + 1 < matrix[0].length)
    {
        cnt = matrix [i + 1] [j + 1] ? cnt + 1 : cnt;
    }

    else
    {
        // 
    }

    return cnt;

}

function sweepMines(matrix)
{
    let row = matrix.length;
    let column = matrix[0].length;
    // let mineMap = [...matrix];
    let mineMap = [row];
    let cnt = 0;
    let tmp = 0;
    
    for (let i = 0; i < row; i++)
    {
        mineMap[i] = [column];

        for (let j = 0; j < column; j++)
        {
            tmp = countNeighbors(matrix, i, j);
            mineMap [i][j] = tmp;
            // console.log("matrix[", i, "][", j, "]: ", matrix[i][j], " neighbors: ", tmp);
            // tmp = countNeighbors(matrix, i, j);
            // console
        }
    }

    return mineMap;
}

function solution(matrix) 
{
    return sweepMines(matrix);
}

matrix = [[true, false, false],
          [false, true, false],
          [false, false, false]];

/*
// the output should be 
solution(matrix) = [[1, 2, 1],
                    [2, 1, 1],
                    [1, 1, 1]]
*/

// console.log(countNeighbors(matrix, 0, 1));
console.log(sweepMines(matrix));

/*

********
BONEYARD
********

// console.log(tmp, matrix[i] [j]);

    // (1+1==2) ? "Pass" : "Fail"

*/