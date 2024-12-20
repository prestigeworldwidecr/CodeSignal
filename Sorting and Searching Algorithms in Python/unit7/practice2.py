'''

Here's your next task, Space Voyager! Vendors from different galaxies are storming your online store, and sales are shooting up like fireworks. Each sale is represented as an integer in a list, with each integer representing units sold for a particular item.

Your job is to spring into action and sort this list in descending order.

Now, it's time to buckle up and start coding!

'''

def sort_sales(sales) :
# {
    # implement this
    return(sorted(sales, reverse = True))
# }

print(sort_sales([10, 15, 4, 20, 1])) # Expected: [20, 15, 10, 4, 1]
print(sort_sales([30, 25, 20, 15])) # Expected: [30, 25, 20, 15]
print(sort_sales([3, 8, 5])) # Expected: [8, 5, 3]

'''

**********  BONEYARD  **********

'''