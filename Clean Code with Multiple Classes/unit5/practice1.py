'''

Welcome to the first task of our lesson on handling exceptions across classes! In this exercise, you will apply the principles of exception handling discussed in the lesson to refactor a simple banking application. Your goal is to enhance the codebase to preserve exception context and provide meaningful error messages while maintaining clean separation between logic and error handling.

The Current Problems

The current implementation has several issues with exception propagation:

It uses generic exceptions, leading to a lack of clarity.
Context is lost when re-throwing exceptions.
Error messages are not specific enough for effective debugging.
Refactor the code to implement robust exception handling.

Requirements

Introduce the following custom exceptions:

AccountException: This is a base exception class for all account-related errors. It should include a message for error details and an optional cause attribute to support exception chaining, preserving the context of why an error occurred.

AccountNotFoundException: Raised when an account does not exist. Inherits from AccountException and captures the account_id using an attribute self.account_id = account_id to indicate which account caused the error.

InsufficientFundsException: Raised when there are insufficient funds in an account. Inherits from AccountException and similarly captures the account_id.

TransferFailedException: A high-level exception for transfer-related failures that captures the underlying cause, allowing access to both the high-level failure reason and the specific lower-level cause.
Propagate exceptions across classes without losing the original context. Use the raise ... from ... syntax for chaining exceptions.

Ensure all error messages are clear, concise, and informative. Provide enough context for effective debugging.

Maintain a clean separation between business logic and error-handling code.

'''

from random import random

class AccountException(Exception) :
# {
    def __init__(self, message, cause=None) :
    # {
        super().__init__(message)
        self.cause = cause
    # }

# }

class AccountNotFoundException(AccountException) :
# {
    def __init__(self, account_id) :
    # {
        msg = "Account: " + account_id + " does not exist"
        super().__init__(msg)
        self.account_id = account_id
    # }
# }

class InsufficientFundsException(AccountException) :
# {
    def __init__(self, account_id) :
    # {
        msg = "Account: " + account_id + " has insufficient funds"
        super().__init__(msg)
        self.account_id = account_id
    # }
# }

class TransferFailedException(AccountException) :
# {
    def __init__(self, from_account_id, to_account_id) :
    # {
        msg = "Transfer from account: " + from_account_id + " to " + to_account_id, " failed"
        super().__init__(msg)
        self.from_account_id = from_account_id
        self.to_account_id = to_account_id
    # }
# }

# Simulate account operations
class AccountRepository :
# {
    def withdraw(self, account_id, amount) :
    # {
        # print()
        print("Attempting successful withdrawal...")

        # Simulate withdrawal logic
        if (random() < 0.5) :  # Simulate insufficient funds
        # {
            raise InsufficientFundsException(account_id)
        # }
        
        # Simulate account not found
        elif (account_id == "11111") :
        # {
            raise AccountNotFoundException(account_id)
        # }

        else :
        # {
            print("Withdrawal in the amount of: $", amount, "completed successfully.")
            print()
        # }

    # }

    def deposit(self, account_id, amount) :
    # {
        print("Attempting successful transfer...")

        # Simulate deposit logic
        if (account_id == "11111") :
        # {
            raise AccountNotFoundException(account_id)
        # }

        else :
        # {
            print("Deposit in the amount of: $", amount, " completed successfully.")
            print()
        # }

    # }

# }

# Service handling business logic for transfers
class AccountService :
# {
    def __init__(self) :
    # {
        self.account_repository = AccountRepository()
    # }

    def transfer_funds(self, from_account_id, to_account_id, amount) :
    # {
        try :
        # {
            self.account_repository.withdraw(from_account_id, amount)
            self.account_repository.deposit(to_account_id, amount)
        # }

        except TransferFailedException as e :
        # {
            raise TransferFailedException("Transfer failed from account ", from_account_id, " to account ", to_account_id) from e
        # }

    # }

# }

# Main function to execute the transfer
def main() :
# {
    account_service = AccountService()
    
    # Test case 1: Successful transfer
    # Note: This test case is subject to a 50% chance of simulating insufficient funds due to the random() logic.
    account_service.transfer_funds("20000", "30000", 100.00)
   
    # Test case 2: Account not found
    account_service.transfer_funds("11111", "67890", 150.00)

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