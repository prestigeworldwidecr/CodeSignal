'''

Alright, Space Explorer, let's have a little fun with data analysis! You have a list of daily temperatures recorded in ascending order of days, right? In degrees Celsius, if you please. No, not Martian days, Earth days! Your job is, for each day, to find out how many days you'll have to wait until the next cooler day. Is it tomorrow? Or three days later? Or maybe there's no cooler day in sight and that calls for a -1.

Just bear in mind the input list of temperatures isn't picky, it could be empty, only contain one record, or have several days with the same temperature. And how are we presenting the results? A list! For each day, indicate the wait time until the next cooler day, or a -1 if the future's looking too hot to handle! Let's see what you can do, Stellar Navigator!

No worries, let's work through this together! It looks like you're using a nested loop to find the next cooler day, which results in an inefficient O(n^2) solution. Let's refocus on using a stack to achieve an O(n) solution.

Here's a step-by-step guide to help you:

Initialize the Stack: Use the stack to store indices of temperatures. This will help you track which days are still waiting for a cooler day.

Iterate Backwards: Start from the last day and move towards the first. This way, you can determine the next cooler day for each day as you go.

Use the Stack: For each day:

While the stack is not empty and the current day's temperature is less than or equal to the temperature at the index stored at the top of the stack, pop the stack. This means the current day is cooler than the days stored in the stack.

If the stack is not empty after popping, the top of the stack will give you the index of the next cooler day. Calculate the difference in days and store it in the result.
Push the current day's index onto the stack.

Return the Result: After processing all days, your result list will contain the number of days until the next cooler day for each day.

'''

def days_until_cooler(temps) :
# {
    result = [-1] * len(temps)
    stack = []

    for i in range(len(temps) - 1, -1, -1) :
    # {

        while (stack and temps[i] <= temps[stack[-1]]) :
        # {
            stack.pop()
        # }

        if (stack) :
        # {
            result[i] = stack[-1] - i
        # }

        else :
        # {
            None
        # }

        stack.append(i)
    # }

    return result

# }

print(days_until_cooler([30, 60, 90, 120, 60, 30]))  # Expected: [-1, 4, 2, 1, 1, -1]
print(days_until_cooler([100, 95, 90, 85, 80, 75]))  # Expected: [1, 1, 1, 1, 1, -1]
print(days_until_cooler([1]))  # Expected: [-1]

'''

***** BONEYARD *****

 # result.append(-1)
            
            # print(temps[i]), "!!", temps[stack[-1]]
            # result.append(stack[-1])

# for i in range(len(temps)) :
    for _ in temps[: : -1] :
    # {
        print('!', _)
    # }

if (temps[i] < mininum) :
        # {
            mininum = temps[i]
        # }

        else :
        # {
            for j in range(i + 1, len(temps)) :
            # {
                if (temps[j] < temps[i]) :
                # {
                    result[i] = j - i
                # }

                else :
                # {
                    None
                # }
            # }

        # }

    # }
    
    return result

import sys
# mininum = sys.maxsize

# print('!', stack)

# for i in range(len(temps) - 1, -1, -1) : *** utterly confusing ***

        # print(i, temps[i])
        # stack.append(temps[i])
        # stack.push(temps[i])

# print(len(temps))

# stack.append(i)
            while (stack and temps[i] > temps[stack[-1]]) :
            # {
                # print('!', stack[-1])
                result[stack[-1]] = i - stack[-1]
                stack.pop()
            # }

'''