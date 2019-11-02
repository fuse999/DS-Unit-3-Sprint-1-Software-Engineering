from random import randint, choice, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???',
         'TNT', 'Nuke', 'WILD-CAT', 'TRICK BALLS', 'SUPER OUTFIT']


def generate_products(count=30):
    """Generates a list of random ACME.ink products."""
    products = []

    for _ in range(0, count):
        """generates product and adds it to the products list"""
        products.append(
            Product(choice(ADJECTIVES) + "_" + choice(NOUNS),
                    price=randint(5, 100),
                    weight=randint(5, 100),
                    flammability=uniform(0.0, 2.5)))
    return products


def inventory_report(products, show_all=False):
    """Prints a list of ACME objects into a report."""
    print("\nACME CORPORATION OFFICIAL INVENTORY REPORT")
    totalPrice = 0
    totalWeight = 0
    totalFlammability = 0
    all_product_titles = []

    for _ in products:
        """Prints all the generated products"""
        if (show_all == True):  # Got PEP8 Error here not sure how to fix?
            print("\nDescription of", _.name, "[ID:", _.identifier, "]",
                  "\nPRICE:\t", _.price,
                  "\nWEIGHT:\t", _.weight,
                  "\nFLAMABILITY:\t", _.flammability)
        totalPrice += _.price
        totalWeight += _.weight
        totalFlammability += _.flammability
        all_product_titles.append(_.name)

    print("\nUnique product names:", len(set(all_product_titles)),
          "\nAverage Price:", totalPrice/len(products),
          "\nAverage Weight:", totalWeight/len(products),
          "\nAverage Flammability:", totalFlammability/len(products))

if __name__ == '__main__':
    inventory_report(generate_products())
