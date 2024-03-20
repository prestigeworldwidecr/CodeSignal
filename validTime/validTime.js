/*

Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
solution(time) = true;
For time = "25:51", the output should be
solution(time) = false;
For time = "02:76", the output should be
solution(time) = false.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string time

A string representing time in HH:MM format. It is guaranteed that the first two characters, as well as the last two characters, are digits.

[output] boolean

true if the given representation is correct, false otherwise.

*/

function validTime(s)
{
    // console.log(s);

    var hour = Number(s.charAt(0) + s.charAt(1));
    var minute = Number(s.charAt(3) + s.charAt(4));
    var result = false;

    console.log("hour: ", hour, " minute: ", minute);

    result = 0 <= hour && hour < 24 && 0 <= minute && minute <= 60;

    // console.log(result);
    return result;

}

function solution(time) 
{

}

// var time = "13:58"; // the output should be solution(time) = true;
// time = "25:51"; // the output should be solution(time) = false;
time = "02:76"; // the output should be solution(time) = false.

validTime(time);

/*

********
BONEYARD
********

function checkHour(s)
{

}

function checkMinute(m)
{

}

*/