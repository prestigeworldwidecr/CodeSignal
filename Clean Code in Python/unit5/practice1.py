'''

In this task, we'll apply the DRY principle to simplify the code structure by eliminating duplication.

The current code contains repetitive logic spread across two methods, which leads to unnecessary complexity. Your mission is to refactor the code by introducing a helper method that consolidates these duplicate parts. The functionality must remain unchanged, but with a cleaner and more maintainable codebase.

'''

from enum import Enum
from typing import List


class Type(Enum) :
# {
    MAMMAL = 1
    FISH = 2
# }

class Animal :
# {
    def __init__(self, name: str, type: Type) :
    # {
        self.name = name
        self.type = type
    # }

# }

def find_mammals(animals: List[Animal]) -> List[Animal]:
    return find_animals_by_type(animals, Type.MAMMAL)

def find_fish(animals: List[Animal]) -> List[Animal]:
    return find_animals_by_type(animals, Type.FISH)

def find_animals_by_type(animals: List[Animal], type: Type) -> List[Animal] :
# {
    return [animal for animal in animals if animal.type == type]
# }

def main() :
# {
    animals = [
                Animal("Whale", Type.MAMMAL),
                Animal("Shark", Type.FISH),
                Animal("Tiger", Type.MAMMAL),
                Animal("Dolphin", Type.MAMMAL),
                Animal("Salmon", Type.FISH)
            ]
    
    mammals = find_mammals(animals)
    fish = find_fish(animals)
    
    print("Mammals:", " ".join(mammal.name for mammal in mammals))
    print("Fish:", " ".join(fish_item.name for fish_item in fish))

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


    animals = [
                Animal("Whale", Type.MAMMAL),
                Animal("Shark", Type.FISH),
                Animal("Tiger", Type.MAMMAL),
                Animal("Dolphin", Type.MAMMAL),
                Animal("Salmon", Type.FISH)
            ]
    
    # tmp = find_animals(animals)

    # print("Fish:", tmp[0])
    # print("Mammals:", tmp[1])

def find_mammals(animals: List[Animal]) -> List[Animal] :
# {
    mammals = []

    for animal in animals :
    # {
        if (animal.type == Type.MAMMAL) :
        # {
            mammals.append(animal)
        # }

        else :
        # {
            None
        # }

    # }

    return mammals

# }

def find_fish(animals: List[Animal]) -> List[Animal] :
# {
    fish = []

    for animal in animals :

        if (animal.type == Type.FISH) :
        # {
            fish.append(animal)
        # }

        else :
        # {
            None
        # }

    return fish

# }

def find_animals(animals) :
# {
    fish = ""
    mammals = ""

    for animal in animals :
    # {
        if (animal.type == Type.FISH) :
        # {
            fish = animal.name + " " + fish
        # }

        elif (animal.type == Type.MAMMAL) :
        # {
            mammals = animal.name + " " + mammals
        # }

        else :
        # {
            None
        # }

    # }

    return fish, mammals

# }

# fish.append(animal)
            # mammals.append(animal)

    # tmp = None

    # print(len(animals))
    # for i in range(len(animals)) :
    # {            
        # tmp = animals[i]

        # if (tmp == Type.FISH) :
        # elif (tmp == Type.MAMMAL) :
    # print(type(animals), type(animals[0]))

    # print(len(find_animals(animals)), animals[0].type, animals[0].name, animals[1].type, animals[1].name,
           # len((animals[0])))

    # for i in animals[0] :
    # {
    #    print(i)
    # }

    # print(len(fish), len(mammals))

    for mammal in mammals :
    # {
        # mammal = str(mammal).join(mammal.name)
       #  print("Mammals:", "".join(mammal.name))
        mammal = mammal.name + mammal.name
        # print("Mamm
    # }

    print("Mammals:", mammal)
    for fish in fish :
    # {
        fish = [" ".join(fish.name)]
        print("fish:", fish)
    # }

    # mammals = find_mammals(animals)
    # fish = find_fish(animals)
    
    # print("Mammals:", " ".join(mammal.name for mammal in mammals))
    # print("Fish:", " ".join(fish_item.name for fish_item in fish))
    # print("Fish:", " ".join(animals.name for animals.name in animals))

    for animal in animals :
    # {
        if (animal.type == Type.MAMMAL) :
        # {
            print("Mammals:", animal.name)
        # }

        else :
        # {
            print("Fish:", animal.name)
        # }

    # }

'''