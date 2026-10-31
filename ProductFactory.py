"""Maps the saved "Type" value to the right class (Lab 7, section 5).
The one place that knows which product types exist."""
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

_PRODUCT_TYPES = {
    "physical": PhysicalProduct,
    "digital": DigitalProduct,
}


def create_product_from_dict(data):
    product_class = _PRODUCT_TYPES.get(str(data.get("Type", "")).lower())
    if product_class is None:
        raise ValueError(
            f"Product {data.get('ID', '?')} has no valid \"Type\" "
            f"(expected 'physical' or 'digital'). Old Week 5 records need a Type added."
        )
    return product_class.from_dict(data)