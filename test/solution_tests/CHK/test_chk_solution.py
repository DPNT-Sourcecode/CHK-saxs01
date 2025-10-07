from solutions.CHK.checkout_solution import CheckoutSolution


class TestSum():
    def test_single_items(self):
        skus = "ABCD"
        assert CheckoutSolution().checkout(skus) == 115
