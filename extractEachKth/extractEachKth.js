/*

Given array of integers, remove each kth element from it.

Example

For inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be
solution(inputArray, k) = [1, 2, 4, 5, 7, 8, 10].

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.integer inputArray

Guaranteed constraints:
5 ≤ inputArray.length ≤ 15,
-20 ≤ inputArray[i] ≤ 20.

[input] integer k

Guaranteed constraints:
1 ≤ k ≤ 10.

[output] array.integer

inputArray without elements k - 1, 2k - 1, 3k - 1 etc.

*/

function createBullshitiTimeskMinus1Array(inputArray, k)
{
    let bs = new Array();
    let max = Math.max(...(new Int32Array(inputArray)));
    let j = max;

    if (k == 1)
    {
        for (let i = 0; i < inputArray.length; i++)
        {
            bs.push(i);
        }
    }

    else if (k == max)
    {
        for (let i = 0; i < inputArray.length; i++)
        {
            if (i == max - 1)
            {
                bs.push(i);
                max = max + j;
            }

            else
            {
                // 
            }
        }
        
    }

    else
    {
        for (let i = 1; k * i < max; i++)
        {
            bs.push(i * k - 1);
        }

    }

    return bs;

}

function buildArraySansK(inputArray, k)
{
    let j = 0;
    let result = new Array();
    let bs = createBullshitiTimeskMinus1Array(inputArray, k);

    // console.log("bs: ", bs);
        
    for (let i = 0; i < inputArray.length; i++)
    {
            
        if (i == bs[j])
        {
            j++;
        }

        else
        {
            result.push(inputArray[i]);
        }    

    }

    return result;

}

function solution(inputArray, k) 
{
    return buildArraySansK(inputArray, k);
}

// inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
// let k = 3; // the output should be solution(inputArray, k) = [1, 2, 4, 5, 7, 8, 10]
// inputArray = [1, 1, 1, 1, 1];   // answer: []
// k = 1;
// inputArray = [1, 2, 1, 2, 1, 2, 1, 2];  // answer: [1, 1, 1, 1];
// k = 2;
// inputArray = [1, 2, 1, 2, 1, 2, 1, 2];  // answer: [1, 2, 1, 2, 1, 2, 1, 2]
// k = 10;
inputArray = [2, 4, 6, 8, 10];  // answer: [2, 6, 10]
k = 2

// createBullshitiTimeskMinus1Array(inputArray, k);

solution(inputArray, k);

// buildArraySansK(inputArray, k);



/*

********
BONEYARD
********

// return buildArraySansK(inputArray, (createBullshitiTimeskMinus1Array(inputArray, k)));
buildArraySansK(inputArray, (createBullshitiTimeskMinus1Array(inputArray, k)));

// console.log(bs);
        // console.log("i: ", i, " bs[j]: ", bs[j]);
            // console.log("!", i);

solution(inputArray, k);

let j = 0;
     let bs = createBullshitiTimeskMinus1Array(inputArray, k);

     for (let i = 1; i < inputArray.length; i++)
     {

        console.log("i: ", i, " j: ", j, " bs[j]: ", bs[j], " inputArray: ", inputArray, " inputArray.length: ", inputArray.length);

        if(i == bs[j])
        {
            inputArray.splice(i, 1);
            j++;
        }

        else
        {
            // 
        }

     }

     console.log(inputArray);

function createArraySansK(inputArray, k)
{
    // k = k - 1;
    // result = [];

    for (let i = 0; i < inputArray.length; i++)
    {
        // console.log("i: ", i, " k * i: ", k * i);
        
        if (i == k * i)
        {
            // 
        }

        else
        {
            // result.push(inputArray[i]);
        }
    }

    console.log(inputArray);
}

createArraySansK(inputArray, k);

return createArraySansK(inputArray, k);

// createArrayMultiples(inputArray, k)
createArraySansK(inputArray, k);

// creates an array of k-multiples up to inputArray.length
function createArrayMultiples(inputArray, k)
{
    let tmp = "";
    let result = new Array(Math.ceil(inputArray.length / k));

    for (let i = 1; i < result.length; i++)
    {        
        tmp = i * k;
        result[i] = tmp;

        // console.log("Number.isInteger(tmp): ", Number.isInteger(tmp));
    }

    if (Number.isInteger(result[0]))
    {
        // 
    }

    else
    {
        result.splice(0, 1);
    }

    return result;
    
}

// check each entry of inputArray against array of k-multiples
function isKMultiple(element, kMult)
{
    let result = false;

    for (let i = 0; i < kMult.length; i++)
    {
        if (element == kMult[i])
        {
            return true;
        }

        else 
        {
            result = false;
        }

    }

    return result;
}

function createArraySansK(inputArray, k)
{
    let tmp = "";
    let result = new Array();
    let kMult = createArrayMultiples(inputArray, k);

    for (let i = 0; i < inputArray.length; i++)
    {
        tmp = isKMultiple(inputArray[i], kMult);
        
        console.log("tmp: ", tmp);

        if (tmp)
        {
            //
        }

        else
        {
            result.push(inputArray[i]);
        }
    }

    console.log(result);

}


let max = Math.max(...(new Int32Array(inputArray)));

result [i] = tmp;
    // return inputArray;


    // result.length = Math.ceil((max + 1) / k);

    console.log(result.length);

// solution(inputArray, k);
// createArrayMultiples(inputArray, k);

function removeEachInstance(inputArray, k)
{
    inputArray = new Int32Array(inputArray);
    inputArray.sort();
    inputArray = [...inputArray];
    
    for (let i = 0; i < inputArray.length; i++)
    {
        tmp = inputArray[i];
        
        if (k == tmp)
        {
            inputArray.splice(i, 1);
            i--;
        }

        else
        {
            //
        }

    }

    return inputArray;

}

// let index = -1;
    // let tmp = k;    // multiples of k
    

// result = removeEachInstance(inputArray, k);
    // result = processMultiples(result, k);

    // console.log(result);

    // return result;   

        index = inputArray.indexOf((i + 1) * k);
        
        if (0 <= index && index < inputArray.length)
        {
            // inputArray.splice(index, 1);
        }

        else
        {
            // 
        }

function processMultiples1(inputArray, k)
{
    let index = -1;
    let tmp = k;    // multiples of k

    for (let i = 0; i < inputArray.length; i++)
    {        
        index = inputArray.indexOf((i + 1) * k);
        
        if (0 <= index && index < inputArray.length)
        {
            inputArray.splice(index, 1);
        }

        else
        {
            // 
        }

    }

    return inputArray;
}

// console.log("!", result);
    // console.log("@", result);
    
    // console.log(removeEachInstance(inputArray, k));
    // processMultiples(inputArray, k);

    // console.log("!");

// console.log(removeEachInstance(inputArray, k));
// console.log(processMultiples(removeDuplicatesIntegerArray(inputArray), k));

// inputArray = [...inputArray];
    // inputArray = inputArray.sort();
    // let len = inputArray.length;
    // console.log(inputArray);
    // console.log(inputArray);

        // console.log("tmp: ", tmp, " i: ", i, " k: ", k);
            // console.log("!");
            // console.log(inputArray.length);
            // inputArray.length = inputArray.length - 1;
            // i--;
    // console.log(inputArray);

// console.log(inputArray);

function removeDuplicatesIntegerArray(inputArray)
{
    let tmp = new Int32Array(inputArray);
    tmp = tmp.sort();    
    tmp = [...new Set(tmp)].join(",");
    tmp = tmp.split(",");
    tmp = new Int32Array(tmp);

    return tmp;
}

// removeDuplicatesIntegerArray(inputArray);

// const i = inputArray.indexOf(1000);
    // inputArray.splice(i, 1);
    // console.log("k: ", k, " inputArray: ", inputArray, " inputArray.length: ", inputArray.length);
        // console.log("i + 1", i + 1, " k: ", k, "(i + 1) * k:", (i + 1) * k, " index: ", index, " inputArray[i]): ", inputArray[i]);

// let tmp = inputArray.toString();
    // tmp = new Array(tmp);

    // console.log(tmp);

// console.log(removeDuplicates(inputArray.sort()));

if (inputArray[i] == k)
        {
            console.log("!");
            
            index = inputArray.indexOf(inputArray[i]);
            inputArray.splice(index, 1);
        }
        
        else 

    const i = inputArray.indexOf(k);
    inputArray.splice(i, 1);
    
    return inputArray;

*/