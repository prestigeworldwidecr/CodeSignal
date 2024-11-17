'''

Welcome to your very first hands-on experience with Binary Search! Excited? You certainly should be!

Imagine that you're working on an e-commerce platform, and there's a customer looking for a product at a specific price. This customer needs to know if such a product exists on the platform.

To assist this customer, we will implement Binary Search on a sorted list of product prices.

Click 'Run' to see it in action!

'''

# Implementation of Binary Search on a specific use case

# List of sorted products' prices in an e-commerce company
products_price = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

def binary_search_iterative(data, target) :
# {
    low = 0
    high = len(data)

    while high - low > 1 :
    # {
        mid = (low + high) // 2

        if (target < data[mid]) :
        # {
            high = mid 
        # }

        elif (target > data[mid]) :
        # {
            low = mid 
        # }

        # if target is equal to data[mid]
        else :
        # {
            return mid
        # }

    # }

    # return low if data[low] == target else None
    if (data[low] == target) :
    # {
        return low
    # }

    else :
    # {
        return None
    # }

# }

def search_price(customer_query) :
# {
    result = binary_search_iterative(products_price, customer_query)

    if (result is not None) :
    # {
        print("Product of price", customer_query, "is found at position ", result, " in the price list.")
    # }

    else :
    # {
        print("No product is found with price", customer_query, ".")
    # }

# }

# Searching for a price that exists
search_price(30)

# Searching for a price that doesn't exist
search_price(31)

'''

********
BONEYARD
********

'''