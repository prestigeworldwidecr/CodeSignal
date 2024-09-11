"""

Define a word as a sequence of consecutive English letters. Find the longest word from the given string.

Example

For text = "Ready, steady, go!", the output should be
solution(text) = "steady".

Input/Output

[execution time limit] 4 seconds (js)

[memory limit] 1 GB

[input] string text

Guaranteed constraints:
4 ≤ text.length ≤ 50.

[output] string

The longest word from text. It's guaranteed that there is a unique output.

"""

import string
import sys

def solution(text) :
# {
    text = text.replace(' ', '*')
    tmp = list(text)
    max = -sys.maxsize
    result = ""
    
    for i in range(len(text)) :
    # {
        if (tmp[i] in string.punctuation) :
        # {
            tmp[i] = '*'
        # }

        else :
        # {
            None
        # }

    # }

    tmp = tuple(tmp)
    tmp = ''.join(tmp)
    tmp = str(tmp).split('*')
    
    for i in range(len(tmp)) :
    # {
        if (len(tmp[i]) > max) :
        # {
            max = len(tmp[i])
            result = tmp[i]
        # }

        else :
        # {
            None
        # }

    # }
    
    return result
# }

text = "Ready, steady, go!"    # the output should be solution(text) = "steady".
# text = "To be or not to be"

print(solution(text))

"""

********
BONEYARD
********

# print(tmp[i], len(tmp[i]))
        # None

# print(tmp)
    # print('@', tmp)
    # print('!', tmp)
    # print('#', tmp)
    # print('!', i)

def solution(t):
    return max("".join([i if i in string.ascii_letters else " " for i in t]).split(),key=len)

# import string library function  
import string  
    
# An input string. 
Sentence = "Hey, Geeks !, How are you?"
  
for i in Sentence: 
      
    # checking whether the char is punctuation. 
    if i in string.punctuation: 
          
        # Printing the punctuation values  
        print("Punctuation: " + i) 

# tmp = list(text)
    # tmp = tmp.split('[^a-zA-Z]', text)

punc = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "[", "]", "{", "}", ".", "<", ">", "?", "`", "~"]
    # max = -sys.maxsize
    result = ""
    
    for ele in text :
    # {
        if (ele in punc) :
        # {
            text = text.replace(ele, "")
        # }

        else :
        # {
            None
        # }

    # }

    text = text.replace(" ", ',')
    tmp = text.split(",")

    print(tmp)

    for i in range(len(tmp)) :
    # {
        
        if (len(tmp[i]) > len(result)) :
        # {
            result = tmp[i]
        # }

        else :
        # {
            None
        # }

    # }

    return result

tmp = tuple(text.split(","))
    # print(text, tmp, len(tmp))

# print(text)
    # print(max(tmp))

    # max = -sys.maxsize
    # tmp = []

# text.replace(punc[i], "")

test_str = 'Gfg, is best: for ! Geeks ;'
    test_str = test_str.translate
    (str.maketrans('', '', string.punctuation))
    print(test_str)
    
    # text = text.translate
    # print((str.maketrans('', '', string.punctuation)))
    # print(text)

test_str = 'Gfg, is best: for ! Geeks ;'
 
    test_str = test_str.translate
    (str.maketrans('', '', string.punctuation))
    print(test_str)

   
    tmp = string(text)
    tmp = tmp.translate(None, tmp.punctuation)
    tmp = tmp.split(", ")
    tmp = str(tmp)

punc = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "[", "]", "{", "}", ".", "<", ">", "?", "`", "~"]
# tmp = str(tmp).replace(punc, "")

    for i in range(len(punc)) :
    # {
        # print(i, punc[i])
        tmp.replace(punc[i], "")
    # }

"""