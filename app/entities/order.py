from cart import Cart

class Order:
    def __init__(self, cart: Cart, discount: float, shipping_cost: float, final_amount: float):
        self.cart = cart
        self.discount = discount
        self.shipping_cost = shipping_cost
        self.final_amount = final_amount