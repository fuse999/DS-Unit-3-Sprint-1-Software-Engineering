from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???',
         'TNT', 'Nuke', 'WILD-CAT', 'TRICK BALLS', 'SUPER OUTFIT']


def generate_products(num_products=30):
    products = []
    key = num_products
    while key > -1:
        name = sample(ADJECTIVES, 1)+"_"+sample(NOUNS, 1)
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.randint(0.0, 2.5)
        products = products.insert((name, price, weight, flammability))
        key = key-1
    return products


def inventory_report(products):
    pass  # TODO - your code! Loop over the products to calculate the report.

if __name__ == '__main__':
    inventory_report(generate_products())
