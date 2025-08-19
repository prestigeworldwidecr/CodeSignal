'''

Great job on learning how to count letter frequencies in sentences! Now, let's put your knowledge into practice. You have a sentence about a library, and your task is to write the missing piece of code to count how many times each letter appears. Remember, only consider alphabetical characters (consider using the method letter.isalpha()), and think about updating counts or adding new letters to your directory.

'''

# Function to count the frequency of each letter in a given sentence
def count_letter_frequency(sentence) :
# {
    letter_count = {}

    for letter in sentence :
    # {
        # TODO: If the character is a letter, update its count in the dictionary
        # or add it with a count of 1 if it's not already there
        if (letter.isalpha()) :
        # {
            letter_count[letter] = letter_count.get(letter, 0) + 1
        # }

        else :
        # {
            None
        # }

    # }

    return letter_count

# }

# Example usage with a predefined sentence
sentence = "Once upon a time in a faraway library"

# TODO: Call the function with the sentence variable and print the result
print(count_letter_frequency(sentence))

'''

***** BONEYARD *****

print(type(letter_count[letter]))
            
            if (letter_count[letter] is None) :
            # {
                letter_count[letter] = 0
            # }

            else :
            # {
                letter_count[letter] = letter_count[letter] + 1
            # }

'''