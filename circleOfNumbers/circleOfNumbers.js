/*

Consider integer numbers from 0 to n - 1 written down along the circle in such a way that the distance between any two neighboring numbers is equal (note that 0 and n - 1 are neighboring, too).

Given n and firstNumber, find the number which is written in the radially opposite position to firstNumber.

Example

For n = 10 and firstNumber = 2, the output should be
solution(n, firstNumber) = 7.



Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

A positive even integer.

Guaranteed constraints:
4 ≤ n ≤ 20.

[input] integer firstNumber

Guaranteed constraints:
0 ≤ firstNumber ≤ n - 1.

[output] integer

*/

function circleOfNumbers(n, firstNumber)
{
    let diameter = n / 2;
    let result = -1;
    
    // console.log(diameter);

    if (firstNumber < diameter)
    {
        result = firstNumber + diameter;
    }

    else if (firstNumber >= diameter)
    {
        result = firstNumber - diameter;
    }

    else
    {
        //
    }
    
    return result;

}

function solution(n, firstNumber) 
{
    return circleOfNumbers(n, firstNumber);
}

let n = 10
let firstNumber = 2  // output should be solution(n, firstNumber) = 7.

console.log(solution(n, firstNumber));

/*

********
BONEYARD
********

*/