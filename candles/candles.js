/*

When a candle finishes burning it leaves a leftover. makeNew leftovers can be combined to make a new candle, which, when burning down, will in turn leave another leftover.

You have candlesNumber candles in your possession. What's the total number of candles you can burn, assuming that you create new candles as soon as you have enough leftovers?

Example

For candlesNumber = 5 and makeNew = 2, the output should be
solution(candlesNumber, makeNew) = 9.

Here is what you can do to burn 9 candles:

burn 5 candles, obtain 5 leftovers;
create 2 more candles, using 4 leftovers (1 leftover remains);
burn 2 candles, end up with 3 leftovers;
create another candle using 2 leftovers (1 leftover remains);
burn the created candle, which gives another leftover (2 leftovers in total);
create a candle from the remaining leftovers;
burn the last candle.
Thus, you can burn 5 + 2 + 1 + 1 = 9 candles, which is the answer.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer candlesNumber

The number of candles you have in your possession.

Guaranteed constraints:
1 ≤ candlesNumber ≤ 15.

[input] integer makeNew

The number of leftovers that you can use up to create a new candle.

Guaranteed constraints:
2 ≤ makeNew ≤ 5.

[output] integer

*/

function makeCandles(makeNew, cnt, candlesNumber, leftovers)
{    
    // first candle
    if (cnt == 0 && candlesNumber == 1)
    {
        console.log("fc", makeNew, cnt, candlesNumber, leftovers);
        return 1;
    }
    
    // burn candle
    else if (candlesNumber > 1)
    {
        cnt = cnt + candlesNumber;
        leftovers = leftovers + candlesNumber;
        candlesNumber = 0;
        console.log("bc", makeNew, cnt, candlesNumber, leftovers);
        return makeCandles(makeNew, cnt, candlesNumber, leftovers);
    }

    // last candle
    else if (candlesNumber == 1 && leftovers <= 1) // (Math.floor(leftovers / makeNew) > 0) )  
    {
        cnt = cnt + candlesNumber;
        console.log("lc", makeNew, cnt, candlesNumber, leftovers);
        return cnt;
    }

    // create candle
    else if (leftovers > 1)
    {
        candlesNumber = Math.floor(leftovers / makeNew);     //
        leftovers = candlesNumber % makeNew;                // 
        console.log("cc", makeNew, cnt, candlesNumber, leftovers);
        return makeCandles(makeNew, cnt, candlesNumber, leftovers);
    }
    
    else
    {
        console.log("?c", makeNew, cnt, candlesNumber, leftovers);
        return cnt + 1;
    }
    
}

function solution(candlesNumber, makeNew) 
{
    return makeCandles(makeNew, 0, candlesNumber, 0);
}

let candlesNumber = 5;
let makeNew = 2;        // the output should be solution(candlesNumber, makeNew) = 9
// candlesNumber = 1;
// makeNew = 2;        // the output should be solution(candlesNumber, makeNew) = 1
// candlesNumber = 3;
// makeNew = 3;        // the output should be solution(candlesNumber, makeNew) = 4

console.log("candle: ", makeCandles(makeNew, 0, candlesNumber, 0));

/*

********
BONEYARD
********

// console.log(makeNew, cnt, candlesNumber, leftovers);

*/