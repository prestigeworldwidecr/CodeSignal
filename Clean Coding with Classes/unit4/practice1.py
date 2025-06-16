'''

Welcome to the first practical exercise on implementing inheritance wisely! In this task, we'll focus on reducing redundancy by promoting code reuse through inheritance. You'll be given three independent classes from a simple banking application, all of which have duplicated functionality. Your task is to identify these redundancies and refactor the code by extracting common functionality into a parent class. This will make the code more organized, maintainable, and easier to extend.

The initial classes handle common banking actions, but the code is repetitive. Let's streamline the structure using inheritance!

'''

class BankAccount :
# {
    def deposit(self, amount) :
    # {
        if (amount > 0) :
        # {
            self.balance = self.balance + amount
            # print("Deposited:", amount, "New balance:", self.balance)
            print("Balance increase:", amount, "New balance:", self.balance)
        # }

        else :
        # {
            print("Deposit failed. Amount must be positive.")
            # None
        # }

    # }

    def withdraw(self, amount) :
    # {
        if (amount > 0 and self.balance >= amount) :
        # {
            self.balance = self.balance - amount
            print("Balance decrease:", amount, "New balance:", self.balance)
        # }

        else :
        # {
            print("Withdrawal failed. Insufficient balance.")
            # None
        # }

    # }

# }

class CheckingAccount(BankAccount) :
# {
    def __init__(self, balance) :
    # {
        self.balance = balance
    # }

# }

class SavingsAccount(BankAccount) :
# {
    def __init__(self, balance) :
    # {
        self.balance = balance
    # }

# }

class LoanAccount(BankAccount) :
# {
    def __init__(self, balance) :
    # {
        self.balance = balance
    # }

# }

def main() :
# {
    checking_account = CheckingAccount(0)
    checking_account.deposit(100)
    checking_account.withdraw(50)

    savings_account = SavingsAccount(0)
    savings_account.deposit(200)
    # savings_account.add_interest()

    loan_account = LoanAccount(0)
    loan_account.withdraw(300)
    loan_account.deposit(100)
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

def __init__(self) :
    # {
        self.balance = 0
    # }

    def deposit(self, amount) :
    # {
        if (amount > 0) :
        # {
            self.balance = self.balance + amount
            print("Deposited:", amount, "New balance:", self.balance)
        # }

        else :
        # {
            print("Deposit failed. Amount must be positive.")
        # }

    # }

    def withdraw(self, amount) :
    # {
        if (amount > 0 and self.balance >= amount) :
        # {
            self.balance = self.balance - amount
            print("Withdrawn:", amount, "New balance:", self.balance)
        # }

        else :
        # {
            print("Withdrawal failed. Insufficient balance.")
        # }

    # }

def __init__(self) :
    # {
        self.balance = 0
    # }

    def deposit(self, amount) :
    # {
        if (amount > 0) :
        # {
            self.balance = self.balance + amount
            print("Deposited:", amount, "New balance:", self.balance)
        # }

        else :
        # {
            print("Deposit failed. Amount must be positive.")
        # }

    # }

    def add_interest(self) :
    # {
        interest = self.balance * 0.05  # 5% interest
        self.balance = self.balance + interest
        print("Interest added, New Balance:", self.balance)
    # }

def __init__(self) :
    # {
        self.balance = 0
    # }

    def withdraw(self, amount) :
    # {
        if (amount > 0 and self.balance >= amount) :
        # {
            self.balance = self.balance - amount
            print("Withdrawn:", amount, "New balance:", self.balance)
        # }

        else :
        # {
            print("Withdrawal failed. Insufficient balance.")
        # }

    # }

    def repay_loan(self, amount) :
    # {
        if (amount > 0) :
        # {
            self.balance = self.balance + amount
            print("Loan repayment, New Balance:", self.balance)
        # }

        else :
        # {
            print("Repayment failed. Amount must be positive.")
        # }

    # }

'''