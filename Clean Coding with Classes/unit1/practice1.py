'''

Welcome to the first practical exercise on applying the Single Responsibility Principle (SRP)! In this task, you'll refactor a class that takes on multiple roles, making it more modular and easier to maintain.

The current UserProfile class manages user details, authentication, and notification tasks all in one place. Your job is to refactor the code to separate these concerns into distinct classes, each fulfilling a single responsibility.

The program involves managing user details, authenticating the user, and sending notifications. Let's get started on untangling this class into a cleaner, more modular design!

'''

class UserProfile :
# {
    def __init__(self, username, password, email) :
    # {
        self._username = username
        self._password = password
        self._email = email
    # }
# } 

class UserProfileAuthenticate :
# {
    def authenticate(self, user_profile_password, password) :
    # {
        # print(type(self))
        return user_profile_password == password
    # }
# }

class UserProfileSendEmail :
# {
    def send_email(self, user_profile_email, message) :
    # {
        print("Sending email to", user_profile_email, ':', message)
    # }
# }

def main() :

    user_profile = UserProfile("john_doe", "password123", "john_doe@example.com")
    user_profile_authenticate = UserProfileAuthenticate()

    if (user_profile_authenticate.authenticate(user_profile._password, "password123")) :
    # {
        user_profile_send_email = UserProfileSendEmail() 
        user_profile_send_email.send_email(user_profile._email, "Welcome back!")
    # }

    else :
    # {
        None
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

# UserProfileSendEmail(user_profile, user_profile._password)
        # user_profile, "Welcome back!")

    if (user_profile.authenticate("password123")) :
    # {
        user_profile.send_email("Welcome back!")
    # }

'''