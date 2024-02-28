/*

Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.

The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself. All the pixels on the border of x are then removed.

Return the blurred image as an integer, with the fractions rounded down.

Example

For

image = [[1, 1, 1], 
         [1, 7, 1], 
         [1, 1, 1]]
the output should be solution(image) = [[1]].

To get the value of the middle pixel in the input 3 × 3 square: (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1. The border pixels are cropped from the final result.

For

image = [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]
the output should be

solution(image) = [[5, 4], 
                   [4, 4]]
There are four 3 × 3 squares in the input image, so there should be four integers in the blurred output. To get the first value: (7 + 4 + 0 + 5 + 6 + 2 + 6 + 10 + 7) = 47 / 9 = 5.2222 = 5. The other three integers are obtained the same way, then the surrounding integers are cropped from the final result.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.array.integer image

An image, stored as a rectangular matrix of non-negative integers.

Guaranteed constraints:
3 ≤ image.length ≤ 100,
3 ≤ image[0].length ≤ 100,
0 ≤ image[i][j] ≤ 255.

[output] array.array.integer

A blurred image represented as integers, obtained through the process in the description.

*/

function runBlocks(image)
{
    // 3 x 3 => 1 x 1
    // 4 x 4 => 2 x 2
    // 5 x 5 => 3 x 3

    let i = 0;
    let j = 0;
    let rowLength = image.length - 2;
    let columnLength = image[0].length - 2;
    let result = [rowLength];
    let tmp = -1;

    // console.log("rowLength: ", " columnLength: " , rowLength, columnLength);
    console.log("i\tj\tj\tj + 1\tj + 2\ti\ti + 3");
    console.log("-\t-\t-\t-----\t-----\t-\t-----");

    for (j; j < rowLength; j++)
    {
        i = 0;
        result[j] = [columnLength];

        console.log(i, "\t", j, "\t", j, "\t", j + 1, "\t", j + 2, "\t", i, "\t", i + 3);
        
        for (i; i < columnLength; i++)
        {
            tmp = [ image[j].slice(i, i + 3), image[j + 1].slice(i, i + 3), image[j + 2].slice(i, i + 3) ];
            result [j][i] = avgOfThreeByThree(tmp);
        }
    }

    return result;
}

function avgOfThreeByThree(image)
{
    let i = 0;
    let j = 0;
    let rowLength = 3;    // image.length;
    let columnLength = 3; // image[i].length;
    let avg = -1;
    let sum = 0;

    for (j; j < columnLength; j++)
    {
        i = 0;
        
        for (i; i < rowLength; i++)
        {
            sum = sum + image[i][j];
        }
    }

    avg = sum / 9;
    
    return Math.floor(avg);
    
}


function solution(image) 
{

}

let image1 = [[1, 1, 1], 
            [1, 7, 1], 
            [1, 1, 1]];    // the output should be solution(image) = [[1]]

let image2 = [[0, 18, 9], 
        [27, 9, 0], 
        [81, 63, 45]];  // [[28]]

let image3 = [[7, 4, 0, 1], 
         [5, 6, 2, 2], 
         [6, 10, 7, 8], 
         [1, 4, 2, 0]]; // the output should be solution(image) = [[5, 4], 
                                                                    // [4, 4]]

let image4 = [[36, 0, 18, 9], 
        [27, 54, 9, 0], 
        [81, 63, 72, 45]]; // [[40,30]]

console.log(runBlocks(image4)); // [ [ 40, 30 ] ]

/*

********
BONEYARD
********

// let tmp1 = -1;

// console.log("Math.floor(avg): ", Math.floor(avg));

// let tmp = -1;

// tmp = [ image[1].slice(1, 4), image[2].slice(1, 4), image[3].slice(1, 4) ]; // 4th block
// [ [ 6, 2, 2 ], [ 10, 7, 8 ], [ 4, 2, 0 ] ]
                                                  
// console.log(tmp);

// console.log(i, "\t", j, "\t", j, "\t", j + 1, "\t", j + 2, "\t", i, "\t", i + 3);
                // result = new Array(rowLength * columnLength);
            // console.log("rowLength: ", " columnLength: " , result.length, result[0].length);
            // console.log("i\tj\tj\tj + 1\tj + 2\ti\ti + 3");
            // console.log("-\t-\t-\t-----\t-----\t-\t-----");
                // console.log(tmp);
                // tmp1 = avgOfThreeByThree(tmp);
                // console.log("tmp1: ", tmp1);

function threeByThree(image)
{

}

// console.log(avgOfThreeByThree(image));

// console.log(runBlocks(image));

// sum = sum + image[i][j];

                //** tmp = [ (image.slice(0, 3) [0]).slice(0, 3), (image.slice(0, 3) [1]).slice(0, 3), (image.slice(0, 3) [2]).slice(0, 3) ];

tmp = [ image[0].slice(0, 3), image[1].slice(0, 3), image[2].slice(0, 3) ]; // 1st block
// [ [ 7, 4, 0 ], [ 5, 6, 2 ], [ 6, 10, 7 ] ]

tmp = [ image[0].slice(1, 4), image[1].slice(1, 4), image[2].slice(1, 4) ]; // 2nd block
// [ [ 4, 0, 1 ], [ 6, 2, 2 ], [ 10, 7, 8 ] ]

tmp = [ image[1].slice(0, 3), image[2].slice(0, 3), image[3].slice(0, 3) ]; // 3rd block
// [ [ 5, 6, 2 ], [ 6, 10, 7 ], [ 1, 4, 2 ] ]

tmp = [ image[1].slice(1, 4), image[2].slice(1, 4), image[3].slice(1, 4) ]; // 4th block
// [ [ 6, 2, 2 ], [ 10, 7, 8 ], [ 4, 2, 0 ] ]

console.log(tmp);

// tmp = [ (image.slice(1, 4) [0]).slice(1, 4), (image.slice(1, 4) [1]).slice(1, 4), (image.slice(1, 4) [2]).slice(1, 4) ];
// [ [ 6, 2, 2 ], [ 10, 7, 8 ], [ 4, 2, 0 ] ]

// tmp = [ (image.slice(0, 3) [0]).slice(0, 3), (image.slice(0, 3) [1]).slice(0, 3), (image.slice(0, 3) [2]).slice(0, 3) ];
// [ [ 7, 4, 0 ], [ 5, 6, 2 ], [ 6, 10, 7 ] ]

// tmp = [ (image.slice(0, 3) [1]).slice(0, 3), (image.slice(0, 3) [2]).slice(0, 3), (image.slice(0, 3) [3]).slice(0, 3) ]; // out of bounds on last slice

tmp = [ (image.slice(0, 3) [1]).slice(0, 3), (image.slice(0, 3) [2]).slice(0, 3) ]
// [ [ 5, 6, 2 ], [ 6, 10, 7 ] ]

// tmp = (image.slice(0, 3) [3]).slice(0, 3); // out of bounds

tmp = image.slice(0, 3) [2]; [ 6, 10, 7, 8 ]

// tmp = image.slice(0, 3) [3]; // undefined

tmp = image [3]; // [ 1, 4, 2, 0 ]

tmp = image [3].slice(0, 3); // [ 1, 4, 2 ]

console.log((image.slice(0, 3) [0]).slice(0, 3));


// console.log(image[0]);
// const uint8 = new Uint8Array([10, 20, 30, 40, 50]);

// uint8.subArray(1); 

*/