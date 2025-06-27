'''

Welcome to the first practical exercise on mastering polymorphism in Python! In this task, you'll refine an existing codebase by implementing polymorphism. The current code uses a series of if-else statements to determine different animal behaviors. Your job is to refactor the code to leverage polymorphism through the use of an abstract base class, thereby making it cleaner and more maintainable.

The code currently has a regular Animal class with several animal classes inheriting from it. Your task is to:

Convert Animal into an abstract base class with an abstract feed method
Implement the feed method in each animal class to replace the conditional logic in the feed_animal function
Modify the feed_animal function to use polymorphism
This refactoring will demonstrate how polymorphism can make your code more elegant and extensible while enforcing a common interface across all animal types.

'''

from abc import ABC, abstractmethod

class Animal(ABC) :
# {
    # TODO: Convert this class to an abstract base class (ABC)
    # TODO: Add an abstract method 'feed' to enforce implementation in subclasses
    def feed(self) :
    # {
        None
    # }

# }

class Dog(Animal) :
# {
    def feed(self) :
    # {
        # TODO: Implement the 'feed' method specific to Dog
        print("Feeding the dog with dog food.")
    # }

# }

class Cat(Animal) :
# {
    def feed(self) :
    # {
        # TODO: Implement the 'feed' method specific to Cat
        print("Feeding the cat with cat food.")
    # }

# }

class Bird(Animal) :
# {
    def feed(self) :
    # {
        # TODO: Implement the 'feed' method specific to Bird
        print("Feeding the bird with bird seeds.")
    # }

# }

def feed_animal(animal) :
# {
    animal.feed()
# }

if (__name__ == "__main__") :
# {
    animals = [Dog(), Cat(), Bird()]

    for animal in animals :
    # {
        feed_animal(animal)
    # }

# }

else :
# {
    None
# }

'''

***** BONEYARD *****

# TODO: Modify this function to use polymorphism
    if (isinstance(animal, Dog)) :
    # {
        print("Feeding the dog with dog food.")
    # }

    elif (isinstance(animal, Cat)) :
    # {
        print("Feeding the cat with cat food.")
    # }

    elif (isinstance(animal, Bird)) :
    # {
        print("Feeding the bird with bird seeds.")
    # }

    else :
    # {
        print("Unknown animal type. Cannot feed.")
    # }

'''