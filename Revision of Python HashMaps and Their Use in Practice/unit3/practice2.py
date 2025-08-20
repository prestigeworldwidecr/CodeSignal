'''

In this exercise, you have a small program intended to calculate and display the minimum quantity of a single type of fruit in a grocery shop's inventory. However, there's a bug preventing it from working correctly. Your task is to find and fix the bug without adding or removing any lines of code.

'''

# A dictionary simulating the inventory of a grocery shop
inventory = {"apples" : 30,
             "bananas" : 45,
             "cherries" : 25
             }

# Calculate the minimum quantity of a single fruit type in the inventory
min_quantity = min(inventory.values())

print("The minimum quantity of a single type of fruit in the inventory is:", min_quantity)

'''

***** BONEYARD *****

'''