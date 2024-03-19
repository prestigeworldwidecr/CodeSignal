/*

A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

Example

For inputString = "00-1B-63-84-45-E6", the output should be
solution(inputString) = true;
For inputString = "Z1-1B-63-84-45-E6", the output should be
solution(inputString) = false;
For inputString = "not a MAC-48 address", the output should be
solution(inputString) = false.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string inputString

Guaranteed constraints:
15 ≤ inputString.length ≤ 20.

[output] boolean

true if inputString corresponds to MAC-48 address naming rules, false otherwise

*/

// check MAC Address: A1--93 ... "-": 45
function isDoubleDashComplaint(s)
{
    var result = false;

    for (var i = 0; i < s.length; i++)
    {
        var cur = s.charCodeAt(i);

        if (cur == 45)
        {
            var next = s.charCodeAt(i + 1);
            
            // console.log("cur: ", cur, " next: ", next);
            
            if (next == 45)
            {
                return false;
            }

            else
            {
                result = true;
            }

        }

        else
        {
            result = true;
        }

    }

    return result;

}

function dashCount(s)
{
    var cnt = 0;

    for(var i = 0; i < s.length; i++)
    {
        var cur = s.charCodeAt(i);

        if (cur == 45)
        {
            cnt++;
        }

        else
        {
            //
        }
    }
    
    return cnt;
}

// return false if does not meed ASCII/MAC requirements:
// CAPS A-F: 65-70 , 0-9: 48-57
function isASCIICompliant(s)
{
    var result = false;
    var tmp = s.replaceAll("-", "");

    // console.log(tmp);

    for (var i = 0; i < tmp.length; i++)
    {
        var cur = tmp.charCodeAt(i)

        // console.log("cur: ", cur, " : ", tmp.charAt(i));

        if (65 <= cur && cur <= 70|| 48 <= cur && cur <= 57)
        {
            result = true;
        }

        else
        {
            return false;
        }

    }

    return result;

}

function isMAC48Address(s)
{
    var result = false;

    if (dashCount(s) == 5 && isASCIICompliant(s) && isDoubleDashComplaint(s))
    {
        result = true;
    }

    else
    {
        result = false;
    }

    return result;

}

function solution(inputString) 
{
    return isMAC48Address(inputString);
}

// var inputString = "00-1B-63-84-45-E6"   // the output should be solution(inputString) = true;
// inputString = "Z1-1B-63-84-45-E6"   // the output should be solution(inputString) = false;
// inputString = "not a MAC-48 address"    // the output should be solution(inputString) = false.
// inputString = "---";

// console.log(isASCIICompliant(inputString));
// console.log(isDoubleDashComplaint(inputString));
// console.log(dashCount(inputString));

console.log(isMAC48Address(inputString));

/*

********
BONEYARD
********

// var prev = s.charAt(0);
    // var cur = prev;
    var cnt = 0;
    

            if (cnt > 1)
            {
                return false;
            }

            else
            {
                result = true;
            }

// tmp = tmp.split("");
        // console.log(tmp.charCodeAt(1));
        // console.log(tmp.length, " tmp[i]: ", tmp[i]);

*/