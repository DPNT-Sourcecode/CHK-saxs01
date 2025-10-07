from solutions.HLO.hello_solution import HelloSolution


class TestHlo():
    def test_hello(self):
        assert HelloSolution().hello("World") == "Hello, World!"

