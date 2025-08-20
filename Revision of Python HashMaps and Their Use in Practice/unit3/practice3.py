'''

Great job with the inventory management! Next, you will refine the grocery shop's inventory system by calculating and displaying some crucial statistics. Given the data in the inventory, write the code to calculate the total number of items and identify the maximum quantity of a single fruit type in the inventory.

'''
# Inventory dictionary for a grocery shop
inventory = {"apples": 30, "bananas": 45, "oranges": 25, "pears": 10}

# TODO: Calculate the total items in the inventory and print it
total_items = sum(inventory.values())
print(total_items)

# TODO: Find the maximum quantity of a single fruit type in the inventory and print it
max_quantity = max(inventory.values())
print(max_quantity)

'''

***** BONEYARD *****

'''