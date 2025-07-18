'''

In the third and final task of our KISS principle journey, we will focus on simplifying string manipulations. The current code is intended to check if a given string is a palindrome, but the logic is unnecessarily convoluted with redundant steps. Your task is to refactor the code to make it more straightforward and easy to understand while preserving its functionality. Specifically, consider the use of the cleaned variable which converts characters to uppercase. This step can be simplified using string built-in methods to normalize case efficiently. Additionally, think about how you can further simplify the palindrome check itself using string methods, thus streamlining the overall logic.

Let's make this palindrome checker as simple as possible!

Good effort simplifying the palindrome check! However, you need to make sure your function works for words with different cases, like "RaceCar". Can you update your code to handle that? Let me know if you want a hint!

'''

def is_palindrome(word) :
# {
    tmp = word.lower()
    
    if (tmp == tmp[ : : -1]) :
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
    word = "balls" # radar # racecar
    result = is_palindrome(word)
    print(word, "is a palindrome:", result)
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

cleaned = ''.join(char.upper() for char in word)
    length = len(cleaned)

    for i in range(length // 2) :
    # {
        if (cleaned[i] != cleaned[length - i - 1]) :
        # {
            return False
        # }

        else :
        # {
            None
        # }

    # }

    return True


'''