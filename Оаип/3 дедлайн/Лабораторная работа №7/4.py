from abc import ABC,abstractmethod
class PaymentSystem(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    @abstractmethod
    def refund(self,amount):
        pass
class CreditCardPayment(PaymentSystem):
    def pay(self,amount):
        print(f"Оплата картой {amount}")
    def refund(self,amount):
        print(f"Возврат на карту {amount}")
class PayPalPayment(PaymentSystem):
    def pay(self,amount):
        print(f"Оплата через PayPal {amount}")
    def refund(self,amount):
        print(f"Возврат через PayPal {amount}")