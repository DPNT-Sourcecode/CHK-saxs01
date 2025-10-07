from solutions.CHK.checkout_solution import CheckoutSolution


class TestSum():
    def test_single_item(self):
        assert CheckoutSolution().checkout("A") == 50
        assert CheckoutSolution().checkout("B") == 30
        assert CheckoutSolution().checkout("C") == 20
        assert CheckoutSolution().checkout("D") == 15

