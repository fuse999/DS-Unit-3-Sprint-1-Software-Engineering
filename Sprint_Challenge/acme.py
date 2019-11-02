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

    def __init__(self, name="None", price=10, weight=20,
                 flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        """How valuable is it"""
        stealometer = self.price / self.weight
        if stealometer < 0.5:
            return "Not so stealable..."
        elif (stealometer >= 0.5) and (stealometer < 1):
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        """This will tell how much the item will explode"""
        explodeymeter = self.flammability * self.weight
        if explodeymeter < 10:
            return "...fizzle."
        elif (explodeymeter >= 10) and (explodeymeter < 50):
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """Subclass of Product called BoxingGlove"""
    def __init__(self, name="The Best BoxingGlove Ever", price=10,
                 weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = 10
        self.flammability = flammability
        self.identifier = identifier

    def explode(self):
        """it's a glove stupid"""
        return "...it's a glove."

    def punch(self):
        """This Will Hurt"""
        hurtymeter = self.weight
        if hurtymeter < 5:
            return "That tickles."
        elif hurtymeter in range(4, 15):
            return "Hey that hurt!"
        else:
            return "OUCH!"
