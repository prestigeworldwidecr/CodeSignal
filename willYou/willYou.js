/*

Once Mary heard a famous song, and a line from it stuck in her head. That line was "Will you still love me when I'm no longer young and beautiful?". Mary believes that a person is loved if and only if he/she is both young and beautiful, but this is quite a depressing thought, so she wants to put her belief to the test.

Knowing whether a person is young, beautiful and loved, find out if they contradict Mary's belief.

A person contradicts Mary's belief if one of the following statements is true:

they are young and beautiful but not loved;
they are loved but not young or not beautiful.
Example

For young = true, beautiful = true, and loved = true, the output should be
solution(young, beautiful, loved) = false.

Young and beautiful people are loved according to Mary's belief.

For young = true, beautiful = false, and loved = true, the output should be
solution(young, beautiful, loved) = true.

Mary doesn't believe that not beautiful people can be loved.

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] boolean young

[input] boolean beautiful

[input] boolean loved

[output] boolean

true if the person contradicts Mary's belief, false otherwise.

*/

function booleantoBinary(b)
{
    if (b == 0)
    {
        return 0;
    }

    else
    {
        return 1;
    }
}

function willYou(young, beautiful, loved)
{
    let binary = "" + booleantoBinary(young) + booleantoBinary(beautiful) + booleantoBinary(loved);
    let digit = parseInt(binary, 2);

    switch (digit)
    {
        case 0:
            return false;
        case 1:
            return true;
        case 2:
            return false;   //
        case 3:
            return true;   //
        case 4:
            return false;
        case 5:
            return true;
        case 6:
            return true;
        case 7:
            return false;
    }

}

function solution(young, beautiful, loved) 
{
    return willYou(young, beautiful, loved);
}

let young = true;
let beautiful = true;
let loved = true;       // the output should be solution(young, beautiful, loved) = false.

young = true;
beautiful = false;
loved = true;       // the output should be solution(young, beautiful, loved) = true.

young = false;
beautiful = false;
loved = false;      // the output should be solution(young, beautiful, loved) = false.

young = false;
beautiful = false;
loved = true;      // the output should be solution(young, beautiful, loved) = true.

// solution(young, beautiful, loved);
willYou(young, beautiful, loved);

/*

********
BONEYARD
********

let cnt = 0;

    if (young)
    {
        cnt++;
    }

    else
    {
        // 
    }

    if (beautiful)
    {
        cnt++;
    }

    else
    {
        //
    }

    if (loved)
    {
        cnt++;
    }

    else
    {
        //
    }

    if (cnt == 1 || cnt == 2)
    {
        return true;
    }

    else
    {
        return false;
    }

// return !(young && beautiful && loved) || !(young == beautiful == loved);

let result = !(young && beautiful && loved);

    if (young == false && beautiful == false && loved == false)
    {
        result = false;
    }

    else
    {

    }

    return result;    

*/