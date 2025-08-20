'''

In your grocery shop inventory, you've successfully calculated the maximum quantity of items. Let's now apply a new skill: change the code to calculate the average quantity of items in the inventory. Utilize the sum and len functions to find your answer. Ready to give it a try?

'''
# import math

# A dictionary simulating a grocery shop inventory where key is the item and value is its quantity
inventory = {"potatoes": 30, "carrots": 25, "onions": 15}

# Finding the maximum quantity among the inventory
avg = sum(inventory.values()) / len(inventory)
print("The average quantity of any item in the shop is:", avg)

'''

***** BONEYARD *****

'''