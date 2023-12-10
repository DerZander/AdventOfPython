from src.services.BaseSolution import BaseSolution, timer


# https://adventofcode.com/0000/day/00

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = None
        self.answer_one = None
        self.answer_two = None

    def setup(self):
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
