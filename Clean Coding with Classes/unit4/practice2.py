'''

In the previous task, we explored enhancing code reuse with inheritance. Now, let's shift our focus to a fundamental clean code principle: composition over inheritance. This task involves refactoring code where inheritance is misapplied due to a weak "is-a" relationship. Your objective is to simplify and optimize the structure by employing composition, making the code logical and flexible.

The aim is to shift from an inheritance model to a composition model, where a character "has" a weapon, enhancing logical structure and flexibility. This approach allows for seamless component swapping and supports potential expansion.

Let’s refactor this code using composition for clearer and more maintainable code!

Good effort, but your solution still uses inheritance instead of composition, and the weapon actions aren't specific like "Swinging the sword!" or "Shooting an arrow!".

Want to give it another shot, or would you like a hint?

Nice progress! You’re using composition by giving the Hero a Weapon, but there are a couple of things to improve:

Hero should not inherit from Weapon. Instead, Hero should just have a weapon as an attribute.
Each weapon should have its own class with a specific attack method (like use_weapon()), so you can print "Swinging the sword!" or "Shooting an arrow!" depending on the weapon.
What if you try making separate Sword and Bow classes, each with a use_weapon() method, and have Hero call that method? How would you update your Hero class to use any weapon?

Good try, but your code isn't quite there yet.

Your Hero class needs a proper __init__ method and an attack method, and the way you're using the Weapon class isn't showing composition. Want to give it another shot, or do you want a small hint?

Great! Here are a few things to focus on:

Your Hero class is missing a proper __init__ method (note the double underscores: __init__).
Hero should have a weapon attribute and an attack method that calls self.weapon.use_weapon().
You don't need a Weapon class that takes another class as an argument. Instead, just pass an instance of Sword or Bow directly to Hero.
Try updating your Hero class like this:

Add a correct __init__ method that takes a weapon parameter.
In your main block, create Hero(Sword()) and Hero(Bow()).
What do you think will happen if you try this approach?

'''

class Sword() :
# {
    def use_weapon(self) :
    # {
        print("Swinging the sword!")
    # }

# }

class Bow() :
# {
    def use_weapon(self) :
    # {
        print("Shooting an arrow!")
    # }
# }

class Hero :
# {
    def __init__(self, weapon) :
    # {
        self.weapon = weapon
    # }

    def attack(self) :
    # {
        self.weapon.use_weapon()
    # }

# }

if (__name__ == "__main__") :
# {
    hero = Hero(Sword())
    hero.attack()

    hero = Hero(Bow())
    hero.attack()
# }

else :
# {
    None
# }

'''

***** BONEYARD *****

# self.weapon.attack()
        

class Weapon :
# {
    def __init__(self, weapon_type) :
    # {
        self.weapon_type = weapon_type
    # }
    
    def attack(self) :
    # {
        self.use_weapon()
    # }

# }

def __init__(self, weapon_type) :
    # {
        self.weapon_type = weapon_type
    # }


class Weapon :
# {
    def __init__(self, weapon_type) :
    # {
        # print(weapon_type)
        self.weapon_type = weapon_type
    # }

# }

def attack(self) :
    # {
        # self.use_sword()
        print("Attacking with", weapon.weapon_type)
    # }

archer = Archer()
archer.attack()

class Sword :
# {
    def use_sword(self) :
    # {
        print("Swinging the sword!")
    # }

# }

class Bow :
# {
    def use_bow(self) :
    # {
        print("Shooting an arrow!")
    # }

# }

class Archer(Bow) :
# {
    def attack(self) :
    # {
        self.use_bow()
    # }

# }

'''