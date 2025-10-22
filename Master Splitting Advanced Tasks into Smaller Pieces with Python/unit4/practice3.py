'''

You are given a delimited text file consisting of user information. Each row represents a user, with a unique identifier followed by the user's details, structured as a comma-separated key-value string. However, this data is not flat. Some values in the key-value pair can be another key-value string, enclosed in parentheses and separated by semicolons.

The input structure for each line is as follows:

"ID,Key1=Value1,Key2=(SubKey1=SubValue1;SubKey2=SubValue2),Key3=Value3,...".

For example, "001,Age=25,Name=John,Address=(Street=Main St;City=NY;Zip=10001),Email=john@gmail.com".

Your task is to write a Python function that will parse this data and output a list of Python dictionaries, one dictionary for each user's information. Each dictionary should translate the user's details from the string into key-value pairs, including the nested structure. Then, you need to update a specific user's detail, identified by the unique identifier and the key name. Let's assume you need to update the Email of the user with ID "001".

Your Python function should first parse these lines into the above dictionaries, then locate the appropriate user and detail to update. The function should ultimately return the updated list of dictionaries.

Constraints:

The number of users in the file is limited to 500.
Each ID is unique and comprises alphanumeric characters only.
Each Key (and SubKey) in the user data is an alphanumeric string without spaces.
Each Value (and SubValue) can be any alphanumeric string and may contain spaces.
The SubValue strings may contain other nested key-value pairs but not more than one level deep (i.e., no nested key-value pairs within SubValue strings).
The key-value pairs do not repeat. If one user’s data includes a key-value pair, no other user’s data will have the same key-value pair.
All strings are case-sensitive.
Here's an example of how the function should work:

Input Data:

'001,Age=25,Name=John,Address=(Street=Main St;City=NY;Zip=10001),Email=john@gmail.com\n002,Age=30,Name=Jane,Address=(Street=2nd St;City=LA;Zip=90001),Email=jane@hotmail.com'

UserID to Update: '001'

Key to Update: 'Email'

New Value: 'johndoe@gmail.com'

Output:

[
    {
        '001': {
            'Age': '25',
            'Name': 'John',
            'Address': {
                'Street': 'Main St',
                'City': 'NY',
                'Zip': '10001'
            },
            'Email': 'johndoe@gmail.com'
        }
    },
    {
        '002': {
            'Age': '30',
            'Name': 'Jane',
            'Address': {
                'Street': '2nd St',
                'City': 'LA',
                'Zip': '90001'
            },
            'Email': 'jane@hotmail.com'
        }
    }
]

Great! Here’s a small hint to get you started:

Try splitting each line by the first comma to separate the user ID from the rest.
For the rest, you’ll need to split by commas, but be careful—if you’re inside parentheses, you shouldn’t split!
When you see something like Key=(SubKey1=SubValue1;SubKey2=SubValue2), treat the value as a nested dictionary.
How might you keep track of whether you’re inside parentheses while looping through the string?

No worries! Here’s a guiding question:

When looping through the string, how could you use a variable (like balance or depth) to count how many open parentheses ( you’ve seen versus closed ones )?
If balance is 0, you’re outside any parentheses—so a comma here means a new key-value pair.
If balance is greater than 0, you’re inside parentheses—so ignore commas until you close them.
Try writing a loop that builds each key-value pair this way. Want to try this step, or need a bit more structure?

Great question! In this practice, nesting only goes one level deep—so you’ll never have parentheses inside other parentheses. For example:

Valid: Address=(Street=Main St;City=NY)
Not valid: Address=(Street=(Name=Main;Type=Road);City=NY)
Here’s a bit more structure for your parser:

Split each line by the first comma to get the user ID and the rest of the data.
Loop through the rest of the line character by character:
Keep a balance counter for parentheses.
Build up a current string for each key-value pair.
When you hit a comma and balance is 0, you’ve finished a key-value pair—add it to a list and reset current.
If you hit (, increase balance. If you hit ), decrease balance.
For each key-value pair:
If the value starts with ( and ends with ), split the inside by ; to get subkey-subvalue pairs and build a nested dictionary.
Otherwise, just store the value as a string.
Does this help you get started? Want to try implementing step 2?

Great question! The issue is in your update_dict function. When you update a field like Address with a new value that is a nested string (e.g., "(Street=3rd Ave;City=SF;Zip=94101)"), your code currently just assigns the string as the value, rather than parsing it into a dictionary.

In your code, this happens here:

if (k == key) :
    dictionary[k] = value

This line simply assigns the new value, regardless of whether it should be a nested dictionary.

What should you do instead?

Before assigning, check if the new value is a nested string (starts with ( and ends with )).
If so, parse it into a dictionary (using your parsing logic for nested values) before assigning.
Try updating your update_dict like this:

if k == key:
    if isinstance(value, str) and value.startswith('(') and value.endswith(')'):
        # Parse the nested string into a dictionary
        value = {kv.split('=')[0]: kv.split('=')[1] for kv in value[1:-1].split(';')}
    dictionary[k] = value

This way, when you update Address, it will be a dictionary, not a string.

Summary:
You need to update your assignment in update_dict to parse nested strings into dictionaries before assigning. Give this a try!

Great question! Here’s what you need to do:

You should update the part of your code where you are updating the user’s detail (inside your solution function).
Right now, you have this:

for r in result:
    if (userid in r.keys()):
        r = update_dict(r, key, new_value)

But your update_dict function is not updating the value inside the nested user dictionary; instead, it’s adding the key at the top level or returning a new dictionary.

What you want is:

Find the dictionary for the user with the matching userid.
Update the value for key inside that user's dictionary.
If the new value is a nested string (starts with ( and ends with )), parse it into a dictionary before assigning.
Replace your update logic with something like:

for r in result:
    if userid in r:
        # Check if new_value is a nested string
        if isinstance(new_value, str) and new_value.startswith('(') and new_value.endswith(')'):
            # Parse the nested string into a dictionary
            nested = {}
            for kv in new_value[1:-1].split(';'):
                k, v = kv.split('=', 1)
                nested[k] = v
            r[userid][key] = nested
        else:
            r[userid][key] = new_value

Summary:

This code goes inside your main solution function, replacing the part where you update the user’s detail.
You do not need a separate update_dict function for this—just update the value directly in the user’s dictionary.
Let me know if you want to see how to clean up your parsing logic too!

'''

def update_dict(dictionary, key, value, userid) :
# {
    tmp = {}
    
    if (isinstance(value, str) and value.startswith('(') and value.endswith(')')) :
    # {
        for kv in value[1: -1].split(';') :
        # {
            k, v = kv.split('=', 1)
            tmp[k] = v
        # }

        dictionary[userid][key] = tmp

    # }

    else :
    # {
        dictionary[userid][key] = value
    # }

    # dictionary[key] = value

    return dictionary

# }

def parse_string(input_string) :
# {    
    result = {}
    data_dict = {}
    sub_data = ""
    sub_data_header = ""
    sub_data_dict = {}

    s = input_string.replace('=', ':')
    s = s.replace('(', '{')
    s = s.replace(')', '}')
    s = s.split(',')
    username = s[0]
    data = s[1 : len(s)]

    for d in data :
    # {
        d = d.split(':')
        sub_data_header = d[0]

        if (len(d) < 2) :
        # {
            None
        # }

        elif ('{' in d[0]) :
        # {
            sub_data = str(d).replace(';', ", ")
            sub_data = sub_data.replace('{', '')
            sub_data = sub_data.replace('}', '')
            sub_data = sub_data.replace("'", '')
            sub_data = sub_data.replace(';', ", ")
            sub_data = sub_data.replace('[', '')
            sub_data = sub_data.replace(']', '')
            sub_data = sub_data.replace('"', '')
            sub_data = sub_data.split(',')
            i = 0
            j = 1
            
            while (i < len(sub_data) - 1) : 
            # {             
                tmp1 = sub_data[i]
                tmp2 = sub_data[j]

                if (tmp1[0] == ' ') :
                # {
                    tmp1 = tmp1[1 : len(tmp1)]
                # }

                else :
                # {
                    None
                # }

                if (tmp2[0] == ' ') :
                # {
                    tmp2 = tmp2[1 : len(tmp2)]
                # }

                else :
                # {
                    None
                # }

                data_dict[tmp1] = tmp2
                i = i + 2
                j = i + 1
            # }

        # }
        
        elif ('{' in d[1]) :
        # {
            sub_data = str(d[1 : len(d)])
            sub_data = sub_data.replace('{', '')
            sub_data = sub_data.replace('}', '')
            sub_data = sub_data.replace("'", '')
            sub_data = sub_data.replace(';', ", ")
            sub_data = sub_data.replace('[', '')
            sub_data = sub_data.replace(']', ", ")
            sub_data = sub_data.split(',')
            i = 0
            j = 1
            
            while (i < len(sub_data) - 1) : 
            # {             
                tmp1 = sub_data[i]
                tmp2 = sub_data[j]

                if (tmp1[0] == ' ') :
                # {
                    tmp1 = tmp1[1 : len(tmp1)]
                # }

                else :
                # {
                    None
                # }

                if (tmp2[0] == ' ') :
                # {
                    tmp2 = tmp2[1 : len(tmp2)]
                # }

                else :
                # {
                    None
                # }

                sub_data_dict[tmp1] = tmp2
                data_dict[sub_data_header] = sub_data_dict
                i = i + 2
                j = i + 1
            # }

        # }

        else :
        # {
            tmp = d[1]
            
            if (tmp[0] == ' ') :
            # {
                tmp = tmp[1 : len(tmp)]
            # }

            else :
            # {
                None
            # }
            
            data_dict[sub_data_header] = tmp

        # }

    # }

    result[username] = data_dict
    return result

# }

def solution(data, userid, key, new_value) :
# {
    users = data.split("\n")
    result = []

    for user in users : 
    # {
        result.append(parse_string(user))
    # }

    for r in result :
    # {
        if (userid in r.keys()) :
        # {
            r = update_dict(r, key, new_value, userid)
        # }

        else :
        # {
            None
        # }

    # }

    # print(result)

    return result

# }

data = "001,Age=25,Name=John,Address=(Street=Main St;City=NY;Zip=10001),Email=john@gmail.com\n002,Age=30,Name=Jane,Address=(Street=2nd St;City=LA;Zip=90001),Email=jane@hotmail.com"

# data = "001,Age=25,Name=John,Address=(Street=Main St;City=NY;Zip=10001),Email=john@gmail.com\n002,Age=30,Name=Jane,Address=(Street=2nd St;City=LA;Zip=90001),Email=jane@hotmail.com', '001', 'Email', 'johndoe@gmail.com"

# data = "001,Name=John,Address=(Street=Main St;City=NY;Zip=10001),Email=john@gmail.com\n002,Name=Jane,Address=(Street=2nd St;City=LA;Zip=90001),Email=jane@hotmail.com', '002', 'Address', '(Street=3rd Ave;City=SF;Zip=94101)"

data = "'002', 'Address', '(Street=3rd Ave;City=SF;Zip=94101)"

userid = "001"
key = "Email"
new_value = "johndoe@gmail.com"

print(solution(data, userid, key, new_value))

'''

***** BONEYARD *****

# Parse the nested string into a dictionary

# value = {kv.split('=')[0]: kv.split('=')[1] for kv in value[1:-1].split(';')}


# value = {kv.split('=')[0]: kv.split('=')[1]}

for r in result:

    if userid in r:
        # Check if new_value is a nested string
        if isinstance(new_value, str) and new_value.startswith('(') and new_value.endswith(')'):
            # Parse the nested string into a dictionary
            nested = {}
            for kv in new_value[1:-1].split(';'):
                k, v = kv.split('=', 1)
                nested[k] = v
            r[userid][key] = nested
        else:
            r[userid][key] = new_value
    

for k in dictionary :
# {
    if (k == key) :
    # {
        dictionary[k] = value
    # }

    elif (isinstance(dictionary[k], dict)) :
    # {
        update_dict(dictionary[k], key, value)
    # }

    else :
    # {
        None
    # }

# }
             
def parse_string_and_update_value(input_string, update_key, new_value) :
# {    
    dictionary = parse_string(input_string)
    update_dict(dictionary, update_key, new_value)

    return dictionary
# }

# print('*', d[0], d[1])

            
# print('%', d[1])



# print('#', d, data, len(d))            
                

# print(tmp1, tmp2)
# data_dict[sub_data_header] = sub_data_dict

# print (sub_data_dict)

# print(sub_data)


            
# print('&', sub_data)

# print('&', sub_data)

# print(type(d[0]), len(d), d, d[0])
            
           
# print(sub_data)


# print("hello", d, len(d))

    # print('1', result)

# tmp = {}
# print(data)
# category = ""


# d = d.split(';')
# print('{', d[1 : len(d)], len(d))
# print('$', d[0])
# sub_data_header = d[0]
# print('^', sub_data, len(sub_data), sub_sub_data)
# sub_data_dict[sub_data[0]] = sub_data[1 : len(d)]
# for sub_d in d[1]
# print(len(sub_data))

# for i in range(len(sub_data)) :
# {
# print(i)
# i = i + 1
# print(tmp1, tmp2)
# sub_data_dict[sub_data[i]] = sub_data_dict[sub_data[i + 1]]
# sub_data_dict[sub_data_header][tmp1] = tmp2
# sub_data_dict[sub_data_header] = tmp
# print('$', sub_data_dict)
# d = d.split(':')
# print('!', sub_data_dict)
# result[username] = data_dict
# print('1', result)

# sub_sub_data = []

# print(d)

# print(d, len(d))
# tmp[d[0]] = d[1]
# print(tmp)

# result[s[0]] = s[1 : len(s) - 1]

# print(username, data)

# TODO: implement the solution following the task description
        
# Iterate through all the key-value pairs in the dictionary

# print(k, key)

# If the key matches the required key, update its value
# If the value is a nested dictionary, recursively search for the key inside it

# Parse the given string into a dictionary
    
# Update the value of the specified key in the dictionary

# Return the updated dictionary


# Preprocess the input_string: replace commas outside of curly brackets
    preprocessed_string = ""
    balance_bracket = 0
    balance_paren = 0
    cnt = 0
    # current = ""
    pairs = []
    result_dict = {}

    for char in input_string :
    # {
        if (char == '{') :
        # {
            print('2')
            balance_bracket = balance_bracket + 1
        # }

        elif (char == '}') :
        # {
            balance_bracket = balance_bracket - 1
        # }

        elif (char == ',' and balance_bracket == 0) :
        # {
            preprocessed_string = preprocessed_string + ";"
        # }

        else :
        # {
            preprocessed_string = preprocessed_string + char
        # }
            
    # }

    elements = preprocessed_string.split(';')

    for element in elements :
    # {
        # username comes first
        if (cnt == 0) :
        # {
            username = [element.split('=', 1)]
            username = username[0][0]
            result_dict[username] = {}
            cnt = cnt + 1
        # }
        
        else :
        # {
            key, value = element.split('=', 1)

            if ('{' in value) :
            # {
                # Value is a nested dictionary
                nested_dict = parse_string(value[0: 1: -1])
                result_dict[username][key] = nested_dict
            # }            

            else :
            # {
                result_dict[username][key] = value
            # }

        # }

    # }

    for d in result_dict.values() :
    # {
        print('1', d, type(d))
        # None
    # }

    # print(result_dict.values())

    return result_dict

# pairs = []
# balance_paren = 0

for char in input_string :
# {
    if char == '(' :
    # {
        balance_paren = balance_paren + 1
        preprocessed_string = preprocessed_string + char
    # }

    elif (char == ')') :
    # {
        balance_paren = balance_paren - 1
        preprocessed_string = preprocessed_string + char
    # }

    elif (char == ',' and balance_paren == 0) :
    # {
        pairs.append(preprocessed_string)
        preprocessed_string = ""
    # }

    else :
    # {
        preprocessed_string = preprocessed_string + char
    # }

# }

print('@', preprocessed_string, pairs)

pairs = []
current = ""
balance = 0

for char in line:
    if char == '(':
        balance += 1
        current += char
    elif char == ')':
        balance -= 1
        current += char
    elif char == ',' and balance == 0:
        pairs.append(current)
        current = ""
    else:
        current += char

if current:
    pairs.append(current)
        
if (char == '(') :
# {
    balance1 = balance1 + 1
# }

elif (char == ')') :
# {
    balance1 = balance1 - 1
# }
elif (char == ',' and balance1 == 0) :
# {
    preprocessed_string = preprocessed_string + ";"
# }

# elements = preprocessed_string.split("',")
# print('!', elements)

elif ('(' in element and ')' in element) :
# {
    print("hey")
# }
        
result_dict = {}
# print(element)

    # tmp = element.split('=', 1)
    # print(len(tmp), tmp)
    # print(value)

    # check if '(' ')'

# preprocessed_string1 = ""

# input_string = input_string.replace('(', '{')
# input_string = input_string.replace(')', '}')
# print('@', input_string)
# print('@', preprocessed_string)

# Parse to a nested dictionary
# print('!', preprocessed_string)

# print('!', elements)
# username = [element.split('=', 1)]
# result_dict[username] = {}


# print(result)
# def parse_string_and_update_value(input_string, update_key, new_value)

# username = 


# r[userid][key] = new_value
# print(userid)
# result = parse_string_and_update_value(r, key, new_value)

# print('!')


# print(dictionary[k], k, key)
# print(dictionary[k], k, key)

elif ('(' in value) :
# {
    # Value is a nested dictionary
    # nested_dict = parse_string(value[0: 1: -1])
    # result_dict[username][key] = nested_dict
    print('%')
# }


# else :
# {
    # None
# }


for char in preprocessed_string :
# {
    if (char == '(') :
    # {
        balance = balance + 1
    # }

    elif (char == ')') :
    # {
        balance = balance - 1
    # }

    elif (char == ',' and balance == 0) :
    # {
        preprocessed_string1 = preprocessed_string1 + ";"
        continue
    # }
        
    # else :
    # {
        # None
    # }

    preprocessed_string1 = preprocessed_string1 + char
        
# }

# preprocessed_string = preprocessed_string.replace("',", "'")

elif (char == '(') :
# {
    balance = balance + 1
# }

elif (char == ')') :
# {
    balance = balance - 1
# }

users = data.split("\n")
result = []

for user in users : 
# {
    result.append(parse_user(user))
# }

result = update_dict(result, userid, key, new_value)

return result

def update_dict(result, userid, key, new_value) :
# {
    for r in result :
    # {
        if (userid in r.keys()) :
        # {
            r[userid][key] = new_value
        # }

        else :
        # {
            None
        # }

    # }

    return result

# }

def parse_address(address_data) :
# {
    address = {}
    ad = address_data.split('(')
    
    address["Address"] = {}
    address_blop = ad[1].replace(')', '')
    address_blop = address_blop.split(';')
    street_data = address_blop[0].split('=')
    city_data = address_blop[1].split('=')
    zip_data = address_blop[2].split('=')

    
    address["Address"][street_data[0]] = street_data[1]
    address["Address"][city_data[0]] = city_data[1]
    address["Address"][zip_data[0]] = zip_data[1]

    return address
# }

def parse_user(user) :
# {
    user_data = user.split(',')
    result = {}
    user = None

    for u in user_data :
    # {
        if ('=' not in u) :
        # {
            user = u
            result[u] = {}
        # }

        else :
        # {
            None
        # }

    # }

    for u in user_data :
    # {
        if ("Age" in u) :
        # {
            age_data = u.split('=')
            result[user][age_data[0]] = age_data[1]
        # }

        else :
        # {
            None
        # }

    # }

    for u in user_data :
    # {
        if ("Name" in u) :
        # {
            name_data = u.split('=')
            result[user][name_data[0]] = name_data[1]
        # }

        else :
        # {
            None
        # }

    # }

    for u in user_data :
    # {
        if ("Address" in u) :
        # {
            address_data = parse_address(u)
            result[user].update(address_data)
        # }

        else :
        # {
            None
        # }

    # }

    for u in user_data :
    # {
        if ("Email" in u) :
        # {
            email_data = u.split('=')
            result[user][email_data[0]] = email_data[1]
        # }

        else :
        # {
            None
        # }

    # }

    return result

# }
 
# age_data = u

# print(age_data)
# print(address_data)
# print(result)

# print(userid in r.keys())


# print('!', r, key, type(key), r[userid]["Email"])

# age_data = None
# name_data = None
# address_data = None
# email_data = None

# print('=' not in user_data)

for u in user_data :
# {
    if ("Age" in u) :
    # {
        # age = age_data.split('=')
        None
    # }

    elif ("Name" in u) :
    # {
        # result[u] = {}
        None
    # }

    elif ("Address" in u) :
    # {
        # result[u] = {}
        None
    # }

    elif ("Email" in u) :
    # {
        # result[u] = {}
        None
    # }

    else :
    # {
        None
    # }

# }

# print(u)
# print(u)
# print(user_data, len(user_data), type(user_data[1]), '=' in user_data[0])
# print(user)

result = {}
user_data = user.split(',')
user = user_data[0]
age_data = user_data[1].split('=')
name_data = user_data[2].split('=')
address_data = user_data[3]
email_data = user_data[4].split('=')

result[user] = {}
result[user][age_data[0]] = age_data[1]
result[user][name_data[0]] = name_data[1]

address_data = parse_address(address_data)
result[user].update(address_data)

result[user][email_data[0]] = email_data[1]

return result

# print(address)

# print(result)
# can have all or no attributes

# result = {}
# print(street_data, city_data, zip_data)
# print(address["address"])

# print(address_data)


# print(user, age_data, name_data, email_data)
# print(result, address_data)
    
# print(address_data)

# ad = address_data.split(';')
# address_tag = ad[0]
# ad[1] = ad[1].replace('(', '')
# print(address_blop)
# print(ad, len(ad), ad[0])
# print(result, ad, ad[1])

# users = []
# users = []


'''