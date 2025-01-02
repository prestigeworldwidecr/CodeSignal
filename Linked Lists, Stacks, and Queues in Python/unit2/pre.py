'''

Let's start with a common coding challenge - checking if the brackets in a string are balanced. Imagine that the string is the source code of a software application, and these brackets are the open and close statements for loops, if-else conditions, or function blocks in the source code. For the code to be valid and runnable, every open statement (bracket) must have a corresponding close statement (bracket) in the proper order.

To make this problem more relatable, let's consider this real-world scenario. You are part of a team developing a text editor for programming languages. As a value-added feature, you want to provide real-time feedback to the users of your text editor about the number of unbalanced brackets in their code to assist them in avoiding syntax errors. This problem accurately mimics such a feature where we are given a string of code, and our task is to check if all the brackets in the code are balanced.

If we consider a simple way to approach this problem, we could initialize a counter variable for each type of bracket (parentheses, braces, and square brackets), increment the counters when we encounter an opening bracket, and decrement it when we get a closing bracket. Although this approach checks whether we have a closing bracket for every opening bracket, it completely misses one critical aspect - the order of brackets. For the brackets to be considered balanced, every closing bracket must correspond to the most recently opened bracket of the same type, which is not checked in this approach.

An efficient way to solve this problem is by using a stack data structure. The stack follows the LIFO (Last In, First Out) principle, which makes it highly suitable when we want to track the opening and closing brackets' order, as the most recently opened bracket needs to be closed first before we move on to the next opening bracket.

We start by creating a dictionary that maps each opening bracket to its corresponding closing bracket and an empty stack. Then, we iterate over each character character in the string input_str:

If character is an opening bracket, it gets appended to the stack.
If character is a closing bracket and the top element in the stack is the corresponding opening bracket, we remove the top element from the stack.
If neither of the above conditions is met, we return False.
Finally, if the stack is empty (all opening brackets had matching closing brackets), we return True. If there are some unmatched opening brackets left, we return False.

This way, the stack helps us keep track of all opening brackets and ensures that every one of them gets their closing mate.

Continuing on to the next problem, we have the task of reversing the characters of a string using a Stack. This is quite a common task that you will often see in coding tests or interviews because it is a good demonstration of understanding the rules and principles of the Stack data structure.

Imagine you're tasked with building a function in which a user can input a string, and you need to display the reversed string as part of the application features. Or, as a more advanced example, in computer networks, stack buffers are often used to reverse the order of packets that arrive out of order. Understanding how to reverse the order of elements using a Stack is a crucial skill.

A direct approach for this problem is using built-in Python methods like string slicing on a list to revert it. But remember, the focus here is to integrate our understanding of the stack operations in solutions, so we will be oriented toward solving this problem using a Stack.

Thanks to the Last In First Out (LIFO) feature of the stack, it serves as an excellent tool to reverse elements' order. The strategy here is straightforward: push all the characters to a stack and then pop them out. As a result, we get the reversed string.

The list(input_str) breaks the string into characters and simulates a stack where each letter is stacked on top of the previous one. Then result += stack.pop() pops out the characters from the top of the stack (which is the reversed order as they were put in) and appends them to the result string. In the end, we get the string in reverse order.

Now, let's move on to another classic algorithmic problem - evaluating postfix expressions. In simple terms, a postfix expression is an arithmetic expression where operators are placed after their operands. For example, the expression 2 3 + is a simple postfix expression, which equals 5 when evaluated.

You've been given a task at work to build a small calculator application. This calculator should be capable of evaluating postfix expressions, as this form of notation eliminates the need for parentheses to indicate the execution order. This problem perfectly fits into such a scenario where you're given a postfix expression as a string; your task is to evaluate the expression and return the result.

One might think of directly parsing the expression from left to right and performing the operations. However, this won't work because it ignores one fundamental aspect of postfix expressions – an operator applies to the most recently seen numbers that haven't been used yet. This basic understanding of postfix expression pushes us to think about a certain data structure that we've encountered before.

The evaluation of postfix expressions can be efficiently done using a stack data structure. The stack follows the LIFO (Last In, First Out) principle, which is fitting in this scenario because we process the most recently encountered yet unused numbers first.

We create an empty stack. Then, we iterate over each character operand in the expression. If operand is a number, we push it onto the stack. If operand is an operator, we pop two numbers from the stack, perform the operation, and push the result back onto the stack. After we have processed all characters of the expression, the stack should contain exactly one element, the result of the expression.



'''

def are_brackets_balanced(input_str) :
# {
    brackets = set(["(", ")", "[", "]", "{", "}"])
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []

    for character in input_str :
    # {
        if (character not in brackets) :
        # {
            # Skipping non-bracket characters
            # continue
            None
        # }

        else :
        # {
            None
        # }

        if (character in open_par) :
        # {
            stack.append(character)
        # }

        elif (stack and character == bracket_map[stack[-1]]) :
        # {
            stack.pop()
        # }

        else :
        # {
            return False
        # }

    # }

    return len(stack) == 0

# }

def reverse_strng(input_str) :
# {
    stack = list(input_str)
    result = ""

    while (len(stack)) :
    # {    
        result = result + stack.pop()
    # }

    return result

# }

def evaluate_postfix(expression) :
# {
    stack = []
    
    for element in expression.split(' ') :
    # {
        if (element.isdigit()) :             
        # {
            stack.append(int(element))
        # }

        else :
        # {
            operand2 = stack.pop()
            operand1 = stack.pop()
            
            if (element == '+') : 
            # {
                stack.append(operand1 + operand2)
            # }

            elif element == '-' : 
            # {
                stack.append(operand1 - operand2)
            # }
            
            elif element == '*' : 
            # {
                stack.append(operand1 * operand2)
            # }
            
            elif element == '/' : 
            # {
                stack.append(operand1 / operand2)
            # }

            else :
            # {
                None
            # }

        # }

    # }
    
    return stack[0]

# }

'''

***** BONEYARD *****

'''