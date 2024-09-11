"""

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

""" 

def solution(time) :
# {
    time = time.split(':')
    hour = int(time[0])
    minute = int(time[1])

    print (hour, minute)

    return (0 <= hour < 24 and 0 <= minute < 60)
# }


# For time = "13:58", the output should be solution(time) = true;
# For time = "25:51", the output should be solution(time) = false;
# For time = "02:76", the output should be solution(time) = false.
time = "13:58"
# time = "25:51"
# time = "02:76"

print(solution(time))

"""

********
BONEYARD
********

"""