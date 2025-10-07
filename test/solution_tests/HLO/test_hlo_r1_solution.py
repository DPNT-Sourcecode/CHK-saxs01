from solutions.HLO.hello_solution import HelloSolution


class TestHloR1():
    def test_sum(self):
        assert HelloSolution().hello("World!test") == "Hello, World!test"



