'''

Great job on your progress so far! Now, let's take it a step further. You've mastered managing a grocery shop inventory. Your next challenge is to determine how each item's stock level compares to the average stock level in the store. Write some code to calculate the difference between each item's count and the average, and print out whether each item has more, less, or exactly the average amount of stock.

'''

# Creating a simple inventory containing a count of items in a grocery shop
inventory = {
                "milk": 24,
                "bread": 36,
                "eggs": 48
            }

# TODO: Calculate the average count of the inventory items
average_count = sum(inventory.values()) / len(inventory)
# average_count = 0
status_message = ""

# Finding how much each item's count differs from the average
for item, count in inventory.items() :
# {
    difference_from_average = count - average_count

    # TODO: Check if the count is greater, less, or equal to the average and set the appropriate message
    if (count > average_count) :
    # {
        status_message = "a count greater than the average."
    # }

    elif (count < average_count) :
    # {
        status_message = "a count less than the average."
    # }

    elif (count == average_count) :
    # {
        status_message = "a count equal to the average."
    # }

    else :
    # {
        None
    # }

    print(item.capitalize(), "has", status_message)

# }

'''

'''