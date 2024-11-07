'''

Hey there, I've got a stellar task for you where you gotta be like a cosmic librarian! You know, we got gazillion documents in the universe, each represented as a string in a list. Your task is to whip up an index that's as nifty as a dictionary which logs in every unique word from these documents. Now, don't forget, each unique word is a key, mapping to another dictionary where the key is the document index and the value is how many times that word appeared in the document. It's sure gonna make searching a lot quicker, kinda like quantum speed, eh? Let's get rollin'!

Ensure that your code handles all the edge cases. The input would be a list, where each string inside the list is a document. And every string is just a regular english text, easy peasy.

The output should be a dictionary, where each unique word is a key, and the mapped value should be another dictionary, having document index as the key and its corresponding word count as the value.

# key is word (string)
# value is dictionary | key is doc idx value word count

Alright, time to hit the hyper-speed!

'''

def keyword_index(docs) :
# {
    # implement this
    index = {}

    for doc_idx, doc in enumerate(docs) :
    # {
        for word in doc.split() :
        # {

            if word in index :
            # {

                if doc_idx in index[word] :
                # {
                    index[word][doc_idx] = index[word][doc_idx] + 1
                # }

                else :
                # {
                    index[word][doc_idx] = 1
                # }

            # }
            
            else :
            # {
                index[word] = {doc_idx: 1}
            # }

        # }

    # }

    return index

# }

docs = ["Hello world", "world of python", "python is a snake"]
print(keyword_index(docs))  
# Expected output: {'Hello': {0: 1}, 'world': {0: 1, 1: 1}, 'of': {1: 1}, 'python': {1: 1, 2: 1}, 'is': {2: 1}, 'a': {2: 1}, 'snake': {2: 1}}

'''

********
BONEYARD
********

Good try, but that's not exactly right. It seems like you're using sets instead of counting occurrences for each word in the documents. The task requires maintaining a count of each word's occurrences per document index. Would you like some help to adjust your approach?

It looks like you're using sets to store document indices, but you need to keep track of the count of each word in each document. Here's a small hint to guide you:

Instead of using a set, try using a dictionary for each word. This dictionary should have the document index as the key and the count of occurrences as the value.
How do you think you can modify your code to achieve this? 

It looks like you're on the right track, but there's a small adjustment needed. Currently, your code is not correctly updating the count of each word per document index. Here's a hint to help you:

When you encounter a word that's already in the index, you should check if the current document index is already a key in the nested dictionary. If it is, increment the count. If not, initialize it with a count of 1.
Try implementing this logic and see how it works! 😊


                # index[word] = {{doc_idx: (index.get(word, 0) + 1)}, index[word + 1]}
                # None
                # index[word] = {int(str(index[word])): "caca"}
                # print(type(index[word]), type(doc_idx))
                # index[word] = doc_idx


                # index[word] = doc_idx
                # None 
                # key is word (string)
                # value is dictionary | key is doc idx value word count
                
                # count_dict[element] = count_dict.get(element, 0) + 1
                # cnt = dict(index[word]).get(word, 0) + 1
                
                # print(index.get(word, 0))

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