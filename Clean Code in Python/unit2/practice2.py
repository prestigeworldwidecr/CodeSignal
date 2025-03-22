'''

Welcome to this engaging task on mastering meaningful and consistent naming conventions! Here, we'll focus on the importance of naming consistency while ensuring clarity and readability. The starter code features a fictional in-memory user database with varied and inconsistent method names that could potentially confuse other developers.

Your job is to refactor these methods to bring uniformity and clarity to the codebase. The functionality remains the same, but the code will become considerably more comprehensible and maintainable.

This code manages basic user operations in an in-memory database. Let's clean up the method names to make the code more intuitive!

'''

class User :
# {
    def __init__(self, user_id, name) :
    # {
        self.id = user_id
        self.name = name
    # }

# }

class UserDatabase :
# {
    def __init__(self) :
    # {
        self.users = []
    # }

    def addUser(self, user) :
    # {
        self.users.append(user)
    # }

    def getUser(self, name) :
    # {
        for user in self.users :
        # {
            if (user.name == name) :
            # {
                return user
            # }

            else :
            # {
                None
            # }

        # }        

    # }

    def allUsers(self) :
    # {
        return self.users
    # }

    def removeUser(self, name) :
    # {
        for user in self.users :
        # {
            if (user.name == name) :
            # {
                None
            # }

            else :
            # {
                self.users = [user]
            # }

        # }

    # }

    def deleteUsers(self) :
    # {
        self.users.clear()
    # }

# }


def main() :
# {
    user_db = UserDatabase()
    user_db.addUser(User(1, "Alice"))
    user_db.addUser(User(2, "Bob"))

    for user in user_db.allUsers() :
    # {
        print(user.name)  # Outputs all users
    # }

    user = user_db.getUser("Alice")

    if (user) :
    # {
        print("Found user:", user.name)
    # }

    else :
    # {
        print("User not found")
    # }

    user_db.removeUser("Alice")

    for user in user_db.allUsers() :
    # {
        print(user.name)  # Outputs all users
    # }

    for user in user_db.allUsers() :
    # {
        print(user.name)  # Outputs remaining users
    # }

    user_db.deleteUsers()

    for user in user_db.allUsers() :
    # {
        print(user.name)  # Outputs an empty list
    # }

# }

if __name__ == "__main__" :
# {
    main()
# }

else :
# {
    None
# }

'''

***** BONEYARD *****


                # print('%', len(self.users))

        
            # print('$', user.name)
                # print('#', len(self.users))

                # print('%', len(self.users))

        
            # print('$', user.name)
                # print('#', len(self.users))

print('!', user.name, name, len(self.users))

                # self.users.remove(name)

# self.users.index(name)
    print('!', user_db.allUsers().index("Alice"))
    # print(type(user_db.allUsers()))

for user in self.user_set :
        # {
            if (user.name == name) :
            # {
                self.user_set.remove(user)
            # }

            else :
            # {
                None
            # }

        # }

# self.user_set = [user for user in self.user_set if user.name != name]
            
        return None

        return self.users [self.users.index(name)]

'''