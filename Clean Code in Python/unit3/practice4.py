'''

Welcome to the final task of this unit! In this task, we will focus on applying the Don't Repeat Yourself (DRY) principle. The provided code contains duplicate logic that processes customer orders. Your task is to extract the common functionalities into a separate function, thereby reducing repetition and improving the maintainability of the code. This approach will showcase the effectiveness of the DRY principle while keeping functionality intact.

The code manages the placement and cancellation of customer orders, but key operations are repeated in both processes. Let’s extract those common elements into a universal function to streamline our code!


'''

class Order :
# {
    def __init__(self, order_id, status) :
    # {
        self._id = order_id
        self._status = status
    # }

    def get_id(self) :
    # {
        return self._id
    # }
    
    def set_status(self, status) :
    # {
        self._status = status
    # }

    def get_status(self) :
    # {
        return self._status
    # }

# }

def main() :
# {
    order = Order("12345", "Pending")

    place_order(order)
    print_order_status(order)

    cancel_order(order)
    print_order_status(order)
# }

def print_order_status(order) :
# {
    print("Order ID:", order.get_id())
    print("Status:", order.get_status())
# }

def place_order(order) :
# {
    order.set_status("Completed")
# }

def cancel_order(order) :
# {
    order.set_status("Cancelled")
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

# print("Order status after placing:", order.get_status())
    # print("Order status after cancellation:", order.get_status())

    print("Order ID:", order.get_id())
    print("Status:", order.get_status())
    print("Action: placing order")
    print("Order ID:", order.get_id())
    print("Status:", order.get_status())
    print("Action: canceling order")

    print("Order ID:", order.get_id())
    print("Status:", order.get_status())
    print("Action: placing order")
    print("Order ID:", order.get_id())
    print("Status:", order.get_status())
    print("Action: canceling order")

'''