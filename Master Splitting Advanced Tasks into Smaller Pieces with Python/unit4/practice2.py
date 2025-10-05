'''

Imagine that you are a database manager dealing with a data structure in the form of a complex nested string. This string contains user data and is structured in such a way that user attributes are separated by semicolons (;), and within each user, the attribute-value pairs are separated by colons (:). Some of the user attributes themselves contain nested attribute-value pairs, which are enclosed in curly braces ({}).

Here's an example of such a string:

"User1:Age1=21;Location1=USA;Preferences1={Food1=Italian; Sport1=Fencing};User2:Age2=30; Location2=Canada; Preferences2={Music2=Jazz; Color2=Blue}".

You need to write a Python function that will convert the string into a nested dictionary, following the structure shown in the string. After the string has been converted into a dictionary, the function should update the value of a user-preference pair for any user to a requested value and return the updated dictionary.

In this string, the keys representing the user names contain numbers (User1, User2, etc.). You should also provide an option to find users by their numerical indices following the "User" keyword, such as 1 for User1, 2 for User2, and so on.

Your function should take the input string, the user index, the preference key, and the new value for the preference pair, and should return the updated dictionary in the end.

The size of the input string will be less than or equal to 500 characters.

Example:

Input:

input_string: "User1:Age1=21;Location1=USA;Preferences1={Food1=Italian;Sport1=Fencing};User2:Age2=30;Location2=Canada;Preferences2={Music2=Jazz;Color2=Blue}"
user_index: 1
pref_key: "Sport1"
new_value: "Hockey"
Output:

{
  'User1': {'Age1': '21', 'Location1': 'USA', 'Preferences1': {'Food1': 'Italian', 'Sport1': 'Hockey'}}, 
  'User2': {'Age2': '30', 'Location2': 'Canada', 'Preferences2': {'Music2': 'Jazz', 'Color2': 'Blue'}}
}

'''

def parse_nested(input_string) :
# {
    result = {}
    elements = input_string.split("};")

    for elem in elements :
    # {
        user = elem.split(';')
        username = ""

        for info in user :
        # {
            if ("User" in info) :
            # {
                user = info.split(':')
                username = user[0]   
                result[user[0]] = {} 
                age = user[1].split('=')
                result[user[0]] = {age[0] : age[1]}
            # }

            elif ("Location" in info) :
            # {
                location = info.split('=')
                result[username][location[0]] = location[1]
            # }

            elif ("Preference" in info) :
            # {
                preference = info.split('=')
                result[username][preference[0]] = {}
                result[username][preference[0]][preference[1].replace('{', '')] = preference[2]
            # }

            elif ("Sport" in info) :
            # {
                sport = info.split('=')
                result[username][preference[0]][sport[0]] = sport[1].replace('}', '')
            # }

            elif ("Music" in info) :
            # {
                music = info.split('=')
                result[username][preference[0]][music[0]] = music[1].replace('}', '')
            # }

            elif ("Color" in info) :
            # {
                color = info.split('=')
                result[username][preference[0]][color[0]] = color[1].replace('}', '')
            # }

            else :
            # {
                None
            # }

        # }

    # }
    
    return result
# }

def update_dict(dictionary, user_index, pref_key, new_value) :
# {
   
    preference_key = "Preferences" + str(user_index)
    i = 1
    # result =

    for user in dictionary :
    # {
        # If the key matches the required key, update its value
        if (user_index == i) :
        # {
            dictionary[user][preference_key][pref_key] = new_value
        # }

        else :
        # {
            None
        # }

        i = i + 1

    # }

    return dictionary

# }

def solution(input_string, user_index, pref_key, new_value) :
# {
    # TODO: Implement the function
    result = parse_nested(input_string)
    result = update_dict(result, user_index, pref_key, new_value)

    return result
# }

input_string = "User1:Age1=21;Location1=USA;Preferences1={Food1=Italian;Sport1=Fencing};User2:Age2=30;Location2=Canada;Preferences2={Music2=Jazz;Color2=Blue}"
user_index = 1
pref_key = "Sport1"
new_value = "Hockey"

print(solution(input_string, user_index, pref_key, new_value))

'''

***** BONEYARD *****

# print("User" + str(user_index), dictionary[user]["Preference" + ])
# print(user, dictionary[user])

# dictionary[username][preference_key][pref_key] = new_value

# print(username, preference_key)
                                   
# print(info)


# print(result)
# print('@', preference[0])
# print(result)
# print('@', preference[0])
# print('@', preference[0])
# print('!', color[1], color[1].replace('}', ''))
# tmp = color[1].replace('}', '')
# print('!', tmp)
# username = "User" + str(user_index)
# user = info.split(':')
# username = user[0]

i = 1
    
# Iterate through all the key-value pairs in the dictionary
# for user in dictionary :
# {
    # If the key matches the required key, update its value
    if (user_index == i) :
    # {
        print("User" + str(user_index), dictionary[user]["Preference" + ])
    # }

    else :
    # {
        None
    # }

    i = i + 1

# }

# print(i, user, dictionary[user], type(dictionary[user]))

# for info, value in dictionary[user] :
# {
    # print(len(info))
# }

# update_dict(dictionary[k], user_index, pref_key, new_value)

# print(dictionary[user].keys(), dictionary[user].values())

for preference in dictionary[user].values() :
# {
    if (isinstance(dictionary[user].values(), dict)) :
    # {
        # update_dict(dictionary[k], key, value)
        print(preference)
    # }

    else :
    # {
        None
    # }

# }

# dictionary[k] = new_value

# If the value is a nested dictionary, recursively search for the key inside it
elif (isinstance(dictionary[k], dict)) :
# {
    # update_dict(dictionary[k], "user" + i, value)
    None
# }

# import json

# print(len(preference), preference)
              
# tmp1 = 
# print(tmp1[0])              
# print(result, len(tmp1), tmp1[1])
# print(result)
# print('!', tmp3, result[username])
# print(result)

# print(input_string.split(';'))

# print(input_string.split(';'))
# print(input_string.split(','))
# tmp = input_string.replace("}", "}abc")

# print('}' in tmp)

# print(len(tmp), tmp, '!', tmp[0], tmp[1])

# if ("User" in tmp[0]) :
# {
    # print('!')
# }

    # print(elem)

'''