'''

Welcome to the next step in mastering SOLID principles! In this task, our focus shifts to the Open/Closed Principle, which emphasizes structuring your code so it's easy to add new features without disrupting existing functionality. The given code calculates the pricing for different types of products but lacks flexibility for future expansions. We need to refactor it to allow new product types to be introduced easily while maintaining existing logic.

Your task is to redesign the code structure so that it aligns with the Open/Closed Principle. This involves making it easy to add new product types without affecting the current codebase

Good effort, but your solution still requires changing the calculator when adding new product types, which doesn't follow the Open/Closed Principle.

Try making each product type responsible for its own price calculation, so you don't need to update the calculator for new types. Want a hint?

Nice work so far! Your code is a step forward, but notice that ProductCalculator still needs to be changed every time you add a new product type. That means it’s not fully following the Open/Closed Principle yet.

Can you think of a way to let each product type handle its own price calculation, so you never have to update ProductCalculator when adding new products?

Maybe try using subclasses for each product type, each with its own calculate_price method.
What would that look like

'''

class Product :
# {
    def __init__(self) :
    # {
        None
    # 

    def calculate_price(self) :
    # {
        return self.calculate_price()
    # }

# }

class Book(Product) :
# {
    def __init__(self, base_price) :
    # {
        self.base_price = base_price
    # }

    def calculate_price(self) :
    # {
        return self.base_price
    # }

# }

class Food(Product) :
# {
    def __init__(self, base_price) :
    # {
        self.base_price = base_price
    # }

    def calculate_price(self) :
    # {
        return self.base_price * 1.07
    # }

# }

class ProductCalculator :
# {
    def calculate(self, product) :
    # {
        return product.calculate_price()
    # }

# }

def main_program() :
# {
    calculator = ProductCalculator()
    book = Book(29.99)
    food = Food(0.99)
    
    print("Price of Book: $", calculator.calculate(book))
    print("Price of Food: $", calculator.calculate(food))
# }

if (__name__ == "__main__") :
# {    
    main_program()
# }

else:
# {
    None
# }

'''

***** BONEYARD *****

def calculate(self, product):
    # {
        match product.get_type() :
        # {
            case "book" :
            # {
                return product.get_base_price()
            # }

            case "food" :
            # {
                return product.get_base_price() * 1.07
            # }        

            case _:
            # {
                return product.get_base_price()
            # }
             
        # }    

    # }

# return self.base_price
# def get_price(self) :
    # {       

def calculate_book_price(self, base_price):
    # {
        # No discount or special pricing for books
        return base_price
    # }

    def calculate_food_price(self, base_price):
    # {
        # Applying tax for food products
        return base_price + base_price * 0.07
    # }    

# book_price = calculator.calculate("Book", 29.99)
    # food_price = calculator.calculate("Food", 0.99)   
    # 
    # 
        if product.get_type() == "Book" :
        # {
            return self.base_price
        # }

        elif product.get_type() == "Food" :
        # {
            return self.base_price * 1.07
        # }

        else :
        # {
            return self.base_price
        # } 

        def __init__(self, type_, base_price) :
    # {
        self.type_ = type_
        self.base_price = base_price
    # }

    def get_type(self) :
    # {
        return self.type_
    # }

    def get_base_price(self) :
    # {
        return self.base_price
    # }    

'''