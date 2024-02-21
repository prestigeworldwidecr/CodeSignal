/*

An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
solution(inputString) = true;

For inputString = "172.316.254.1", the output should be
solution(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
solution(inputString) = false.

There is no first number.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string inputString

A string consisting of digits, full stops and lowercase English letters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 30.

[output] boolean

true if inputString satisfies the IPv4 address naming rules, false otherwise.

*/

function allDigits(inputString)
{
    var i = 0;
    var tmp = [];
    var tmp1 = "";
    var result = false;

    for (i; i < inputString.length; i++)
    {
        tmp = [];
        tmp.push(inputString [i]);
        tmp = tmp.toString();
        tmp1 = tmp.match(/[0-9]/g);

        if (tmp1 == null || isNaN(tmp1) || tmp1 == undefined || tmp1 == "")
        {
            return false;
        }

        else
        {
            result = true;
        }

        i++;
    }

    return result;

}

function solution(inputString) 
{
    var i = 0;
    var j = 0;
    var ip = inputString.split('.');
    var tmp = "";
    var tmp1 = "";
    var result = false;

    if (ip.length == 4)
    {
        for (i; i < ip.length; i++)
        {
            tmp = ip [i];             
            tmp1 = [...tmp];
            tmp1 = tmp.split('').reverse();
            
            console.log("^ ", "tmp1: ", tmp1, " tmp1 [0]: ", tmp1 [0] , " tmp1.length: ", tmp1.length);

            if(allDigits(tmp1))
            {                    
                if ( (tmp1.length == 1) || 
                    (tmp1 [1] != 0 && tmp1.length == 2) ||  // 01, first number can't be 0, 2 digit entry
                    (tmp1 [2] != 0 && tmp1.length == 3) )  // 02, first number can't be 0, 3 digit entry
                {                    
                    for (j = 0; j < tmp.length; j++)
                    {
                        tmp1 = [];
                        tmp1.push(tmp [j]);
                        tmp1 = tmp1.toString();
                                
                        if (0 <= Number(tmp) && Number(tmp) < 256)
                        {
                            result = true;
                        }

                        else
                        {
                             return false;
                        }
                    }

                }

                else
                {
                    return false;
                }

            }

            else
            {
                return false;
            }

        }

    }

    else
    {
        return false;
    }

    return result;

}

/*

********
BONEYARD
********

console.log(solution(inputString));

// var inputString = "1";  //  false    ok
// var inputString = ".254.255.0";         // false    ok
// var inputString = "0.254.255.0";        // true      ok
// var inputString = "64.233.161.00";      // false     ok
// var inputString = "172.16.254.1";          // true   ok
// var inputString = "255.16.254.1";           // true  ok
// var inputString = "1.1.1.1a";   // false    ok
// var inputString = "0..1.0";     // false    ok
// var inputString = "01.233.161.131"; // false    ok
// var inputString = "1.256.1.1";  // false    ok

// console.log(allDigits(""));
// console.log("tmp1 & ", tmp1);
                        // console.log("Number(tmp): ", Number(tmp), " 0 <= Number(tmp): ", 0 <= Number(tmp), " Number(tmp) < 256: ", Number(tmp) < 256);

// var tmp2 = "";

    // console.log("ip.length: ", ip.length);
            
            // console.log("!");

// console.log("#: ", tmp, "$: ", tmp1 [0], " tmp1 [0] !== undefined: ", tmp1 [0] !== undefined);
            // tmp2 = tmp1 [0];
            // if (!Number(tmp1 [0]) == 0)

else
                {
                    return false;
                }

if (tmp.length == 1)
            {
                console.log("@");
                return allDigits(tmp);
            }

            else
            {   

        // console.log("inputString: ", inputString, " tmp: ", tmp, " tmp.match(/[0-9]/g): ", tmp.match(/[0-9]/g), Number(tmp.match(/[0-9]/g)));
        // console.log(inputString.length);
        // console.log(inputString[i]);

// 02/20/2024 15.11

// no non digits check
// 

console.log(solution(inputString));

                        // console.log("j: ", j, " %: ", tmp1);
                        // console.log("^ ", "tmp.match(/[0-9]/g: ", tmp1.match(/[0-9]/g));

console.log(tmp1 [0]);

                        // tmp = tmp [i].toString();
                        // tmp = tmp [i].join("");

// console.log("; ", tmp1, " tmp1 [0]", tmp1 [0]);
// return (0 <= Number(tmp) && Number(tmp) < 256)
// console.log("% ", ip.length, " ip: ", ip);

// console.log(tmp);

            // console.log("ip [i]: *", tmp, " *ip.length == 4: ", ip.length == 4, " !isNaN(Number(tmp)): ", !isNaN(tmp), " isInteger: ", Number.isInteger(tmp), " tmp < 256: ", (tmp < 256), " tmp >= 0: ", (tmp >= 0));
            
            // if (Number.isInteger(parseInt(tmp)) && ip.length == 4 && !isNaN(Number(tmp)) && Number.isInteger(Number(tmp)) && Number(tmp) < 256 && Number(tmp) >= 0 && (tmp.length > 1 && tmp [0] == 0))

            

// console.log(tmp.split('').reverse() [0]);

// console.log("00".length, "00"[0]);
// console.log(Number.isInteger(172));
// console.log(Number.isInteger(Number('172')));
// console.log(Number.isInteger('172'));

// let text = "Visit W3Schools";
// let n = text.search(/w3schools/i);

// text.match(/[1-4]/g);

// var test = "172";
// var testes = test.match(/[0-9]/g);
// console.log(testes, test.length, Number.isInteger(Number(test[0])), Number(testes.toString));
// console.log(test.split('').reverse() [0]);

inputString = "1.1.1.1a";  // false    ok
inputString = "1.156.254.1";    //  true    ok
inputString = ".156.254.1";     //  false   ok
inputString = "172.316.254.1";  //  false   ok
inputString = "172.16.254.1";  //  true     ok

console.log(solution(inputString));

// console.log(parseInt(172.text()));
// console.log(isNaN(Number('16px')));

// console.log(solution(inputString));
// console.log(Number.isInteger(172))

// if (!isNaN(parseInt($('#val').text())))

// console.log(Number.isInteger(ip [0]), ip [0] == '', ip [0] < 256, ip [0] >= 0);
    // if (!isNaN(parseInt($('#val').text())))

// inputString = "172.16.254.1";    // true     ok
// inputString = "172.316.254.1";  // false    ok
inputString = ".254.255.0";  // false    

console.log(solution(inputString));


            if (tmp != "")
            {
                if (Number.isInteger(tmp))
                {
                    if (tmp < 256 && tmp >= 0)
                    {
                        return true;
                    }

                    else
                    {
                        return false;
                    }
                }

                else
                {
                    return false;
                }
            }

            else
            {
                return false;
            }
        }

        else
        {
            return false;
        }

*/