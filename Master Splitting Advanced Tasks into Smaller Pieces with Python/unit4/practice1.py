'''

You are given a string representation of a nested JSON object. Each JSON object is represented by key-value pairs enclosed within curly braces {}. Keys and values are separated by colons :, and distinct entries in an object are separated by commas ,. A value in a JSON object can be a string, a number, or another nested JSON object. For simplicity, we will not consider arrays or null values in this task.

For example, the string "{\"key1\": \"value1\", \"key2\": {\"key3\": \"value3\", \"key4\": \"value4\"}, \"key5\": \"value5\"}" represents the following JSON object:

{
  "key1": "value1",
  "key2": {
    "key3": "value3",
    "key4": "value4"
  },
  "key5": "value5"
}

Your task is to transform the given string into a nested Python dictionary and then update a specific key-value pair within the dictionary. You should parse the JSON string into a Python dictionary and then update the value associated with the key "key4" to the given update_value. The string and the new value will be provided as input to your function. Your function should return the updated dictionary.

The input string will contain from 1 to 500 characters, inclusive. For this task, we'll assume that all keys in the JSON object are unique.

Example Input: "{\"key1\": \"value1\", \"key2\": {\"key3\": \"value3\", \"key4\": \"value4\"}, \"key5\": \"value5\"}", "newValue"

Expected Output:

{
  "key1": "value1",
  "key2": {
    "key3": "value3",
    "key4": "newValue"
  },
  "key5": "value5"
}

'''

import json

def update_dict(dictionary, key, value) :
# {
    # Iterate through all the key-value pairs in the dictionary
    for k in dictionary :
    # {
        # If the key matches the required key, update its value
        if (k == key) :
        # {
            dictionary[k] = value
        # }

        # If the value is a nested dictionary, recursively search for the key inside it
        elif (isinstance(dictionary[k], dict)) :
        # {
            update_dict(dictionary[k], key, value)
        # }

        else :
        # {
            None
        # }

    # }

    return dictionary

# }
             
def parse_string_and_update_value(input_string, update_key, new_value) :
# {
    # Parse the given string into a dictionary
    dictionary = parse_string(input_string)

    # Update the value of the specified key in the dictionary
    update_dict(dictionary, update_key, new_value)

    # Return the updated dictionary
    return dictionary

# }

def parse_string(input_string) :
# {
    # Preprocess the input_string: replace commas outside of curly brackets
    preprocessed_string = ""
    balance = 0

    for char in input_string :
    # {
        if (char == '{') :
        # {
            balance = balance + 1
        # }

        elif (char == '}') :
        # {
            balance = balance - 1
        # }

        elif (char == ',' and balance == 0) :
        # {    
            preprocessed_string = preprocessed_string + ';'
            # continue
        # }

        else :
        # {
            None
        # }

        preprocessed_string = preprocessed_string + char

    # }
             
    # Parse to a nested dictionary
    elements = preprocessed_string.split(';')
    result_dict = {}

    for element in elements :
    # {
        key, value = element.split(',', 1)

        if ('{' in value) :
        # {
            # Value is a nested dictionary
            nested_dict = parse_string(value[1: -1])
            result_dict[key] = nested_dict
        # }

        else :
        # {
            result_dict[key] = value
        # }

    # }

    return result_dict

# }

def solution(json_string, update_value) :
# {
    # TODO: implement the solution here    
    return update_dict(json.loads(json_string), "key4", update_value)
# }


json_string = "{\"key1\": \"value1\", \"key2\": {\"key3\": \"value3\", \"key4\": \"value4\"}, \"key5\": \"value5\"}"
update_value = "taco"

print(solution(json_string, update_value))

'''

***** BONEYARD *****

# return parse_string_and_update_value(json_string, "key4", update_value)
# print(json.loads(json_string))

# elements = elements.split('=', 1)
    
# print(element.split('=', 1))
# tmp = element.split('=', 1)
# tmp = element.split('=', 1)
# print(element)
# print(elements)
# key, value = element.split('=', 1)

# s = parse_string(json_string)
# parse_string_and_update_value

# print(json_string["key2"]["key4"])
# json_string["key2"]["key4"] = update_value

json_string = {
                "key1": "value1",
                "key2": {
                    "key3": "value3",
                    "key4": "value4"
                        },
                "key5": "value5"
                }

'''