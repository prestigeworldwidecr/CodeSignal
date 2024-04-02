/*

Implement the missing code, denoted by ellipses. You may not modify the pre-existing code.
In order to stop the Mad Coder evil genius you need to decipher the encrypted message he sent to his minions. The message contains several numbers that, when typed into a supercomputer, will launch a missile into the sky blocking out the sun, and making all the people on Earth grumpy and sad.

You figured out that some numbers have a modified single digit in their binary representation. More specifically, in the given number n the kth bit from the right was initially set to 0, but its current value might be different. It's now up to you to write a function that will change the kth bit of n back to 0.

Example

For n = 37 and k = 3, the output should be
solution(n, k) = 33.

3710 = 1001012 ~> 1000012 = 3310.

For n = 37 and k = 4, the output should be
solution(n, k) = 37.

The 4th bit is 0 already (looks like the Mad Coder forgot to encrypt this number), so the answer is still 37.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer n

Guaranteed constraints:
0 ≤ n ≤ 231 - 1.

[input] integer k

The 1-based index of the changed bit (counting from the right).

Guaranteed constraints:
1 ≤ k ≤ 31.

[output] integer

*/

function killKthBit(n, k)
{
    let tmp = n.toString(2).split("");
    let s = "";
    
    tmp[tmp.length - k] = '0';

    for (let i = 0; i < tmp.length; i++)
    {
        s = s + tmp[i];
    }

    s = parseInt(s, 2);
    
    // console.log(s);
    return s;
}

function solution(n, k) 
{
    // return killKthBit(n, k);
    return (function (n, k) {
        return "hello";
    });
}

let n = 37;
let k = 3;      // the output should be solution(n, k) = 33.

n = 37;
k = 4;          // the output should be solution(n, k) = 37.

console.log(solution(n, k));

/*

********
BONEYARD
********

// console.log(parseInt(tmp, 2));
    

    // console.log(tmp[tmp.length - k]);
    // tmp[tmp.length - k] = 0;

    // tmp = tmp.join();
    // tmp = tmp.replace(",");

let tmp = n.toString(2).split("").reverse();
    let result = "";

    tmp[2] = Number(0);
    tmp.reverse();
    // tmp.join();
    // console.log(tmp);
    

    for (let i = tmp.length - 1; i >= 0; i--)
    {
        result = result + tmp[i];
    }

    // result = result.reverse();
    result = parseInt(result, 2);
    console.log(result);
    return result;

// console.log(result[k - 1]);

function digittoBinary(n)
{
    
    let binary = n.toString(2);

    console.log(binary);
}

*/