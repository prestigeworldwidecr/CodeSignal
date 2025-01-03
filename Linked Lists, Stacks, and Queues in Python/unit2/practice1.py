'''

You've got a string with brackets (like '(', ')', '[', ']', '{', '}',) and alphanumeric characters. Your objective, like a seasoned code wrangler, is to ride through the string and confirm if all those brackets are balanced, cowboy! Balanced, you ask? That's a lingo for saying every open bracket gets closed correctly. They gotta pair-up right with the same kinda bracket with no mismatched varmints in-between. But the alphanumeric characters? Just take them as tumbleweeds.

Your task is to write a function that takes this mixed-up string as input and returns True if the brackets balance perfectly or False if they are a wild mess. Buckle up!

'''

def are_brackets_balanced(s) :
# {
    # implement this
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_brackets = set(["(", "[", "{"])
    stack = []

    for character in s :
    # {
        if (character in open_brackets) :
        # {
            stack.append(character)
        # }

        elif (stack and character == bracket_map[stack[-1]]) :
        # {
            stack.pop()
        # }

        else :
        # {
            None
        # }

    # }

    return len(stack) == 0

# }

print(are_brackets_balanced("(abc[d]{fg})"))  # Expected output: True
print(are_brackets_balanced("(a[bcd{fg}h]i)"))  # Expected output: True
print(are_brackets_balanced("(abc{d[fg]h)i"))  # Expected output: False
print(are_brackets_balanced("({a[bcd]})"))  # Expected output: True

'''

***** BONEYARD *****

# return False

# brackets = set(["(", ")", "[", "]", "{", "}"])

        else :
        # {
            None
        # }

if (character in brackets) :
        # {
            # Skipping non-bracket characters
            # continue
            None
        # }

        el

'''