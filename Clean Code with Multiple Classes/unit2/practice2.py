'''

In our next exercise we're aiming to streamline our payment processing system. Currently, we have a StoreTransaction class that directly interacts with specific payment types. This setup is inflexible and makes it challenging to introduce new payment methods. Your task is to refactor the code to create a PaymentType abstract class, which will decouple the transaction processing logic from the payment methods. Doing so will enable our transaction processing to work with any payment type that implements this class, paving the way for future scalability and easier maintenance.

'''

from abc import ABC, abstractmethod

class PaymentType(ABC) :
# {
    @abstractmethod
    def process(self) :
    # {
        None
    # }
# }

class Cash(PaymentType) :
# {
    def process(self) :
    # {
        print("Processing cash payment")
    # }

# }

class CreditCard(PaymentType) :
# {
    def process(self) :
    # {
        print("Processing credit card payment")
    # }
        
# }

class StoreTransaction :
# {
    def perform_transaction_with_cash(self, cash) :
    # {
        cash.process()
    # }

    def perform_transaction_with_card(self, card) :
    # {
        card.process()
    # }

# }

def main() :

    # cash_payment = Cash()
    # card_payment = CreditCard()

    transaction = StoreTransaction()
    transaction.perform_transaction_with_cash(Cash())
    transaction.perform_transaction_with_card(CreditCard())


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

# print("Processing cash payment")
        # print("Processing payment")
        # print("Processing credit card payment")

'''