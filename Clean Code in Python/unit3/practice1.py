'''

Welcome to the first task focusing on clean functions! Let's concentrate on reducing the size of a method. The current code includes a method that performs multiple tasks, making it difficult to read and maintain. Your mission is to refactor this method into smaller, focused methods that each do just one thing. This approach will greatly enhance code readability and maintainability.

The code currently processes a list of numbers to compute both the sum and the average, but all operations are cramped into a single method. Let’s break these down into more manageable chunks!

'''

def find_sum(numbers) :
# {
    total = 0

    for number in numbers :
    # {
        total = total + number
    # }

    return total
# }

def find_average(numbers) :
# {
    total = find_sum(numbers)
    average = total / len(numbers)

    return average
# }

def main() :
# {
    numbers = [1, 2, 3, 4, 5]
    # process_numbers(numbers)
    print("Sum:", find_sum(numbers))
    print("Average:", find_average(numbers))
# }

if __name__ == "__main__" :
# {
    main()
# }

else :
# {
    None
# }

'''

***** BONEYARD *****

def process_numbers(numbers) :
# {
    total = 0

    for number in numbers :
    # {
        total = total + number
    # }

    average = total / len(numbers)

    print("Sum:", total)
    print("Average:", average)
# }

'''