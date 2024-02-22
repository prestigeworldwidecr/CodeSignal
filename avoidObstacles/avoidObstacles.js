/*

You are given an array of integers representing coordinates of obstacles situated on a straight line.

Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.

Find the minimal length of the jump enough to avoid all the obstacles.

Example

For inputArray = [5, 3, 6, 7, 9], the output should be
solution(inputArray) = 4.

Check out the image below for better understanding:



Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] array.integer inputArray

Non-empty array of positive integers.

Guaranteed constraints:
2 ≤ inputArray.length ≤ 1000,
1 ≤ inputArray[i] ≤ 1000.

[output] integer

The desired length.

*/

function maxDifference(inputArray)
{
    let maxDifference = -1;

    for (let i = 0; i < inputArray.length - 1; i++)
    {
        let tmp = inputArray[i + 1] - inputArray[i];

        if (tmp > maxDifference)
        {
            maxDifference = tmp;
        }

        else
        {
            //
        }
    }

    return maxDifference;
}


function safePosition(inputArray)
{
    // can jump one
    // goto second occupied, back one until not occupied
        // worry about inputArray.length == 2 later, that's fucking easy
    let safePosition = inputArray[1] - 1;

    for (let i = safePosition; i >= 0; i--)
    {
        if (i == 0)
        {
            safePosition = NaN;     // no-go
        }

        else if (safePosition != inputArray[0])
        {
            safePosition = i;
            i = -1;
        }

        else if (safePosition == inputArray[0])
        {
            safePosition = i - 1;
            i = -1;
        }
        
        else
        {
            i--;
        }
    }

    return safePosition;

}

function remapCourse(inputArray)
{
    var course = "";
    var line = new Array(inputArray[inputArray.length - 1] + 1);   // make the course as biggest element
                                                        // used + 1 for extra visual space

    for (let i = 0; i < inputArray.length; i++)
    {
        line[inputArray[i]] = "X";
    }

    for (let i = 0; i < line.length; i++)
    {
        if (line[i] == "X")
        {
            //
        }

        else
        {
            line[i] = "O";
        }
    }

    course = line.toString();
    course = course.replaceAll(",", "\t");

    return course;
}

function lineGuide(line)
{
    let cnt = 0;
    var guide = new Array(line.length);

    // console.log("! ", line);
    
    for (let i = 0; i < line.length; i++)
    {
        if (line[i] == "X" || line[i] == "O" )
        {
            // console.log(".", line[i],".");
            guide[i] = cnt;
            // console.log(".", guide[i],".");
            cnt++;
        }

        else
        {
            // console.log(line[i]);
            // guide[i] = "-";
        }
    }

    guide = guide.toString();
    guide = guide.replaceAll(",,", "\t");
    // console.log(guide.toString());
    return guide;
    
}

function scramble(inputArray)
{
    inputArray = inputArray.sort();

    console.log(inputArray);

    // when biggest gap dont work, stuff a NaN in the array
}


function solution(inputArray) 
{

}

inputArray = [5, 3, 6, 7, 9]    // solution(inputArray) = 4

let course = remapCourse(inputArray.sort());
let guide = lineGuide(course);
console.log(safePosition(inputArray));

/*

********
BONEYARD
********

// console.log(inputArray);
// console.log(course);
// console.log(guide);
// console.log("i: ", i, " inputArray[i]: ", inputArray[i]);
    // return (line.toString()).replace(",", "   ");
    // console.log(line [0]);
        // console.log(line[i]);
// console.log(line.length);

// scramble (inputArray);

// console.log(maxDifference(inputArray));
// console.log(util.inspect(socialWindow.tabOpen().join(videoWindow.tabClose(2)), {compact: true}));
// console.log(lineGuide(remapCourse(inputArray.sort())));

let guide = new Array(course.length);
    
    for (let i = 0; i < inputArray.length; i++)
    {
        // console.log("i: ", i, " inputArray[i]: ", inputArray[i]);

        guide[inputArray[i]] = i;
    }

    for (let i = 0; i < guide.length; i++)
    {
        if (guide[i] != "")
        {
            
        }

        else
        {
            // guide[i] = "O";
        }
    }

    for(let i = 0; i < inputArray.length; i++)
    {
        // console.log(course[i]);
        if (course[i] != " ")
        {
            guide[i] = i;
        }

        else
        {
            guide[i] = "-";
        }

    }

    guide = guide.toString();
    guide = guide.replaceAll(",", "----");

    return guide;

biggest jump, if no, next biggest, so forth
max difference

jump jump jump if u hit a number, use regex and search, if hit, next max difference

*/