"""PhysicalProduct: IS-A Product and CanBeShipped (Lab 7, sections 1.2, 2, 3.2, 4.2)."""
from product import Product
from CanBeShipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):
    """One real parent (Product) plus one interface (CanBeShipped)."""

    BASE_SHIPPING = 5.00     # my simple rule: flat fee ...
    COST_PER_KG = 2.00       # ... plus a cost per kilogram

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)   # reuse parent constructor
        self._weight = float(weight)                       # kg

    @property
    def weight(self):
        return self._weight

    def display_information(self):
        super().display_information()                      # parent prints common info
        print(f"   Type: Physical | Weight: {self._weight} kg")

    def get_fulfilment_info(self):
        return "Physical product: requires storage and physical shipping."

    def calculate_shipping_cost(self):
        return self.BASE_SHIPPING + self.COST_PER_KG * self._weight

    def to_dict(self):
        data = super().to_dict()
        data["Type"] = "physical"
        data["Weight"] = self._weight
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["ID"], data["Name"], data["Price"], data["Stock"], data["Weight"])