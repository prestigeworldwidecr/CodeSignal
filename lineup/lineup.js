/*

To prepare his students for an upcoming game, the sports coach decides to try some new training drills. To begin with, he lines them up and starts with the following warm-up exercise: when the coach says 'L', he instructs the students to turn to the left. Alternatively, when he says 'R', they should turn to the right. Finally, when the coach says 'A', the students should turn around.

Unfortunately some students (not all of them, but at least one) can't tell left from right, meaning they always turn right when they hear 'L' and left when they hear 'R'. The coach wants to know how many times the students end up facing the same direction.

Given the list of commands the coach has given, count the number of such commands after which the students will be facing the same direction.

Example

For commands = "LLARL", the output should be
solution(commands) = 3.

Let's say that there are 4 students, and the second one can't tell left from right. In this case, only after the second, third and fifth commands will the students face the same direction.



Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string commands

String consisting of characters 'L', 'R' and 'A' only.

Guaranteed constraints:
0 ≤ commands.length ≤ 35.

[output] integer

The number of commands after which students face the same direction.

*/

// starting position    move    end
// front 1              
//                      L       2
//                      R       3
//                      A       4
// left 2
//                      L       4
//                      R       1
//                      A       3
// right 3
//                      L       1
//                      R       4
//                      A       2
// back 4
//                      L       3
//                      R       2
//                      A       1

function facingSame(a)
{
    let result = false;
    
    for (let i = 0; i < a.length - 1; i++)
    {
        if (a [i] == a [i + 1])
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

function endState(start, move, movelist)
{
    let end = "";
    
    for (let i = 0; i < movelist.length; i++)
    {
        if (start == movelist[i][0])
        {
            if (move == movelist[i][1])
            {
                return movelist[i][2];
            }

            else
            {

            }

        }

        else
        {
            //
        }

    }

}

function teamMove(commands, team, movelist)
{
    let s = "";

    for (let i = 0; i < commands.length; i++)
    {
        for (let j = 0; j < team.length; j++)
        {
            team[j] = endState(team[j], commands[i], movelist);
        }
    }

    console.log(team);

}

function solution(commands) 
{

}

let movelist = [[1, "L", 2],
                [1, "R", 3],
                [1, "A", 4],                
                [2, "L", 4],            
                [2, "R", 1],
                [2, "A", 3],
                [3, "L", 1],
                [3, "R", 4],                
                [3, "A", 2],            
                [4, "L", 3],
                [4, "R", 2],
                [4, "A", 1]];

let commands = "LLARL";     // the output should be solution(commands) = 3.
let team = [1, 1, 2, 1];

// console.log(facingSame(team));
teamMove(commands, team, movelist);

/*

********
BONEYARD
********

// console.log(team[i]);
        // lets do one move, easy... start 1, end 2
    // let teamMember1 = 1;
    // let move = "L";

    // endState(teamMember1, move, movelist);

    
// console.log(a [i], a [i + 1]);

                // console.log("!");
                // console.log("!");
                // console.log(movelist[i][2]);

*/