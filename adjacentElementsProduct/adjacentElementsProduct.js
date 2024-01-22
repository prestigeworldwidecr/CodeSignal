// adjacentElementsProduct.js

/*

Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

7 and 3 produce the largest product.

*/

function solution(inputArray)
{
    i = 0;
    j = 1;
    tmp = 0;
    maxProduct = -999999;
    
    for (i; i < inputArray.length - 1; i++)
    {
        console.log("i: ", i, " j: ", j, " maxProduct: ", maxProduct);
        
        if (j == inputArray.length)
        {
            return maxProduct;
        }

        else
        {
            tmp = inputArray[i] * inputArray[j];

            if (tmp > maxProduct)
            {
                maxProduct = tmp;
            }

            else
            {
                // 
            }
        }

        j++;
    }

    return maxProduct;
}

tmp = [3, 6, -2, -5, 7, 3];
// console.log(tmp);
console.log(solution(tmp));