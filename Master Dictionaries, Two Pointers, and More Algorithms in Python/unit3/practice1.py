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

Awesome! If you already have the loop like:

for i, c in enumerate(s):
    # your logic here

Now, inside that loop:

Update a variable (let’s call it end) to be the maximum of its current value and last_occurrence[c].
If i == end, that’s the end of a chapter—append the length to your result list and reset your start point.
What do you think you should use to keep track of where the current chapter started?


c
Nov 13
i have no clue
Cosmo
Nov 13
Read message aloud
No problem! You can use a variable, let’s call it start, to remember where the current chapter began.

Set start = 0 before the loop.
When you find a chapter end (i == end), the chapter length is i - start + 1.
After recording the length, set start = i + 1 to begin the next chapter.
Would you like to try adding this logic to your loop?


c
Nov 13
done
Cosmo
Nov 13
Read message aloud
Great job! 🚀

Now, test your function with a few examples (like "abacdcd" or "abcabcabc") to see if it returns the correct chapter lengths. If something doesn’t look right, let me know what output you get and we’ll debug together!


c
Nov 13
input: "abcabcabc"
output: {'a': 2, 'b': 5, 'c': 8}
Cosmo
Nov 13
Read message aloud
Nice, that means your last_occurrence dictionary is working!
Now, try running your full function to see what list of chapter lengths it returns for "abcabcabc". What output do you get?


c
Yesterday
{'a': 2, 'b': 5, 'c': 8}
Cosmo
Yesterday
Read message aloud
It looks like you’re printing the last_occurrence dictionary, not the list of chapter lengths.

Make sure your function:

Builds last_occurrence first,
Then runs the loop to find chapter ends and appends the lengths to a result list,
Finally, returns the result list (not the dictionary).
Can you check if you’re returning the correct result at the end? If not, try adding a return res where res is your list of chapter lengths.


c
Yesterday
[9]
Cosmo
Yesterday
Read message aloud
Perfect! 🎉

That’s the correct output for "abcabcabc"—the whole string is one chapter. Try a few more test cases (like "abacdcd" or "abc") to make sure your function works for different patterns. If you see any unexpected results, let me know!


c
Yesterday
"abacdcd" returns [7]
all its doing is returning the count of letters
this doesnt work
Cosmo
Yesterday
Read message aloud
Great observation! If your function returns [7] for "abacdcd", it means your partitioning logic isn’t splitting chapters at the right places.

Let’s debug together:

Are you updating end inside your loop to be the maximum of its current value and the last occurrence of the current character?
Are you checking if i == end: inside the loop, and only then appending the chapter length and updating start?
For "abacdcd", the correct output should be [3, 4].
Try printing end and i at each step to see if your logic is finding the right chapter ends.
What do you see when you do that?


c
Yesterday
Are you updating end inside your loop to be the maximum of its current value and the last occurrence of the current character?
i dont know how to do this
Cosmo
Yesterday
Read message aloud
No worries! Here’s how you can update end inside your loop:

end = max(end, last_occurrence[c])

end keeps track of the farthest last index of any character you’ve seen so far.
last_occurrence[c] gives you the last index of the current character.
So, in your loop, after getting c (the current character), update end like above.
This way, end always points to the farthest last occurrence among all characters in the current chapter.

Want to try adding that line inside your loop?


c
Yesterday
what is variable c?
Cosmo
Yesterday
Read message aloud
Great question! In the loop:


for i, c in enumerate(s):

i is the current index (0, 1, 2, ...)
c is the character at that index in the string s
So, for example, if s = "abacdcd", then on the first iteration, i = 0 and c = 'a'.

Does that help clarify?


c
Yesterday
still doesnt work
Cosmo
Yesterday
Read message aloud
Let’s double-check your steps! Here’s a checklist to help you debug:

Build the last occurrence dictionary:

last_occurrence = {c: i for i, c in enumerate(s)}

Initialize variables:

res = []
end = 0
start = 0

Loop through the string:

for i, c in enumerate(s):
    end = max(end, last_occurrence[c])
    if i == end:
        res.append(i - start + 1)
        start = i + 1

Return the result

return res

If you follow these steps exactly, "abacdcd" should return [3, 4].

If it still doesn’t work, can you share your current code (just the function)? I’ll help you spot what’s off!


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