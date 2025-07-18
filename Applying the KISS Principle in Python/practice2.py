'''

Welcome to the second task of the KISS principle lesson! In the previous task, we simplified the order cost calculation. Now, we'll shift our focus to improving the readability of the method's logic.

The current code evaluates whether a given year is a leap year, but it's a bit more complex than it needs to be. Your task is to refactor the code by simplifying the logic while maintaining its functionality. Apply the KISS principle to enhance the simplicity and clarity of the function is_leap_year.

A leap year is determined by the following rules:

A year is a leap year if it is evenly divisible by 4.
However, if the year is evenly divisible by 100, it is not a leap year, unless:
The year is also evenly divisible by 400, in which case it is a leap year.
For example:

The year 2000 is a leap year because it is evenly divisible by 400.
The year 1900 is not a leap year because it is evenly divisible by 100 but not by 400.
The year 2024 is a leap year because it is evenly divisible by 4 but not by 100.
Let's simplify this logic to make it easy to read and understand!

'''

def check_leap(year) :
# {
    # print("year % 400\t", "year % 4\t", "year % 100")
    # print(year % 400 == 0, "\t", year % 4 == 0, "\t", year % 100 == 0)
    
    if (year % 400 == 0) :
    # {
        return True
    # }

    elif (year % 4 == 0 and not(year % 100 == 0)) :
    # {
        return True
    # }

    else :
    # {
        return False
    # }

# }

def main() :
# {
    year = 2024
    leap = check_leap(year)
    print(year, "is a leap year:", leap)
# }

if (__name__ == "__main__") :
# {
    main()
# }

else :
# {
    None
# }

'''

***** BONEYARD *****


    if year % 4 == 0:

        if year % 100 == 0:

            if year % 400 == 0:

                return True
            
            else:

                return False
        else:

            return True
        
    return False

'''