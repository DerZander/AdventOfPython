from src.services.BaseSolution import BaseSolution, timer, SOLUTIONS


# https://adventofcode.com/2016/day/11

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0
        self.answer_one = 0
        self.answer_two = 0
        self.data = None

    def setup(self):
        if self.current_solution == SOLUTIONS.TEST:
            self.data = self.input_test_data
        elif self.current_solution == SOLUTIONS.ONE:
            self.data = self.input_data
        elif self.current_solution == SOLUTIONS.TWO:
            self.data = self.input_data
        pass

    @timer
    def solve_test(self):
        self.answer_test = ""

    @timer
    def solve_one(self):
        self.answer_one = ""

    @timer
    def solve_two(self):
        self.answer_two = ""


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
