from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def feed(self, feedback):
        pass


class CreditCard(Payment):

    def pay(self, amount):
        print(f"Payment done by credit card {amount}")

    def feed(self, feedback):
        print(f"Feedback is {feedback}")


class Jazzcash(Payment):

    def pay(self, amount):
        print(f"Payment done by JazzCash {amount}")

    def feed(self, feedback):
        print(f"Feedback is {feedback}")


mobileapp = Jazzcash()
mobileapp.pay(1000)
mobileapp.feed("Bad")

card = CreditCard()
card.pay(500)
card.feed("Good")