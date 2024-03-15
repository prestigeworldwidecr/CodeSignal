/*

Caring for a plant can be hard work, but since you tend to it regularly, you have a plant that grows consistently. Each day, its height increases by a fixed amount represented by the integer upSpeed. But due to lack of sunlight, the plant decreases in height every night, by an amount represented by downSpeed.

Since you grew the plant from a seed, it started at height 0 initially. Given an integer desiredHeight, your task is to find how many days it'll take for the plant to reach this height.

Example

For upSpeed = 100, downSpeed = 10, and desiredHeight = 910, the output should be
solution(upSpeed, downSpeed, desiredHeight) = 10.

#	Day	Night
1	100	90
2	190	180
3	280	270
4	370	360
5	460	450
6	550	540
7	640	630
8	730	720
9	820	810
10	910	900
The plant first reaches a height of 910 on day 10.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer upSpeed

A positive integer representing the daily growth of the plant.

Guaranteed constraints:
3 ≤ upSpeed ≤ 100.

[input] integer downSpeed

A positive integer representing the nightly decline of the plant.

Guaranteed constraints:
2 ≤ downSpeed < upSpeed.

[input] integer desiredHeight

A positive integer representing the goal height.

Guaranteed constraints:
4 ≤ desiredHeight ≤ 1000.

[output] integer

The number of days that it will take for the plant to reach / pass desiredHeight.

*/

/*

    produce
    -------
    #	Day	Night
1	100	90
2	190	180
3	280	270
4	370	360
5	460	450
6	550	540
7	640	630
8	730	720
9	820	810
10	910	900

*/
function trackProgress(upSpeed, downSpeed, desiredHeight)
{
    var progress = new Array();

    console.log("  # ", "Day ", "Night");

    for (var i = 0; i < 10; i++)
    {

        progress[i] = new Array();
        
        for (var j = 0; j < 3; j++)
        {
            
            if (j == 0)
            {
                progress[i][j] = i;
            }

            else if (j == 1)
            {
                if (i <= 1)
                {
                    progress[i][j] = upSpeed;
                }

                
                else if (i > 1)
                {
                    progress [i] [j] = progress [i - 1] [j] - progress [i - 1] [j + 1] + upSpeed;                   
                }
                

                else
                {
                    progress[i][j] = upSpeed;
                }

            }

            else if (j == 2)
            {
                if (i <= 1)
                {
                    progress[i][j] = downSpeed;
                }

                else
                {
                    progress [i] [j] = progress [i] [j - 1] - downSpeed;
                    progress[i][j] = downSpeed;
                }
            }

            else
            {
                //
            }

        }
    }

    for (var i = 0; i < progress.length; i++)
    {
        console.log(progress[i]);
    }

}

function solution(upSpeed, downSpeed, desiredHeight) 
{

}

var upSpeed = 100;
var downSpeed = 10;
var desiredHeight = 910;    // the output should be solution(upSpeed, downSpeed, desiredHeight) = 10.

trackProgress(upSpeed, downSpeed, desiredHeight);

/*

********
BONEYARD
********

// console.log("progress [i - 1] [j]: ", progress [i - 1] [j], " progress [i - 1] [j + 1]: ", progress [i - 1] [j + 1]);
                    // console.log("i: ", i, " j: ", j);
                    // console.log(progress [i - 1] [j]);
                    // console.log(progress [i - 1] [j + 1]);
                    // console.log("i: ", i, " j: ", j);

// console.log("row: ", progress.length, " column: ", progress[0].length);

else if (j == 1)
            {
                progress [i] [j] = upSpeedStep;
                // upSpeedStep = upSpeedStep + upSpeed;
            }

            else if (j == 2)
            {
                progress [i] [j] = downSpeedStep;
                // downSpeedStep = downSpeedStep + downSpeed;
            }

// console.log("i: ", i, " j: ", j, " ", progress[i][j], "\t");

if (i == 0)
            {
                progress [0] [0] = "#";
                // progress [0] [1] = "upspeed";
                // progress [0] [2] = "downspeed";
                progress [0] [1] = "Day";
                progress [0] [2] = "Night";
            }

    // console.log(progress [3][2]);

*/
