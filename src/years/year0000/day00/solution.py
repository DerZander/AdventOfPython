from src.services.BaseSolution import BaseSolution


class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_one = None
        self.answer_two = None

    def solve_one(self):
        self.answer_one = ""

    def solve_two(self):
        self.answer_two = ""


if __name__ == "__main__":
    solution = Solution()
    solution.solve()