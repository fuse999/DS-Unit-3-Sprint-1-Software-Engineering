"""
Classes for acme
"""
# need imports
import random


class Product:
    """
    General production of Acme.Ink
    """
    fun_level = 5

    def __init__(self, name = "None", price = 10, weight = 20,
                 flammability = 0.5,
                 identifier = random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """How valuable is it"""
        stealometer = self.price/self.weight
        if stealometer < 0.5:
            return print("Not so stealable...")
        elif 0.5 > stealometer < 1:
            return print("Kinda stealable.")
        else:
            return print("Very stealable!")

    def explode(self):
        """This will tell how much the item will explode"""
        explodeymeter = self.flammability*self.weight
        if explodeymeter < 10:
            return print("...fizzle.")
        elif explodeymeter in range(9, 50):
            return print("...boom!")
        else:
            return print("...BABOOM!!")


class BoxingGlove(Product):
    """Subclass of Product called BoxingGlove"""
    def __init__(self, name = "The Best BoxingGlove Ever", price = 10,
                 weight = 20, flammability = 0.5,
                 identifier = random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = 10
        self.flammability = flammability
        self.identifier = identifier

    def explode(self):
        """it's a glove stupid"""
        return print("...it's a glove.")

    def punch(self):
        """This Will Hurt"""
        hurtymeter = self.weight
        if hurtymeter < 5:
            return print("That tickles.")
        elif hurtymeter in range(4, 15):
            return print("Hey that hurt!")
        else:
            return print("OUCH!")
