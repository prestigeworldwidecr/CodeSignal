'''

Pay attention code explorer, here's a task for your coding journey. Your interstellar communication system has a glitch. It inverts your messages and adds some noisy meaningless text in the beginning.

Your mission is clear: you need to build a function named string_end that receives a string and a positive integer n. The function's job will be to flip the entire string and then reveal only the first n characters. Take the string "DataStructures" as an example. If n equals 5, the output should be "serut". Use the reliable Stack data structure to your advantage in this task.

'''

def string_end(strng, n) :
# {
    stack = list(strng)
    result = ""
   
    # implement this
    for i in range(n) :
    # {
        result = result + stack.pop()
    # }

    return result
# }

print(string_end("ijkshgegassem tnatropmi", 17))  # Expected output: important message
print(string_end("ffsfatad", 4))  # Expected output: data
print(string_end("IA", 2))  # Expected output: AI


'''

***** BONEYARD *****

'''