"""Inventory manages Product objects. It calls their methods; it never does their work."""
import json
from ProductFactory import create_product_from_dict


class Inventory:
    def __init__(self):
        self._products = {}                      # ID -> Product

    def add_product(self, product):
        if product.product_id in self._products:
            raise ValueError(f"Product ID {product.product_id} already exists.")
        self._products[product.product_id] = product

    def get_product(self, product_id):
        return self._products.get(product_id)

    def update_stock(self, product_id, new_quantity):
        product = self.get_product(product_id)
        if product is None:
            raise KeyError(product_id)
        product.update_stock(new_quantity)       # the PRODUCT validates and updates

    def display_all(self):
        for product in self._products.values():
            product.display_information()

    def load(self, filename):
        with open(filename, "r") as file:
            records = json.load(file)
        products = [create_product_from_dict(r) for r in records]   # fail before changing state
        self._products = {p.product_id: p for p in products}

    def save(self, filename):
        with open(filename, "w") as file:
            json.dump([p.to_dict() for p in self._products.values()], file, indent=4)