/*

Construct a square matrix with a size N × N containing integers from 1 to N * N in a spiral order, starting from top-left and in clockwise direction.

Example

For n = 3, the output should be

solution(n) = [[1, 2, 3],
               [8, 9, 4],
               [7, 6, 5]]
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

Matrix size, a positive integer.

Guaranteed constraints:
3 ≤ n ≤ 100.

[output] array.array.integer

*/

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

function createNxNArray(n)
{
    let m = new Array();
    
    for (let i = 0; i < n; i++)
    {
        m [i] = new Array();
        
        for (let j = 0; j < n; j++)
        {
            m [i] [j] = "x";
        }

    }

    // console.log(a);

    return m;
}

function spiralNumbers(n)
{
    let m = createNxNArray(n); 
    let cnt = moveRight(m, 1);

    cnt = moveDown(m, cnt - 1);
    cnt = moveLeft(m, cnt - 1);
    cnt = moveUp(m, cnt - 1);
    printMatrix(m);
}

function moveRight(a, cnt)
{

    for (let i = 0; i < a.length; i++)
    {
        a [0] [i] = cnt++;
    }

    return cnt;
}

function moveDown(a, cnt)
{

    for (let i = 0; i < a.length; i++)
    {
        a [i] [a.length - 1] = cnt;
        cnt++;
    }

    return cnt;
}

function moveLeft(a, cnt)
{

    for (let i = a.length - 1; i >= 0; i--)
    {
        console.log(i, cnt);
        a [a.length - 1] [i] = cnt;
        cnt++;
    }

    return cnt;
}

function moveUp(a, cnt)
{

    for (let i = a.length - 1; i > 0; i--)
    {
        console.log(i, cnt);
        a [i] [a.length - 1] = cnt;
        cnt++;
    }

    return cnt;
}

function solution(n) 
{

}

let n = 3;  // the output should be solution(n) =  [[1, 2, 3],
//                                                  [8, 9, 4],
//                                                  [7, 6, 5]]


// createNxNArray(n);
spiralNumbers(n);

/*

********
BONEYARD
********

// console.log("$");
        // console.log("i:", i, "r:", r, "c:", c);
    // console.log("$");
        // console.log("i:", i, "r:", r, "c:", c);
// console.log("!", m);
    // console.log("@", m);
    // m = moveDown(m, 0, 3, 4);
    // console.log("#");
        // console.log("i:", i, "r:", r, "c:", c);
    // console.log(a);
    // console.log("#");

*/