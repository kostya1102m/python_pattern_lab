from product import Product
from typing import List

class CartItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

class Cart:
    def __init__(self):
        self.items: List[CartItem] = []

    def add_item(self, item: CartItem):
        for existing in self.items:
            if existing.product.name == item.product.name:
                existing.quantity += item.quantity
                return
        self.items.append(item)

    def remove_item(self, product_name: str, quantity: int):
        for item in self.items:
            if item.product.name == product_name:
                item.quantity -= quantity
                if item.quantity <= 0:
                    self.items.remove(item)
                return

    def get_total(self) -> float:
        return sum(item.product.price * item.quantity for item in self.items)