from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def make_payment(self, amount):
        print(f"Paid {amount} using Credit Card.")
        
class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def pay(self, amount):
        self.payment_method.make_payment(amount)

cc = CreditCardPayment()
processor = PaymentProcessor(cc)
processor.pay(100)
