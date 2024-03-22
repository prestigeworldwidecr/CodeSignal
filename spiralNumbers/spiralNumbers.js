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

    // printMatrix(m);

    return m;
}

function spiralNumbers(n)
{
    let m = createNxNArray(n); 
    let cnt = 1;
    let rightBorderX = 0;
    let rightBorderY = m.length;
    let downBorderX = m.length - 1;
    let downBorderY = 0;
    let leftBorderX = m.length - 1;
    let leftBorderY = 0;
    let upBorderX = m.length - 1;
    let upBorderY = 0;

    // for (let i = 0; i < Math.pow(m.length, 2); i++)
    while (cnt <= Math.pow(m.length, 2) && cnt > 0)
    {
        // console.log(cnt);       
        
        cnt = moveRight(m, cnt, rightBorderX, rightBorderY);
        rightBorderX++;
        rightBorderY--;
        
        if (cnt <= Math.pow(m.length, 2) && downBorderX < m.length && downBorderY >= 0)
        {
            // console.log(i);
            
            cnt = moveDown(m, cnt - 1, downBorderX, downBorderY);
            downBorderX++;
            downBorderY--;
        }

        else
        {
            
        }

        if (cnt <= Math.pow(m.length, 2)) // && leftBorderX >= 0 && leftBorderX < m.length)
        {
            cnt = moveLeft(m, cnt - 1, leftBorderX, leftBorderY);
            leftBorderX--;
            leftBorderY++;
        }

        else
        {

        }

        if (cnt <= Math.pow(m.length, 2)) // && upBorderX >= 0 && upBorderY < m.length)
        {
            cnt = moveUp(m, cnt - 1, upBorderX, upBorderY);
            upBorderX--;
            upBorderY++;
        }

        else
        {

        }

    }
    
    printMatrix(m);
    // return m;

}

function moveRight(a, cnt, rightBorderX, rightBorderY)
{

    for (let i = rightBorderX; i < rightBorderY; i++)
    {
        a [rightBorderX] [i] = cnt++;
    }

    return cnt;
}

function moveDown(a, cnt, downBorderX, downBorderY)
{

    for (let i = downBorderY; i < downBorderX; i++)
    {
        // console.log("i:", i, "cnt:", cnt, "downBorderX:", downBorderX, "downBorderY:", downBorderY);
        a [i] [downBorderX] = cnt;
        cnt++;
    }

    return cnt;
}

function moveLeft(a, cnt, leftBorderX, leftBorderY)
{

    for (let i = leftBorderX; i >= leftBorderY; i--)
    {
        a [leftBorderX] [i] = cnt;
        cnt++;
    }

    return cnt;
}

function moveUp(a, cnt, upBorderX, upBorderY)
{

    for (let i = upBorderX; i > upBorderY; i--)
    {
        a [i] [upBorderY] = cnt;
        cnt++;
    }

    return cnt;
}

function solution(n) 
{
    return spiralNumbers(n);
}

let n = 3;  // the output should be solution(n) =  [[1, 2, 3],
//                                                  [8, 9, 4],
//                                                  [7, 6, 5]]


spiralNumbers(3);

/*



********
BONEYARD
********

var spiral =    [moveRight(m, 1, rightBorderX, rightBorderY), 
        moveDown(m, cnt - 1, downBorderX, downBorderY), 
        moveLeft(m, cnt - 1, leftBorderX, leftBorderY),
        moveUp(m, cnt - 1, upBorderX, upBorderY)];
    spiral[0](m, 1, rightBorderX, rightBorderY);

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
        a [i] [0] = cnt;
        cnt++;
    }

    return cnt;
}

console.log(i, cnt);
        
// createNxNArray(n);
// console.log(i, cnt);
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