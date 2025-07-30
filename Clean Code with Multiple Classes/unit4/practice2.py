'''

In this task, you'll refactor a Python codebase that currently uses type checking (isinstance()) to determine animal behaviors. The code needs to be improved using polymorphism and interface-based design patterns.

The starter code includes several animal classes (Dog, Cat, and Bird) with helper functions that contain all the behavior logic. This approach is problematic because:

It requires modifying the helper functions each time a new animal type is added
It violates the Open-Closed Principle
It makes the code harder to maintain and extend
Your task is to refactor this code by:

Making Animal an abstract base class with the required feed behavior
Creating a Playable interface for animals that can play
Moving the behavior implementations into their respective classes
Using polymorphism to eliminate type checking
This refactoring will make the code more maintainable, extensible, and aligned with object-oriented principles. You'll use Python's abc module to create abstract base classes and implement multiple inheritance where needed.

'''

from abc import ABC, abstractmethod

class Animal(ABC) :
# {
    def feed(self) :
    # {
        None
    # }

    def play(self) :
    # {
        None
    # }

# }

class Playable(ABC) :
# {
    @abstractmethod
    def play(self) :
    # {
        None
    # }

# }

class Dog(Animal, Playable) :
# {
    def feed(self) :
    # {
        print("Feeding the dog with dog food.")
    # }

    def play(self) :
    # {
        print("Playing fetch with the dog.")
    # }
    
# }

class Cat(Animal, Playable) :
# {
    def feed(self) :
    # {
        print("Feeding the cat with cat food.")
    # }

    def play(self) :
    # {
        print("Playing with the cat using a ball of yarn.")
    # }

# }

class Bird(Animal) :
# {
    def feed(self) :
    # {
        print("Feeding the bird with bird seeds.")
    # }
# }

def feed_animal(animal) :
# {
    animal.feed()
# }    

def play_with_animal(animal) :
# {
    if (isinstance(animal, Bird)) :
    # {
        print("Birds don't play like other animals.")
    # }

    else :
    # {
        animal.play()
    # }
    
# }


if (__name__ == '__main__') :
# {
    animals = [Dog(), Cat(), Bird()]

    for animal in animals :
    # {
        feed_animal(animal)
        play_with_animal(animal)
    # }

# }

else :
# {
    None
# }

'''

***** BONEYARD *****

if (isinstance(self, Bird)) :
        # {
            print("Birds don't play like other animals.")
        # }

        else :
        # {
            self.play(self)
        # }


if (isinstance(animal, Dog)) :

        print("Playing fetch with the dog.")

    elif (isinstance(animal, Cat)) :
    # {
        print("Playing with the cat using a ball of yarn.")
    # }

    else :
    # {
        None
    # }

class Playable(ABC) :
# {
    @abstractmethod
    def play(self) :
    # {
        None
    # }

# }

'''