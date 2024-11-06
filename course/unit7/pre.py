'''

Solution for Problem 1
Let's break down the solution step-by-step:

First, let's set up an empty dictionary count_dict:

Python
Copy
Play
count_dict = {}
This dictionary will help us keep track of the count or occurrences of each element in our list.

We iterate through the elements of listA. For each element, we increment its count in count_dict. If the count exceeds n / 2, we return that element:

Python
Copy
Play
for element in listA:
    count_dict[element] = count_dict.get(element, 0) + 1
    if count_dict[element] > len(listA) // 2:
        return element
Here, the method dict.get(key, default) returns the value for a key if it exists in the dictionary. If not, it returns the default value.

If no majority element is found after the full iteration, we return -1:

Python
Copy
Play
return -1
Such a default value is a common approach in problems where the answer may not exist.

The final solution looks like this:
Python
Copy
Play
def solution(listA):
    count_dict = {}
    for element in listA:
        count_dict[element] = count_dict.get(element, 0) + 1
        if count_dict[element] > len(listA) // 2:
            return element
    return -1
On a separate note, do you think we can apply defaultdict here? How will the code change in that case?

Congratulations! You have successfully optimized the solution to the majority vote problem using Python dictionaries.


Let's work through the solution. We first initialize an empty dictionary index. Then, we start looping through our list of documents. For each document we split each document into words, and for each word, we check if it is already in our dictionary index. If it's in the dictionary, we append the current document's index to the list of indices for that word. If the word is not in the dictionary, then it's the first time we've seen this word, and we add it to the index with a list that contains the current document's index as the value. Here's how to do it:

As evident from the function, the keyword_index function runs in 
O
(
N
)
O(N) time, achieving the task efficiently with the help of dictionaries.

'''

def solution(listA) :
# {
    count_dict = {}

    for element in listA :
    # {  
        count_dict[element] = count_dict.get(element, 0) + 1
        
        if count_dict[element] > len(listA) // 2 :
        # {
            return element
        # }

        else :
        # {
            None
        # }

    # }
       
    return -1

# }

def keyword_index(docs) :
# {
    index = {}

    for doc_idx, doc in enumerate(docs) :
    # {
        for word in doc.split() :
        # {
            if word in index :
            # {
                index[word].append(doc_idx)
            # }
            
            else :
            # {
                index[word] = [doc_idx]
            # }

        # }

    # }

    return index

# }

'''

********
BONEYARD
********

'''