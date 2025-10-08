from collections import Counter


class CheckoutSolution:
    def __init__(self):
        self.prices = {
            "A": 50,
            "B": 30,
            "C": 20,
            "D": 15,
            "E": 40,
        }

        
        self.multi_offers = {
            "A": [(5, 200), (3, 130)],
            "B": [(2, 45)],
        }

        self.free_offers = {
            "E": ("B", 1, 2)
        }


    # skus = unicode string
    def checkout(self, skus) -> int:
        total = 0
        if not isinstance(skus, str):
            return -1
        
        if any(item not in self.prices for item in skus):
            return -1
        
        counts = Counter(skus)
        
        # for item, count in counts.items():
        #     if item in self.offers:
        #         offer_qty, offer_price = self.offers[item]

        #         offer_count = count // offer_qty
        #         remainder = count % offer_qty
        #         total += offer_count * offer_price + remainder * self.prices[item]
        #     else:
        #         total += count * self.prices[item]

        for item, (free_item, free_)


        return total






