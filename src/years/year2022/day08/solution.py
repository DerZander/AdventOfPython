from src.services.BaseSolution import BaseSolution


# https://adventofcode.com/2022/day/8

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = None
        self.answer_one = None
        self.answer_two = None

    def solve_test(self):
        self.answer_test = ""

    def solve_one(self):
        self.answer_one = ""

    def solve_two(self):
        self.answer_two = ""


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
