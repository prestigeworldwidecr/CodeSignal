'''

Problem 1: Efficient Approach Explanation
This is where Python dictionaries shine. A Python dictionary allows us to store data in key-value pairs. In this case, we can use each unique word in the text as a key and the frequency of the word as its corresponding value. As we traverse the document once, we can record the count of each word on the go, avoiding the need for multiple full-document checks. Hence, using a dictionary would drastically reduce our algorithm's time complexity and boost its efficiency.

Problem 1: Solution Building
Now, let's put this efficient approach into effect with some Python code and dive into its step-by-step explanation.

Problem 2: Password Strength Counter
As an application developer, ensuring the security of user data is pivotal. A common measure to ensure robust security is testing the strength of passwords. A 'strong' password is usually defined as one that is long (at least 8 characters) and includes a mix of uppercase characters, lowercase characters, and digits.

Problem 3: Bonus Calculator
As a software developer in an HR or Finance team, you might need to work on tasks related to personnel management. For instance, suppose your firm has just approved a new policy to give all developers a bonus equal to 10% of their salary. Your task is to update the database to reflect this new policy.

'''

from collections import defaultdict

def frequent_words_finder(text) :
# {
    text = text.lower()
    word_counts = defaultdict(int)
    word_list = text.split()

    for word in word_list : 
    # {
        word_counts[word] = word_counts[word] + 1
        top_three = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:3]
    # }

    print(top_three)

    return top_three

# }

def password_strength_counter(password) :
# {
    strength = {
                'length': False,
                'digit': False,
                'lowercase': False,
                'uppercase': False,
                }

    if len(password) >= 8 :
    # {
        strength['length'] = True
    # }

    else :
    # {
        None
    # }

    for char in password :
    # {
        if char.isdigit() :
        # {
            strength['digit'] = True
        # }
            
        elif char.islower() :
        # {
            strength['lowercase'] = True
        # }

        elif char.isupper() : 
        # {
            strength['uppercase'] = True
        # }

        else :
        # {
            None
        # }

    # }

    return strength

# }

def bonus_calculator(employees) :
# {
    for employee in employees :
    # {
        bonus = 0

        if employee['role'] == 'developer' :
        # {
            bonus = employee['salary'] * 0.1
        # }

        else :
        # {
            None
        # }
        
        employee['bonus'] = bonus
    # }

    return employees

# }

'''

********
BONEYARD
********

'''