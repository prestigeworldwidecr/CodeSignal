//这个有点意思

// function 

function solution(arr) 
{
    for(var n = 1; ; n++) 
    {
        if (arr.every(x => x%n)) 
        {
            return n;
        }

        else
        {
            //
        }

    }
}

let inputArray = [5, 3, 6, 7, 9];

console.log(solution(inputArray));