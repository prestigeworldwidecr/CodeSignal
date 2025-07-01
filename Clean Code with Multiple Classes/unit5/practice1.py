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

Good effort, but your solution is missing a few key requirements:

Your custom exceptions need to store the account_id and use clear, single-string messages.
Exception chaining (raise ... from ...) should be used for all relevant exceptions.
The main function should handle and print errors clearly.
Want to try fixing these? Let me know if you need a hint!

Cosmo
5:24 AM
Read message aloud
Good effort, but your solution isn't quite there yet.

You need to catch the lower-level exceptions in transfer_funds and raise a TransferFailedException using raise ... from .... Also, make sure your error messages are strings, and handle exceptions in main() to print clear messages.

Want to try fixing these? Let me know if you need a hint!

Cosmo
5:30 AM
Read message aloud
Good effort, but your solution is missing proper exception chaining and context preservation, and the main function doesn't handle or print errors as required.

Want to try fixing these issues, or do you need a hint?

Cosmo
Just now
Read message aloud
Good effort, but your solution doesn't fully meet the requirements.

You need to improve how exceptions are chained and handled in the service layer, and make sure error messages are printed in main(). Want to try fixing these, or do you need a hint?


c
Just now
hint
Cosmo
Just now
Read message aloud
Great! Here are a few focused hints to help you move forward:

In your AccountService.transfer_funds method, you should catch exceptions like InsufficientFundsException and AccountNotFoundException (not TransferFailedException), and then raise a TransferFailedException using raise ... from ... to preserve the original context.
Your TransferFailedException should accept a message and a cause (the original exception), not just account IDs.
In your main() function, wrap the transfer calls in try/except blocks to print clear error messages if a transfer fails.
Try updating just one part at a time—start with exception handling in transfer_funds. Want a more specific example of how to catch and re-raise with context?

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
        msg = str("Account: " + account_id + " does not exist")
        super().__init__(msg)
        self.account_id = account_id
    # }
# }

class InsufficientFundsException(AccountException) :
# {
    def __init__(self, account_id) :
    # {
        msg = str("Account: " + account_id + " has insufficient funds")
        super().__init__(msg)
        self.account_id = account_id
    # }
# }

class TransferFailedException(AccountException) :
# {
    def __init__(self, msg) :
    # {
        # msg = str("Transfer from account: " + from_account_id + " to " + to_account_id, " failed")
        super().__init__(msg)
        # self.from_account_id = from_account_id
        # self.to_account_id = to_account_id
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
            # msg = "Withdrawal failed from account: " + account_id + " amount: " + amount
            raise InsufficientFundsException(account_id)
        # }
        
        # Simulate account not found
        elif (account_id == "11111") :
        # {
            # msg = "Account: " + account_id + " does not exist"
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
        print("Attempting successful deposit...")

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

        except (InsufficientFundsException, AccountNotFoundException) as e :
        # {
            raise TransferFailedException("Transfer failed") from e
        # }

    # }

# }

# Main function to execute the transfer
def main() :
# {
    account_service = AccountService()
    from_account_id = "20000"
    to_account_id = "30000"
    
    # Test case 1: Successful transfer
    # Note: This test case is subject to a 50% chance of simulating insufficient funds due to the random() logic.
    try :
    # {
        account_service.transfer_funds(from_account_id, to_account_id, 100.00)
    # }

    except TransferFailedException as e :
    # {
        msg = "Transfer failed from account: " + from_account_id + " to account: " + to_account_id
        print(msg, " ", e)
    # }

    from_account_id = "11111"
    to_account_id = "67890"

    # Test case 2: Account not found
    try :
    # {
        account_service.transfer_funds(from_account_id, to_account_id, 150.00)
    # }

    except TransferFailedException as e :
    # {
        msg = "Transfer failed from account: " + from_account_id + " to account: " + to_account_id
        print(msg, " ", e)
    # }
    
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

# raise TransferFailedException(msg) from e
        # print("Transfer failed:", e)
        # raise TransferFailedException(msg) from e

try :
        # {
            print("Attempting successful deposit...")
            self.account_repository.withdraw(from_account_id, amount)
        # }

        except InsufficientFundsException as e :
        # {
            # msg = "Withdrawal failed from account: " + from_account_id + " amount: " + amount
            raise InsufficientFundsException(from_account_id) #, msg) from e
        # }

        except AccountNotFoundException as e :
        # {
            # msg = "Account: " + from_account_id + " does not exist"
            raise AccountNotFoundException(from_account_id) # , msg) from e
        # }

        except TransferFailedException as e :
        # {
            msg = "Transfer failed from account: " + from_account_id + " to account: " + to_account_id
            raise TransferFailedException(msg) from e
        # }
    
        try : 
        # {   
            self.account_repository.deposit(to_account_id, amount)
        # }

        except TransferFailedException as e :
        # {
            msg = "Transfer failed from account: " + from_account_id + " to account: " + to_account_id
            raise TransferFailedException(msg) from e
        # }

'''