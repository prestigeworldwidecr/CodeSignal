'''

In the legendary kingdom of Alphaland, exists a cryptic scroll named s, inscribed with a string of elegant lowercase letters. As a renowned linguist, your quest is to decipher this scroll by partitioning it into as many chapters (substrings) as your wit allows, under the condition that each letter graces only a maximum of one chapter.

This is a sacred task, for the chapters must follow the progression of the original text, reflecting the flow of the narrative embedded within it. To illustrate, if you were to partition the text "abacdcd" into the chapters "aba" and "cdcd", your resultant report of chapter lengths should list as [3, 4], preserving the original sequence.

The ancient scroll s stretches on to a length n, varying anywhere from 1 to 1000000 characters. Its diverse inhabitants range from the scribed characters from a to z.

Your mission, dear linguist, is to draw the linguistics of Alphaland in the form of the Python Function string_partition(string). This magical function shall read the string of characters and spin out a list of integers representing the lengths of each chapter, forming the crucial code to decipher the legend of Alphaland.

def string_partition(string):
    pass
    
Your chosen quest comes with the challenge of abstract thinking and careful crafting, as your function must perfectly divide the string, ensuring a unique occurrence of each character per chapter, while efficiently reporting the length of these tales.

Constraints:

The length of the input string n will be in the range of 1 ≤ n ≤ 1000000.
All characters in the string will be lower-case English alphabets ('a' to 'z').
The time complexity of the solution should be 
O
(
n
)
O(n).

Great! Here’s a small hint to nudge you forward:

Try to think about:

For each character, where is its last occurrence in the string?
As you scan the string, how can you use this info to decide when a chapter (partition) should end?
What data structure could help you quickly look up the last position of each character?


c
4:50 AM
hashmap
Cosmo
4:50 AM
Read message aloud
Nice! Yes, a HashMap (in Python, a dict) is perfect for this.

Try this:

First, create a dictionary that maps each character to its last index in the string.
Then, as you loop through the string, keep track of the farthest last index you've seen so far.
When your current index matches this farthest index, you know you can end a chapter there!
Can you try implementing just the part that builds the dictionary of last indices?


c
4:51 AM
i created two: 
last_occurrence = {}
max_block_sizes = {}
Cosmo
4:51 AM
Read message aloud
Great start! You only need the last_occurrence dictionary for this string partition problem.

Here’s a guiding question:

Once you have last_occurrence, how can you use it to decide where to split the string as you loop through it?
Try to:

Build last_occurrence so you know the last index of each character.
As you loop through the string, keep track of the farthest last index seen so far.
When your current index matches that farthest index, you can make a partition!
Can you try implementing just steps 1 and 2?


c
4:51 AM
i did that already
Cosmo
4:51 AM
Read message aloud
You did create a last_occurrence dictionary, but your current code is actually using logic from the previous array problem, not the string partition problem. That’s why you’re getting a KeyError and not the expected output.

Here’s a nudge:

For this problem, you don’t need max_block_sizes or to calculate block sizes between repeated elements.
Instead, after building last_occurrence, loop through the string and keep track of the farthest last index for any character you’ve seen so far.
When your current index matches that farthest index, that’s the end of a chapter—record its length and start a new one.
Can you try writing just the loop that finds these chapter ends, using your last_occurrence dictionary?

'''

def min_block(s) :
# {    
    start = 0
    end = 0
    chapter_length = 0
    last_occurrence = {}
    result = []

    for i, c in enumerate(s) :
    # {
        last_occurrence[c] = i
    # }
    
    for i, c in enumerate(s) :
    # {
        end = max(end, last_occurrence[c])
        
        if (i == end) :
        # {
            chapter_length = i - start + 1
            result.append(chapter_length)
            start = i + 1
        # }
        
        else :
        # {
            None
        # }
        
    # } 
     
    return result

# }

def string_partition(s) :
# {
    # TODO: implement the function
    result = min_block(s)

    return result

# }

s = "aaabbbccc" # [3, 3, 3]
s = "zabacbcz" # [8]
# s = "abcabcabc"
s = "abacdcd"

# "abacdcd" into the chapters "aba" and "cdcd", your resultant report of chapter lengths should list as [3, 4]

print(string_partition(s))

'''

***** BONEYARD *****

# last_occurrence[num] = i

# print(chapter_length)

if (num in last_occurrence) :
# {
    None
# }

else :
# {
    block_size = i - last_occurrence[num] - 1
# }


# max_block_sizes[num] = max(max_block_sizes[num], block_size)
# max_block_sizes = {}
# print(last_occurrence, max_block_sizes)

for num, pos in last_occurrence.items() :
# {
    block_size = len(arr) - pos - 1
    max_block_sizes[num] = max(max_block_sizes[num], block_size)
# }

min_num = min(max_block_sizes, key=max_block_sizes.get)

# print(min_num)

return min_num

def minimal_max_block(arr):
    last_occurrence = {}
    max_block_sizes = {}

    for i, num in enumerate(arr):
        if num not in last_occurrence:
            max_block_sizes[num] = i
        else:
            block_size = i - last_occurrence[num] - 1
            max_block_sizes[num] = max(max_block_sizes[num], block_size)
        last_occurrence[num] = i

    for num, pos in last_occurrence.items():
        block_size = len(arr) - pos - 1
        max_block_sizes[num] = max(max_block_sizes[num], block_size)

    min_num = min(max_block_sizes, key=max_block_sizes.get)

    return min_num

-----

def minimal_max_block(arr):
    last_occurrence = {}
    max_block_sizes = {}

for i, num in enumerate(arr):
    if num not in last_occurrence:
        max_block_sizes[num] = i
    else:
        block_size = i - last_occurrence[num] - 1
        max_block_sizes[num] = max(max_block_sizes[num], block_size)
    last_occurrence[num] = i    

    min_num = min(max_block_sizes, key=max_block_sizes.get)

return min_num



'''