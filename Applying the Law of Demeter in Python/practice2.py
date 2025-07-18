'''

Welcome to the second and final task of this unit! The current code is a simple example of a food delivery service system, where a DeliveryService processes an order for a Customer. However, the way classes interact violates the Law of Demeter by exposing too many details between objects. Your job is to refactor the code to ensure that each class only interacts with objects it directly knows about. Let's streamline this code to be cleaner and adhere to proper encapsulation principles

'''

class Customer :
# {
    def __init__(self, name) :
    # {
        self._name = name
    # }

    def get_name(self) :
    # {
        return self._name
    # }

# }

class Order :
# {
    def __init__(self, item, quantity) :
    # {
        self.item = item
        self.quantity = quantity
    # }

# }

class DeliveryService :
# {
    def process_order(self, customer, item, quantity) :
    # {
        order = Order(item, quantity)
        print(customer.get_name(), "received order:", quantity, 'x', order.item)
    # }

# }

def main() :
# {
    customer = Customer("Alice")
    delivery_service = DeliveryService()
    delivery_service.process_order(customer, "Pizza", 2)
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