
class CheckoutSolution:
    def __init__(self):
        self.prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
        }

        self.offers = {
            "A": (3, 130),
            "B": (2, 45),
        }

        self.total = 0

    # skus = unicode string
    def checkout(self, skus) -> int:
        if not isinstance(skus, str):
            return -1
        
        if any(item not in self.prices for item in skus):
            return -1
        




