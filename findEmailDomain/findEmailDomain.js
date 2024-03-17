/*

An email address such as "John.Smith@example.com" is made up of a local part ("John.Smith"), an "@" symbol, then a domain part ("example.com").

The domain name part of an email address may only consist of letters, digits, hyphens and dots. The local part, however, also allows a lot of different special characters. Here you can look at several examples of correct and incorrect email addresses.

Given a valid email address, find its domain part.

Example

For address = "prettyandsimple@example.com", the output should be
solution(address) = "example.com";
For address = "fully-qualified-domain@codesignal.com", the output should be
solution(address) = "codesignal.com".
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string address

Guaranteed constraints:
10 ≤ address.length ≤ 50.

[output] string

*/

function findEmailDomain(s)
{
    var tmp = s.split("@");

    result = tmp[tmp.length - 1];
    result = result.replace(/"/g, "");

    if ( (65 > result.charCodeAt(0) && result.charCodeAt(0) > 90) ||  // A-Z
         (97 > result.charCodeAt(0) && result.charCodeAt(0) > 122) )  // a-z
    {
        result = result.substring(1, result.length);
    }

    else
    {
        // 
    }
    
    return result;
}

function solution(address) 
{
    return findEmailDomain(address);
}

// var address = "prettyandsimple@example.com"     // the output should be solution(address) = "example.com";
// var address = "fully-qualified-domain@codesignal.com"   // the output should be solution(address) = "codesignal.com".
var address = "\"very.unusual.@.unusual.com\"@usual.com"    // "usual.com"

console.log(findEmailDomain(address));

/*

********
BONEYARD
********

function breakStringAt(s)
{
    tmp = s.split("@");

    console.log(tmp.length, " a ver: ", tmp[tmp.length -1]);
}

// breakStringAt(address);
// console.log("tmp.length: ", tmp.length, " tmp[0]: ", tmp[0], " tmp[1]: ", tmp[1], " tmp[tmp.length - 1]: ", tmp[tmp.length - 1]);
// console.log(s);

// var result = [tmp.length - 2].toString();

    // console.log("tmp: ", tmp, " result: ", result);
    // console.log("tmp: ", tmp, " result: ", result);
    // result = result.replace(/"/g, "");
    // console.log(result);
        // console.log("!");
    // console.log(s.split("@")[1]);
    // console.log("tmp: ", tmp, " result: ", result);

*/