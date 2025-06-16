'''

Welcome to the final task of this unit! 🎉 In this exercise, we will focus on cleaning up a constructor by applying the Builder Pattern. Our goal is to simplify the creation of an Order object, which currently requires a large number of parameters in its constructor, not all of which are mandatory. Specifically, the parameters productName and price are mandatory, while quantity, deliveryAddress, and note are optional. Your task is to refactor the code to utilize the Builder Pattern, enabling more flexible and readable object creation.

Let's enhance the initialization of our Order class by making it more user-friendly through the Builder Pattern!

Reminder: The Builder Pattern helps construct complex objects step-by-step, allowing for mandatory and optional parameters. For instance:

'''

class Car :
# {
    def __init__(self, builder) :
    # {
        self.make = builder.make
        self.model = builder.model
        self.color = builder.color
    # }

    class Builder :
    # {
        def __init__(self, make, model) :
        # {
            self.make = make
            self.model = model
            self.color = None
        # }

        def set_color(self, color) :
        # {
            self.color = color
            return self
        # }

        def build(self) :
        # {
            return Car(self)
        # }

    # }

# }

car = Car.Builder("Toyota", "Corolla").set_color("Blue").build()

class Order :
# {
    def __init__(self, builder) :
    # {
        self.product_name = builder.product_name
        self.price = builder.price
        self.quantity = builder.quantity
        self.delivery_address = builder.delivery_address
        self.note = builder.note
    # }

    class Builder :
    # {
        def __init__(self, product_name, price, quantity, delivery_address) :
        # {
            self.product_name = product_name
            self.price = price
            self.quantity = quantity
            self.delivery_address = delivery_address
            self.note = ""
        # }

        def add_note(self, note) :
        # {
            self.note = note
            return self
        # }
        
        def build(self) :
        # {
            return Order(self)
        # }
        
    # }

# }

def main() :
# {
    # order = Order("Laptop", 999.99, 2, "123 Main St, Anytown", None)
    # print(order)
    order = (Order.Builder("Laptop", 999.99, 2, "123 Main St, Anytown")
    .add_note("None")
    .build())

    print("Product Name:", order.product_name)
    print("Price:", order.price)
    print("Quantity:", order.quantity)
    print("Delivery Address:", order.delivery_address)
    print("Note:", order.note)
# }

if __name__ == "__main__" :
# {
    main()
# }

else :
# {
    None
# }

'''

***** BONEYARD *****

def __str__(self) :
    # {
        s = "Order [product_name:" + self.product_name + "price:" + str(self.price) + "quantity:" + str(self.quantity) + "delivery_address:" + self.delivery_address + "note:" + self.note + ']'
        
        print(type(s))
        # s = tuple(s)
        
        s = ' '.join(s)

        print(s)
        
        return s
    # }

'''