/*

Given integers a and b, determine whether the following pseudocode results in an infinite loop

while a is not equal to b do
  increase a by 1
  decrease b by 1
Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.

Example

For a = 2 and b = 6, the output should be
solution(a, b) = false;
For a = 2 and b = 3, the output should be
solution(a, b) = true.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer a

Guaranteed constraints:
0 ≤ a ≤ 20.

[input] integer b

Guaranteed constraints:
0 ≤ b ≤ 20.

[output] boolean

true if the pseudocode will never stop, false otherwise.

*/

function isInfiniteProcess(a, b)
{
    let flag = a > b;
    let cur = "";
    let result = false;
    let cnt = 0;

    do
    {
        if (a == b)
        {
            return false;
        }
        
        else if (flag != cur)
        {
            return true;
        }

        else
        {
            result = false;
            a++;
            b--;
            cur = a > b;
        }

    } while (a != b);

    return result;

}

function solution(a, b) 
{
    return isInfiniteProcess(a, b);
}

let a = 2;
let b = 6;      // the output should be solution(a, b) = false;
a = 2;
b = 3;      // the output should be solution(a, b) = true.
a = 3;
b = 1;      // the output should be solution(a, b) = true.
a = 10;
b = 10;      // the output should be solution(a, b) = false

console.log(isInfiniteProcess(a, b)); 

/*

********
BONEYARD
********



        if (a == b)
        {
            return false;
        }

        else if (cnt == 20)
        {
            return true;
        }

        cnt++;

    while (a != b)
    {
        if (a + 1 == b)
        {
            return false;
        }

        else if (a = b - 1)
        {
            return false;
        }

        else if (cnt == 20)
        {
            return false;
        }

        else
        {
            a++;
            b--;
            result = true;
        }
        
    }

// let result = true;
    
// console.log(a, b);
                // a++;

while a is not equal to b do
  increase a by 1
  decrease b by 1


*/