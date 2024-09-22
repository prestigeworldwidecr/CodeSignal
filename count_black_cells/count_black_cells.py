"""

Imagine a white rectangular grid of n rows and m columns divided into two parts by a diagonal line running from the upper left to the lower right corner. Now let's paint the grid in two colors according to the following rules:

A cell is painted black if it has at least one point in common with the diagonal;
Otherwise, a cell is painted white.
Count the number of cells painted black.

Example

For n = 3 and m = 4, the output should be
solution(n, m) = 6.

There are 6 cells that have at least one common point with the diagonal and therefore are painted black.



For n = 3 and m = 3, the output should be
solution(n, m) = 7.

7 cells have at least one common point with the diagonal and are painted black.



Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] integer n

The number of rows.

Guaranteed constraints:
1 ≤ n ≤ 105.

[input] integer m

The number of columns.

Guaranteed constraints:
1 ≤ m ≤ 105.

[output] integer

The number of black cells.

"""

def solution(n, m) :
# {
    max = 1

    for i in range(1, n + 1) :
    # {
        if (n % i == 0 and m % i == 0) :
        # {
            max = i
        # }

        else :
        # {
            None
        # }

    # }

    return n + m + max - 2

# }

# For n = 3 and m = 3, the output should be solution(n, m) = 7.
n = 3 
m = 3

print(solution(n, m))

"""

********
BONEYARD
********

author: cthaeghya
int solution(int n, int m) {
    int max = 1;
    for (int k = 1; k <= n; k++) {
        if (n%k == 0 && m%k == 0)
            max = k;
    }
    return n+m+max-2;
}


"""