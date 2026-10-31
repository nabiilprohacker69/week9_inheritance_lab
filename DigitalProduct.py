"""DigitalProduct: IS-A Product. Does NOT implement CanBeShipped."""
from product import Product


class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self._download_size = float(download_size)         # MB

    @property
    def download_size(self):
        return self._download_size

    def display_information(self):
        super().display_information()
        print(f"   Type: Digital | Download size: {self._download_size} MB")

    def get_fulfilment_info(self):
        return "Digital product: delivered electronically via download link."

    def to_dict(self):
        data = super().to_dict()
        data["Type"] = "digital"
        data["Download_Size"] = self._download_size
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["ID"], data["Name"], data["Price"], data["Stock"], data["Download_Size"])