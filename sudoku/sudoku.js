/*

Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 sub-grids that compose the grid contains all of the digits from 1 to 9.

This algorithm should check if the given grid of numbers represents a correct solution to Sudoku.

Example

For
grid = [[1, 3, 2, 5, 4, 6, 9, 8, 7],
        [4, 6, 5, 8, 7, 9, 3, 2, 1],
        [7, 9, 8, 2, 1, 3, 6, 5, 4],
        [9, 2, 1, 4, 3, 5, 8, 7, 6],
        [3, 5, 4, 7, 6, 8, 2, 1, 9],
        [6, 8, 7, 1, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 3, 6, 5, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be
solution(grid) = true;

For
grid = [[1, 3, 4, 2, 5, 6, 9, 8, 7],
        [4, 6, 8, 5, 7, 9, 3, 2, 1],
        [7, 9, 2, 8, 1, 3, 6, 5, 4],
        [9, 2, 3, 1, 4, 5, 8, 7, 6],
        [3, 5, 7, 4, 6, 8, 2, 1, 9],
        [6, 8, 1, 7, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 5, 6, 3, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]]
the output should be
solution(grid) = false.

The output should be false: each of the nine 3 × 3 sub-grids should contain all of the digits from 1 to 9.
These examples are represented on the image below.



Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.array.integer grid

A matrix representing 9 × 9 grid already filled with numbers from 1 to 9.

Guaranteed constraints:
grid.length = 9,
grid[i].length = 9,
1 ≤ grid[i][j] ≤ 9.

[output] boolean

true if the given grid represents a correct solution to Sudoku, false otherwise.

*/

function scanSudoku(grid, startX, endX, startY, endY)
{
    let a = [];

    for (let i = startX; i < endX; i++)
    {
        
        for (let j = startY; j < endY; j++)
        {
            a.push(grid [i][j]);
        }

    }

    return a;

}

function isSudokuCompliant(a)
{
    let result = false;
    let j = 1;

    a.sort();

    for (let i = 0; i < a.length; i++)
    {
        if (a[i] == j)
        {
            result = true;
            j++;
        }

        else
        {
            return false;
        }
    }

    return result;

}

function solution(grid) 
{
    let result1 = isSudokuCompliant(scanSudoku(grid, 0, 3, 0, 3));
    let result2 = isSudokuCompliant(scanSudoku(grid, 0, 3, 3, 6));
    let result3 = isSudokuCompliant(scanSudoku(grid, 0, 3, 6, 9));
    let result4 = isSudokuCompliant(scanSudoku(grid, 3, 6, 0, 3));
    let result5 = isSudokuCompliant(scanSudoku(grid, 3, 6, 3, 6));
    let result6 = isSudokuCompliant(scanSudoku(grid, 3, 6, 6, 9));
    let result7 = isSudokuCompliant(scanSudoku(grid, 6, 9, 0, 3));
    let result8 = isSudokuCompliant(scanSudoku(grid, 6, 9, 3, 6));
    let result9 = isSudokuCompliant(scanSudoku(grid, 6, 9, 6, 9));

    // console.log(result1 && result2 && result3 && result4 && result5 && result6 && result7 && result8 && result9);
    
    return (result1 && result2 && result3 && result4 && result5 && result6 && result7 && result8 && result9);

}

let grid =  [[1, 3, 2, 5, 4, 6, 9, 8, 7],
            [4, 6, 5, 8, 7, 9, 3, 2, 1],
            [7, 9, 8, 2, 1, 3, 6, 5, 4],
            [9, 2, 1, 4, 3, 5, 8, 7, 6],
            [3, 5, 4, 7, 6, 8, 2, 1, 9],
            [6, 8, 7, 1, 9, 2, 5, 4, 3],
            [5, 7, 6, 9, 8, 1, 4, 3, 2],
            [2, 4, 3, 6, 5, 7, 1, 9, 8],
            [8, 1, 9, 3, 2, 4, 7, 6, 5]]

        // the output should be solution(grid) = true

grid = [[1, 3, 4, 2, 5, 6, 9, 8, 7],
        [4, 6, 8, 5, 7, 9, 3, 2, 1],
        [7, 9, 2, 8, 1, 3, 6, 5, 4],
        [9, 2, 3, 1, 4, 5, 8, 7, 6],
        [3, 5, 7, 4, 6, 8, 2, 1, 9],
        [6, 8, 1, 7, 9, 2, 5, 4, 3],
        [5, 7, 6, 9, 8, 1, 4, 3, 2],
        [2, 4, 5, 6, 3, 7, 1, 9, 8],
        [8, 1, 9, 3, 2, 4, 7, 6, 5]];

        // the output should be solution(grid) = false

// console.log(isSudokuCompliant(scanSudoku(grid, 0, 3, 0, 3)));
solution(grid);

/*

********
BONEYARD
********

// s = s + grid [i][j];
// console.log(a[i])
// console.log(a);
    // console.log(s);
        // console.log(s.charAt(i));

function printMatrix(matrix)
{
    let tmp = "";

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

// s = "";
        
        // start xy, end xy
        

    let tmp =       [["x", "x", "x"],
                    ["x", "x", "x"],
                    ["x", "x", "x"]];

    // console.log(tmp);
    // printMatrix(tmp);
    // console.log(tmp.includes("1"));
// printMatrix(grid);

    tmp [0][0] = grid[0][0];
    tmp [0][1] = grid[0][1];
    tmp [0][2] = grid[0][2];
    tmp [1][0] = grid[1][0];
    tmp [1][1] = grid[1][1];
    tmp [1][2] = grid[1][2];
    tmp [2][0] = grid[2][0];
    tmp [2][1] = grid[2][1];
    tmp [2][2] = grid[2][2];

for (let i = 0; i < grid.length; i++)
    {
        let s = "";
        
        for (let j = 0; j < grid[0].length; j++)
        {
            s = s + grid[i][j];
        }

        
    }

// console.log("!");
// console.log(s);
    // console.log(tmp);
            // console.log(grid[i][j]);
// console.log("x: ", i, " y: ", j, grid [i][j]);
        // console.log(s);

*/