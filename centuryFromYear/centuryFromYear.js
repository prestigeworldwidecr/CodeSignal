// centuryFromYear.js

/*

Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example

For year = 1905, the output should be
solution(year) = 20;
For year = 1700, the output should be
solution(year) = 17.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer year

A positive integer, designating the year.

Guaranteed constraints:
1 ≤ year ≤ 2005.

[output] integer

The number of the century the year is in.

[JavaScript] Syntax Tips

// Prints help message to the console
// Returns a string
function helloWorld(name) {
    console.log("This prints to the console when you Run Tests");
    return "Hello, " + name;
}

*/

function solution(year)
{
    tmp = year.toString();

    if (year < 100)
    {
        return 1;
    }

    else if (year < 1000)
    {
        if (tmp[2] == '0')
        {
            return parseInt(tmp [0]);
        }
        
        
        else
        {
            return parseInt(tmp [0]) + 1;
        }
    }

    else
    {
        if (tmp [3] == '0')
        {
            return parseInt(tmp [0] + tmp [1]);
        }

        else
        {
            return parseInt(tmp [0] + tmp [1]) + 1;
        }
    }

}

console.log("1905: ", solution(1905)); // 20
console.log("1700: ", solution(1700)); // 18
console.log("1988: ", solution(1988)); // 20
console.log("2000: ", solution(2000)); // 20
console.log("2001: ", solution(2001)); // 21
console.log("200: ", solution(200)); // 3
console.log("45: ", solution(45)); // 0
console.log("8: ", solution(8)); // 0
