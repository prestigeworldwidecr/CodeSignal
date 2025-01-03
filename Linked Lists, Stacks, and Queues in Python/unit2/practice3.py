'''

Alright, small star! We have a fun task that involves playing around with a funky kind of math called inverse operations. Here's the deal: you're to evaluate a postfix expression, but here's the twist - the second operand operates on the first, not the other way around! So, 2 3 -, usually ends up making -1, right? Not this time! In this scenario, it equals 1 (3 - 2 = 1).

Eager to give it a whirl? Here are the details:

Input: You'll receive a string containing numbers and operations, where numbers and operations are separated by spaces (for example: "2 3 -"). You're safe to assume that there won't be any division by zero.
Output: Your aim is to return the evaluated result as a number.

'''

def evaluate_postfix_inverse(expression) :
# {
    # implement this
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
            
            match (element) :
            # {
                case '+':
                    stack.append(operand1 + operand2)
                case '-':
                    stack.append(operand2 - operand1)
                case '/':
                    stack.append(operand2 / operand1)
                case '*':
                    stack.append(operand1 * operand2)
            # }

        # }

    # }
    
    return stack[0]
# }

print(evaluate_postfix_inverse("2 3 -"))  # Expected output: 1
print(evaluate_postfix_inverse("2 3 +"))  # Expected output: 5
print(evaluate_postfix_inverse("6 3 *"))  # Expected output: 18

'''

***** BONEYARD *****

# define the function blocks
def zero():
    print "You typed zero.\n"

def sqr():
    print "n is a perfect square\n"

def even():
    print "n is an even number\n"

def prime():
    print "n is a prime number\n"

# map the inputs to the function blocks
options = {0 : zero,
           1 : sqr,
           4 : sqr,
           9 : sqr,
           2 : even,
           3 : prime,
           5 : prime,
           7 : prime,
}

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"

        # If an exact match is not confirmed, this last case will be used if provided
        case _:
            return "Something's wrong with the internet"

    match element:
        case '+':
        case '-':
        case '/':
        case '*':

if (element == '+') : 
            # {
                stack.append(operand1 + operand2)
            # }

            elif element == '-' : 
            # {
                stack.append(operand2 - operand1)
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

result = {
  'a': lambda x: x * 5,
  'b': lambda x: x + 7,
  'c': lambda x: x - 2
}[value](x)            

'''