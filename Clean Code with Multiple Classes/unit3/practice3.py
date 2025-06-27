'''

In this exercise, you'll leverage the Factory Pattern to refactor an existing Python program. Currently, the FruitStore class creates and manages different types of fruits, but it's tightly coupled to specific fruit implementations, such as Apple and Banana. By introducing the Factory Pattern, you'll decouple the FruitStore from specific fruit classes, making your code more scalable and easier to maintain. Let's get started!

'''

from abc import ABC, abstractmethod

class Fruit(ABC) :
# {
    @abstractmethod
    def get_description(self) :
    # {
        None
    # }

# }

class Apple(Fruit) :
# {
    def get_description(self) :
    # {
        return "This is an apple."
    # }

# }

class Banana(Fruit) :
# {
    def get_description(self) :
    # {
        return "This is a banana."
    # }

# }

class FruitFactory :
# {
    @staticmethod
    def order_fruit(fruit_type: str) -> Fruit :
    # {
        if (fruit_type == "apple") :
        # {
            return Apple()
        # }

        elif (fruit_type == "banana") :
        # {
            return Banana()
        # }

        else :
        # {
            raise ValueError("Unknown fruit type")
        # }

    # }

# }


class FruitStore :
# {
    def __init__(self, fruit_type: str) :
    # {
        self.fruit_factory = FruitFactory.order_fruit(fruit_type)
    # }

    def order_fruit(self) :
    # {
        return self.fruit_factory.order_fruit()
    # }

# }

def main() :
# {
    apple = FruitStore("apple")
    banana = FruitStore("banana")
    apple = FruitFactory.order_fruit("apple")
    banana = FruitFactory.order_fruit("banana")
    # apple = Fruit()
    # banana = Fruit()
    print(apple.get_description())
    print(banana.get_description())
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

# apple = fruit_store.order_fruit("apple")
    # banana = fruit_store.order_fruit("banana")
    # apple = fruit_store.order_fruit(fruit_store, "apple")
    # banana = fruit_store.order_fruit(Banana())
    print(apple.order_fruit())
    print(banana.order_fruit())
    # print(apple.get_description())

    # 
    # print(banana.get_description())

# return self.order_fruit(self, "apple")
            # return Apple().order_fruit()
            # return "apple"
            
            # return self.order_fruit(self, "banana")
            # return "banana"
            

    def order_apple(self) :
    # {
        return Apple()  # Direct dependency
    # }

    def order_banana(self) :
    # {
        return Banana()  # Direct dependency
    # }

'''