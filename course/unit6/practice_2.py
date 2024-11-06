'''

Alright, Space Voyager! Let's apply our knowledge to something a tad trickier - an array of passwords, each one a unique mystery to be solved. Imagine you're working as a security analyst, huh? Your mission, if you choose to accept it, is to create a program to evaluate the strength of multiple passwords.

You are to write a function that takes a list of passwords as input. Each password in the list will be a non-empty string. The function should output a list of dictionaries, with each dictionary corresponding to a password in the original list. Each dictionary will have five keys: 'length', 'digit', 'uppercase', 'lowercase', and 'special_char'. The value for each key will be a Boolean indicating whether the password meets a particular criterion: has at least 8 characters for 'length', contains a digit for 'digit', contains an uppercase letter for 'uppercase', contains a lowercase letter for 'lowercase', and contains a special character (one of "!@#$%^&*()-+") for 'special_char'.

Get ready to dive into the world of security analysis – this is where the real fun begins!

'''

def password_strength_counter(password) :
# {
    special_characters = "!@#$%^&*()-+"
    strength = {
                "length": False,
                "digit": False,
                "lowercase": False,
                "uppercase": False,
                "special_char": False
                }

    if len(password) >= 8 :
    # {
        strength["length"] = True
    # }

    else :
    # {
        None
    # }

    for char in password :
    # {        
        if char.isdigit() :
        # {
            strength["digit"] = True
        # }
            
        elif char.islower() :
        # {
            strength["lowercase"] = True
        # }

        elif char.isupper() : 
        # {
            strength["uppercase"] = True
        # }

        elif char in special_characters :
        # {
            strength["special_char"] = True
        # }

        else :
        # {
            None
        # }

    # }

    return strength

# }

def multi_password_strength_counter(passwords) :
# {
    # implement this
    results = []
    
    for password in passwords :
    # {
        results.append(password_strength_counter(password))
    # }

    return results
# }

passwords = ["password", "Pa$$w0rd", "SuperSecurePwd!", "weakpw"]
results = multi_password_strength_counter(passwords)

for result in results :
# {
    print(result)
# }

# The expected output is:
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}
# {'length': True, 'digit': True, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': True, 'digit': False, 'lowercase': True, 'uppercase': True, 'special_char': True}
# {'length': False, 'digit': False, 'lowercase': True, 'uppercase': False, 'special_char': False}

'''

********
BONEYARD
********

# print('!', char, char in special_characters)

'''