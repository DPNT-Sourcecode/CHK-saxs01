from solutions.CHK.checkout_solution import CheckoutSolution


class TestSum():
    def test_checkout_single_item(self):
        assert CheckoutSolution().checkout("A") == 50
        assert CheckoutSolution().checkout("B") == 30
        assert CheckoutSolution().checkout("C") == 20
        assert CheckoutSolution().checkout("D") == 15

    def test_checkout_multiple_items(self):
        assert CheckoutSolution().checkout("AB") == 80
        assert CheckoutSolution().checkout("BA") == 80
    
    def test_checkout_offers(self):
        assert CheckoutSolution().checkout("AAA") == 130
        assert CheckoutSolution().checkout("BB") == 45
        assert CheckoutSolution().checkout("AAAA") == 180
        assert CheckoutSolution().checkout("BBB") == 75


    def test_non_string_input(self):
        assert CheckoutSolution().checkout(20) == -1
    
    def test_non_existing_item(self):
        assert CheckoutSolution().checkout("F") == -1
    
    def test_empty_cart(self):
        assert CheckoutSolution().checkout("") == 0





