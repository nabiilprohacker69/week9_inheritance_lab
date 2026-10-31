"""Interface-style abstract base class (Lab 7, section 4): a contract only,
with no attributes and no implementation."""
from abc import ABC, abstractmethod


class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        """Return the cost of shipping this item."""