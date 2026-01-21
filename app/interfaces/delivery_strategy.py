from abc import ABC, abstractmethod

class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate_cost(self) -> float:
        pass

class FreeDelivery(DeliveryStrategy):
    def calculate_cost(self) -> float:
        return 0.0

class StandardDelivery(DeliveryStrategy):
    def calculate_cost(self) -> float:
        return 5.0

class ExpressDelivery(DeliveryStrategy):
    def calculate_cost(self) -> float:
        return 15.0