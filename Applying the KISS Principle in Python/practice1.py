'''

Welcome to the first practical task on applying the KISS (Keep It Simple, Stupid) principle! In this task, we’ll focus on improving the simplicity and readability of the current code. The code calculates the total cost of an order, but it contains some unnecessary complexity that can be removed. Your task is to refactor the code to make it more straightforward and maintainable without altering its functionality. Keep in mind the strategies you learned about applying the KISS principle during your lesson.

The goal is to reduce complexity and increase clarity in the code. Let’s make it simple and easy to read!

To help you understand the financial terms used in the task, here's a quick glossary:

Total Price (Gross Amount): This is the initial amount before any discounts or taxes are applied, calculated as the product of the item price and the quantity.

Discount: A reduction in the total price, calculated by multiplying the total price by the discount rate.
Price After Discount (Net Amount): The amount after the discount has been subtracted from the total price.

Tax Amount: The amount of tax added to the net amount, calculated by multiplying the net amount by the tax rate.

Final Price: The total cost of the order after applying the discount and adding the tax amount.

Good effort, but your formula isn't quite right—it's not calculating the final price as intended.

Try breaking the calculation into clear steps: subtract the discount first, then apply the tax. Want a hint on how to structure it?

Great! Here’s a small hint:

First, calculate the total price before any discounts or taxes.
Next, subtract the discount from that total.
Finally, apply the tax to the discounted amount.
How might you write that in code, step by step?

'''

def total_price(item_price, quantity) :
# {
    return item_price * quantity
# }
    
def discount(total_price, discount_rate) :
# {
    return total_price * discount_rate
# }

def tax_amount(price_after_discount, tax_rate) :
# {
    # price_after_discount = total_price - discount
    return price_after_discount * tax_rate

# }

def calculate_total(item_price, quantity, discount_rate, tax_rate) :
# {
    # return (item_price * quantity) - (item_price * quantity * discount_rate) * (1 + tax_rate)
    tp = total_price(item_price, quantity)
    d = discount(tp, discount_rate)
    ta = tax_amount(tp - d, tax_rate)

    return tp - d + ta
# }

def main() :
# {
    item_price = 12.50
    quantity = 4
    discount_rate = 0.10
    tax_rate = 0.08
    
    print("Total Cost:", calculate_total(item_price, quantity, discount_rate, tax_rate))
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

def final_price(price_after_discount, tax_amount) :
# {
    return price_after_discount + tax_amount
# }

# total_price = item_price * quantity
    # discount = total_price * discount_rate
    # price_after_discount = total_price - discount
    # tax_amount = price_after_discount * tax_rate
    # final_price = price_after_discount + tax_amount

    
    # total_cost = calculate_total(item_price, quantity, discount_rate, tax_rate)

'''