from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass

class NoDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        return total

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        self.percent = percent

    def apply_discount(self, total: float) -> float:
        return total * (1 - self.percent / 100)