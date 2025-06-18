'''

Welcome to the first practical exercise on abstract classes in clean code!

In this task, you’ll refine your skills by implementing an abstract class that promotes flexibility and interchangeability. The starter code contains two classes with similar payment functionalities but lacks the flexibility to easily extend or modify payment types.

You are required to refactor this code by defining a Payment abstract class with an abstract pay method and refactoring the existing classes to inherit from this abstract class.

Additionally, implement a process_payment function that takes a Payment object and calls its pay method. By doing so, you will establish a standardized approach to process different types of payments, making the codebase more flexible and easier to extend in the future!

Good effort, but you missed a key requirement: both CashPayment and CreditCardPayment need to inherit from your abstract base class. Also, the pay method should not take any parameters.

Want to give it another shot, or would you like a hint?

Good effort, but your process_payment function is calling pay with an argument, while your pay methods don't take any parameters. Try adjusting that and see if it works!

'''

from abc import ABC, abstractmethod

class PaymentProcesser(ABC) :
# {
    @abstractmethod
    def pay(self) :
    # {
        None
    # }

# }

class CashPayment(PaymentProcesser) :
# {
    def pay(self):
    # {
        print("Paying with cash")
    # }

# }

class CreditCardPayment(PaymentProcesser) :
# { 
    def pay(self) :
    # {
        print("Paying with credit card")
    # }

# }

def process_payment(payment_method):
# {
    payment_method.pay()
# }

def main() :
# {
    # cash_payment = CashPayment()
    # credit_card_payment = CreditCardPayment()

    # cash_payment.pay()
    # credit_card_payment.pay()
    process_payment(CashPayment())
    process_payment(CreditCardPayment())

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