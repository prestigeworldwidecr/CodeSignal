'''

As a starting point, let's consider a familiar task where you have a list of integers generated randomly. You need to sort this list in ascending order. In our e-library example, this task could be likened to arranging the books based on their unique ID numbers.

Python has a built-in function called sorted() that sorts a given list without modifying the original one. Instead, it returns a new list with the elements of the original list in sorted order. Here's how we can solve this problem:

Next, suppose you need to sort a list of integers, but this time in descending order. For instance, you might want to arrange the e-library's books based on their publication year, with the most recent ones appearing first.

The sorted() function is again handy here, but we need to set its reverse argument to True. Here's how to do that:

Next, consider a situation where you need to sort a list of tuples. Each tuple contains two elements — an integer and a string (for instance, the integer might be a unique ID representing a book, and the string is the book's title). You want to arrange these tuples based on the strings.

The sorted() function can sort complex data structures like tuples using the key parameter. This parameter defines a function that takes an input element and returns a key that Python will use for sorting purposes. To sort the tuples based on the second element (i.e., the string), we'll use a lambda function as the key. Here's your solution:

The lambda function x: x[1] takes an element from tuples and returns its second element (i.e., x[1]). The sorted() function uses these second elements to sort the tuples.

On top of that, if the second element can include ties we need to eliminate, a tuple comes to the rescue, as tuples in Python are automatically comparable:

This code will now sort the values list, first sorting by the x[1] value and, in case of a tie, sorting by the x[0] value.

For our final case, imagine that you have a dictionary where each key-value pair represents the title of a book (as a key) and its corresponding author's name (as a value). Your task is to sort this dictionary based on the authors' names and return a list of tuples, where each tuple is a key-value pair from the dictionary.

Python provides the items() method, converting a dictionary into a list of its key-value pairs as tuples. We can then sort this list using sorted() and the key parameter. Let's see this in action:

'''

def sort_list(values) :
# {
    return sorted(values)
# }

def sort_list(values) :
# {
    return sorted(values, reverse = True)
# }

def sort_tuples(tuples) :
# {
    return sorted(tuples, key = lambda x: x[1])
# }

def sort_tuples_ties(values) :
# {
    return values.sort(key = lambda x: (x[1], x[0]))
# }

def sort_dict(dictionary) :
# {
    return sorted(dictionary.items(), key = lambda x: x[1])
# }

'''

**********  BONEYARD  **********

'''