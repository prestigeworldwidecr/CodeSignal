'''

In this task, we will take a closer look at the use of boolean flags in methods and how they can obscure the purpose of the code. The current method uses a boolean flag to change its behavior, which can make the code less readable and more difficult to maintain. Your task is to refactor this functionality into two separate methods with self-explanatory names, thereby enhancing both clarity and usability.

The code you're working on involves account management, where a method either activates or deactivates an account, depending on the provided boolean flag. Let’s refactor this so that there are two distinct methods: one for activating the account and the other for deactivating it.

'''

class Account :
# {
    def __init__(self, initial_status) :
    # {
        self.status = initial_status
    # }

    def set_status(self, new_status) :
    # {
        self.status = new_status
    # }

    def get_status(self) :
    # {
        return self.status
    # }

# }

def deactivate_account(account) :
# {
    account.set_status("Inactive")
# }

def activate_account(account) :
# {
    account.set_status("Active")
# }

def main() :
# {    
    account = Account("Inactive")

    activate_account(account)
    print("Account status after activation:", account.get_status())

    deactivate_account(account)
    print("Account status after deactivation:", account.get_status())
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

# set_active_status(account, True)
    # set_active_status(account, False)

def set_active_status(account, is_active) :
# {
    if (is_active) :
    # {
        account.set_status("Active")
    # }

    else :
    # {
        account.set_status("Inactive")
    # }

# }

'''