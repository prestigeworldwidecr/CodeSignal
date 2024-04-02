/*

You are playing an RPG game. Currently your experience points (XP) total is equal to experience. To reach the next level your XP should be at least at threshold. If you kill the monster in front of you, you will gain more experience points in the amount of the reward.

Given values experience, threshold and reward, check if you reach the next level after killing the monster.

Example

For experience = 10, threshold = 15, and reward = 5, the output should be
solution(experience, threshold, reward) = true;
For experience = 10, threshold = 15, and reward = 4, the output should be
solution(experience, threshold, reward) = false.
Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] integer experience

Guaranteed constraints:
3 ≤ experience ≤ 250.

[input] integer threshold

Guaranteed constraints:
5 ≤ threshold ≤ 300.

[input] integer reward

Guaranteed constraints:
2 ≤ reward ≤ 65.

[output] boolean

true if you reach the next level, false otherwise.

*/

function solution(experience, threshold, reward) 
{
    console.log(experience + reward >= threshold);
    
    return experience + reward >= threshold;
}

let experience = 10;
let threshold = 15;
let reward = 5;     //the output should be solution(experience, threshold, reward) = true;
// experience = 10;
// threshold = 15;
// reward = 4;     // the output should be solution(experience, threshold, reward) = false.

solution(experience, threshold, reward);

/*

********
BONEYARD
********

*/