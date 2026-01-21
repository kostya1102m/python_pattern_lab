from entities.product import Product
from services.cart_service import Cart
from interfaces.discount_strategy import PercentageDiscount, NoDiscount
from interfaces.delivery_strategy import StandardDelivery, ExpressDelivery
from infrastructure.payment_gateway import PaymentProcessor
from services.order_service import OrderProcessor

import json

# Фасад
class OrderFacade:
    def __init__(self):
        self.cart = Cart()
        self.payment_processor = PaymentProcessor()

    def add_to_cart(self, product: Product):
        self.cart.add_item(product)

    def place_order(
        self,
        discount_strategy=None,
        delivery_strategy=None
    ):
        if discount_strategy is None:
            discount_strategy = NoDiscount()
        if delivery_strategy is None:
            delivery_strategy = StandardDelivery()

        processor = OrderProcessor(
            cart=self.cart,
            discount_strategy=discount_strategy,
            delivery_strategy=delivery_strategy,
            payment_processor=self.payment_processor
        )
        result = processor.process_order()
        return json.dumps(result, indent=2)

if __name__ == "__main__":
    facade = OrderFacade()

    
    facade.add_to_cart(Product(1, "Мыло", 1000.0))
    facade.add_to_cart(Product(2, "Шило", 1000.00))

    
    result = facade.place_order(
        discount_strategy=PercentageDiscount(10),
        delivery_strategy=ExpressDelivery()
    )

    print("Order_results", result)