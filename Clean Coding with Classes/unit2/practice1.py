'''

Welcome to the first practical exercise on encapsulation and access modifiers! In this task, you'll refactor a BankAccount class to enhance its encapsulation by securing access to its fields. The current version of the class exposes its fields directly to the users, allowing them to modify the balance in ways that may lead to unwanted behavior, such as setting a negative balance. Your goal is to modify the class to ensure that the balance is protected, and that only valid operations can modify it.

To accomplish this, you'll need to:

Make the balance field private to prevent direct access.

Ensure that the initial balance provided during the account creation is non-negative. If a negative initial balance is provided, raise an error to prevent the creation of an account with an invalid state.

Implement a property method to allow controlled access to the balance in a read-only manner, ensuring that the balance can be accessed but not modified directly.

Refactor the deposit method to ensure that only positive amounts can be deposited. Add a check to raise an error if the deposit amount is negative or zero.

Refactor the withdraw method to ensure that the amount withdrawn is positive and that the balance is sufficient for the withdrawal. If not, raise an error for insufficient funds.

By making these changes, you will improve the integrity and security of the BankAccount class while ensuring that only valid operations can affect the balance.

'''

class BankAccount :
# {
    def __init__(self, initial_balance) :
    # {
        if (initial_balance < 0) :
        # {
            raise ValueError("Balance cannot be less than $0") 
        # }

        else :
        # {
            self._balance = initial_balance
            print("Initial Balance:", self._balance)
        # }

    # }

    @property
    def balance(self) :
    # {
        return self._balance
    # }

    def deposit(self, amount) :
    # {
        if (amount > 0) :
        # {
            self._balance = self._balance + amount
            print("After Deposit:", self._balance)
        # }

        else :
        # {
            raise ValueError("Deposit cannot be less than $0")
        # }

    # }

    def withdraw(self, amount) :
    # {
        if (0 < amount and amount <= self._balance) :
        # {
            self._balance = self._balance - amount
            print("After Withdrawal:", self._balance)
        # }

        else :
        # {
            raise ValueError("Balance cannot be less than $0")
        # }

    # }    


# }

def main() :
# {
    account = BankAccount(500.00)
    account.deposit(150.00)
    account.withdraw(100.00)
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


            # self.balance -= amount
            # self.balance += amount

    def deposit(self, amount) :
    # {
        if (amount > 0) :
        # {
            # self.balance += amount
            self.balance = self.balance + amount
        # }

        else :
        # {
            None
        # }

    # }

    def withdraw(self, amount) :
    # {
        if (0 < amount and amount <= self.balance) :
        # {
            # self.balance -= amount
            self.balance = self.balance - amount
        # }

        else :
        # {
            None
        # }

    # }

    @balance.withdraw
    def balance() :
    # {

    # }

    @balance.deposit

    print("Initial Balance:", account.balance)

    account.deposit(150.00)
    print("After Deposit:", account.balance)

    account.withdraw(100.00)
    print("After Withdrawal:", account.balance)

'''