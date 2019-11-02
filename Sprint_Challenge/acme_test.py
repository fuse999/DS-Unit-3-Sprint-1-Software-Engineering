"""Performs unit tests on acme.py, and acme_report.py"""
# !/usr/bin/env python

import unittest
from acme import Product
from acme_repory import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are as safe as possible! LOL"""

    def test_default_product_price(self):
        """Test default product price of 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight of 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_explode(self):
        """Test for .explode in acme.py file"""
        prod = Product(name='Test Product',
                       weight=100, price=1,
                       flammability=0.5)
        self.assertEqual(prod.explode(), "...BABOOM!!")

    def test_stealable(self):
        """Test for .stealability in acme.py file"""
        prod = Product(name='Test Product',
                       weight=100, price=1,
                       flammability=0.5)
        self.assertEqual(prod.stealability(), "Not so stealable...")


class AcmeReportTests(unittest.TestCase):
    """Making sure the ACME report tests are up to standards"""

    def test_default_num_products(self):
        """Tests default number of products generated by generate_products()"""
        lst = generate_products()
        self.assertEqual(len(lst), 30)

    def test_legal_names(self):
        """Tests that the names are proper Acme names in lists"""
        products = generate_products()
        for product in products:
            test_adjective, test_noun = product.name.split("_")
            self.assertIn(test_adjective, ADJECTIVES)
            self.assertIn(test_noun, NOUNS)

if __name__ == '__main__':
    unittest.main()
