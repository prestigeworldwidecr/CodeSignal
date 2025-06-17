'''

In the previous task, we focused on the "Feature Envy" code smell. Now, let's dive into the world of "Message Chains." You'll encounter a scenario where accessing a method requires navigating through multiple objects, which may reduce code clarity and increase the likelihood of errors. Your task is to refactor the code by moving method calls into their respective classes to break the message chains. Refactoring will involve creating new methods in existing classes to encapsulate the data access and provide a clean, simplified interface for retrieving information. Focus on restructuring the code so that each class is responsible for its specific piece of data, effectively removing the need for deep navigation through multiple objects.

'''

class User :
# {
    def __init__(self, address) :
    # {
        self._address = address
    # }

    def get_address(self) :
    # {
        return self._address.full_address()
    # }

# }

class Address :
# {
    def __init__(self, city, zip_code) :
    # {
        self._city = city
        self._zip_code = zip_code
    # }

    def full_address(self) :
    # {
        return self._city.full_city_name() + ' ' + self._zip_code
    # }

# }

class City :
# {
    def __init__(self, city_name, state) :
    # {
        self._city_name = city_name
        self._state = state
    # }

    def full_city_name(self) :
    # {
        return self._city_name + ' ' + self._state
    # }

# }

if (__name__ == "__main__") :
# {
    user = User(Address(City("New York", "NY"), "10001"))

    # full_address = f"{user.get_address().get_city().get_city_name()}, " \
    #               f"{user.get_address().get_city().get_state()}, Zip Code: " \
    #               f"{user.get_address().get_zip_code()}"
    
    print("Full Address:", user.get_address())
# }

else :
# {
    None
#}

'''

***** BONEYARD *****


    def get_address(self):
    # {
        return self._address
    # }

    def get_city(self) :
    # {
        return self._city
    # }

    def get_zip_code(self) :
    # {
        return self._zip_code
    # }

    def get_city_name(self) :
    # {
        return self._city_name
    # }

    def get_state(self) :
    # {
        return self._state
    # }

'''