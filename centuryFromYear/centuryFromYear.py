"""

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

"""

def solution(year) :
    
    tmp = str(year)

    if (year < 100) :
        return 1
    
    elif (year < 1000) :
        if (tmp[1] == '0' and tmp[2] == '0') :
            return int(tmp[0])
        else :
            return int(tmp[0]) + 1
    
    else :
        if (tmp[2] == '0' and tmp[3] == '0') :
            return int(tmp[0] + tmp[1])
        else :
            return int(tmp[0] + tmp[1]) + 1

print(solution(2120))


"""

########
BONEYARD
########

# return len(str(year))

"""