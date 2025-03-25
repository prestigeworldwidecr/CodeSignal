'''

Welcome to the first task of our lesson on comments and documentation!

In this exercise, we'll focus on cleaning up unnecessary comments and noise in the code. The current code is cluttered with redundant comments that don't add value and simply restate what the code does. Your challenge is to remove these comments and ensure the code is more concise and readable.

The code is a simple program that computes the total price of items in a cart by multiplying the price and quantity. Let's strive for clarity and tidiness!

'''

def calculate_total_price(price, quantity) :
# {
    return price * quantity
# }

def main() :
# {
    item_price = 15.99
    item_count = 4
    total_price = calculate_total_price(item_price, item_count)

    print("Total Price:", total_price)
# }

if (__name__ == "__main__") :
# {
    main()
# }

else :
# {
    None
# }

'''

***** BONEYARD *****

'''