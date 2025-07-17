'''

Welcome to the final task of this unit! Let's put everything together by focusing on the Replace Temp with Query refactoring technique. In this exercise, you'll refine code related to customer eligibility checks for a promotion. The existing code contains temporary variables that are repetitive and can lead to maintenance issues. Your task is to replace these temporary variables with query methods, ensuring the logic is clean, efficient, and maintainable.

This change will encapsulate certain checks into reusable methods, reduce repetition, and enhance code readability.

'''

from datetime import datetime, timedelta

class Customer :
# {    
    def __init__(self, sign_up_date, purchase_history, loyalty_level) :
    # {
        self.sign_up_date = sign_up_date
        self.purchase_history = purchase_history
        self.loyalty_level = loyalty_level
    # }

    def get_sign_up_date(self) :
    # {
        return self.sign_up_date
    # }

    def get_purchase_history(self) :
    # {
        return self.purchase_history
    # }

    def get_loyalty_level(self) :
    # {
        return self.loyalty_level
    # }

# }

def is_customer_new(customer_sign_up_date) :
# {
    if ((datetime.now() - timedelta(days = 90)) < customer_sign_up_date) :
    # {
        return True
    # }

    else :
    # {
        return False
    # }
# }

def is_eligible_for_discount(customer) :
# {
    if (is_customer_new(customer.get_sign_up_date()) and len(customer.get_purchase_history()) > 5) :
    # {
        return True
    # }
    
    else :
    # {
        return False
    # }

# }

def is_eligible_for_loyalty_program(customer) :
# {

    if ((is_customer_new(customer.get_sign_up_date()) and customer.get_loyalty_level()) > 3) :
    # {
        return True
    # }
    
    else :
    # {
        return False
    # }

# }


def main() :
# {
    customer = Customer(
                        datetime.now() - timedelta(days = 30),
                        [10, 20, 30, 40, 50, 60],
                        4
                        )
    
    print("Eligible for discount:", is_eligible_for_discount(customer))
    print("Eligible for loyalty program:", is_eligible_for_loyalty_program(customer))
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

# new_customer = customer.get_sign_up_date() > datetime.now() - timedelta(days = 90)
    # print('!', new_customer, timedelta(days = 90))
    # return new_customer and len(customer.get_purchase_history()) > 5



    new_customer = customer.get_sign_up_date() > datetime.now() - timedelta(days = 90)

    return new_customer or customer.get_loyalty_level() > 3    

    # print(customer.get_purchase_history(), len(customer.get_purchase_history()))
    
    
    

'''