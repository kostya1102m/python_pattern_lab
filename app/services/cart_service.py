from entities.product import Product
from typing import List

class Cart:
    def __init__(self):
        self.items: List[Product] = []

    def add_item(self, product: Product):
        self.items.append(product)

    def remove_item(self, product_id: int):
        self.items = [item for item in self.items if item.id != product_id]

    def get_total(self) -> float:
        return sum(item.price for item in self.items)

    def clear(self):
        self.items.clear()