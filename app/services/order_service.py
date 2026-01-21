from interfaces.discount_strategy import DiscountStrategy
from interfaces.delivery_strategy import DeliveryStrategy
from infrastructure.payment_gateway import PaymentProcessor
from services.cart_service import Cart

class OrderProcessor:
    def __init__(
        self,
        cart: Cart,
        discount_strategy: DiscountStrategy,
        delivery_strategy: DeliveryStrategy,
        payment_processor: PaymentProcessor
    ):
        self.cart = cart
        self.discount_strategy = discount_strategy
        self.delivery_strategy = delivery_strategy
        self.payment_processor = payment_processor

    def process_order(self) -> dict:
        total = self.cart.get_total()
        discounted_total = self.discount_strategy.apply_discount(total)
        delivery_cost = self.delivery_strategy.calculate_cost()
        final_total = discounted_total + delivery_cost

        payment_success = self.payment_processor.process_payment(final_total)

        result = {
            "Начальная стоимость": total,
            "С учётом скидки": discounted_total,
            "Стоимость доставки": delivery_cost,
            "Итог": final_total,
            "Статус": "Успешно" if payment_success else "Неуспешно"
        }

        self.cart.clear()
        return result