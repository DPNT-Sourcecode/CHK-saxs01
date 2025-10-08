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

        for item, (free_item, free_qty, req_qty) in self.free_offers.items():
            if item in counts:
                num_qualified_offers = counts[item] // req_qty

                if free_item in counts:
                    counts[free_item] = max(0, counts[free_item] - num_qualified_offers * free_qty)

        
        return total


    def calculate_best_offer_price(unit_price, count, offers):
        offer_price = 0
        offers = sorted(offers, key=lambda x: -x[0])

        for quantity, offer_price in offers:
            num_offers = count // quantity
            offer_price += num_offers * offer_price
            count %= quantity

        offer_price += count * unit_price
        return offer_price


