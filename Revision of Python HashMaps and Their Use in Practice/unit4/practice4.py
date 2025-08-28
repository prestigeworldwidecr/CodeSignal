'''

Great job on the last task! Now, let's see if you can add a missing piece. Use your knowledge from the lesson to determine how to count and display the number of appearances for each specified word in a provided string. Focus on analyzing the string and updating the HashMap accordingly.

'''

# Initialize a HashMap to store the word counts
word_counts = {}

# List of words to count
words_to_count = ["apple", "banana", "cherry"]

# String in which to count words
string_to_search = "apple banana apple cherry apple banana"

# Split the string into individual words
words_in_string = string_to_search.split()

# TODO: Count the appearances of each word in the string
# and update word_counts accordingly
for word in words_in_string :
# {
    if (word in words_to_count) :
    # {
        word_counts[word] = word_counts.get(word, 0) + 1
    # }

    else :
    # {
        None
    # }

# }

# Output the counts of each word
print(word_counts)

'''

'''