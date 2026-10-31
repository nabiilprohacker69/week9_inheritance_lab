"""Abstract base class for every product (Lab 7, sections 1 and 3)."""
from abc import ABC, abstractmethod


def parse_price(value):
    """Accept 1200, 25.5, '$1200' or '$25.50'."""
    if isinstance(value, str):
        value = value.replace("$", "").replace(",", "").strip()
    return float(value)


class Product(ABC):
    """Data and behaviour shared by ALL products.

    Abstract: a plain Product cannot be created because get_fulfilment_info()
    has no implementation here. Only Physical/Digital products can exist.
    """

    def __init__(self, product_id, name, price, stock):
        self._product_id = product_id
        self._name = name
        self._price = parse_price(price)
        self._stock = int(stock)

    # ---- read-only access (encapsulation) ----
    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def stock(self):
        return self._stock

    # ---- shared behaviour ----
    def update_stock(self, new_quantity):
        """Set the stock level (same meaning as option 3 in menu)."""
        new_quantity = int(new_quantity)
        if new_quantity < 0:
            raise ValueError("Stock cannot be negative.")
        self._stock = new_quantity

    def display_information(self):
        print(f"ID: {self._product_id} | Name: {self._name} | "
              f"Price: ${self._price:.2f} | Stock: {self._stock}")

    def to_dict(self):
        """Common JSON fields"""
        return {
            "ID": self._product_id,
            "Name": self._name,
            "Price": self._price,
            "Stock": self._stock,
        }

    # ---- contract every subclass MUST fulfil ----
    @abstractmethod
    def get_fulfilment_info(self):
        """Describe how this product reaches the customer."""