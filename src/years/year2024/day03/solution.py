import re

from src.services.BaseSolution import BaseSolution, timer, SOLUTIONS


# https://adventofcode.com/2024/day/3

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

    @staticmethod
    def extract_mul_expressions(input_string):
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(pattern, input_string)
        return matches

    @timer
    def solve_test(self):
        matches = self.extract_mul_expressions(self.data)
        for match in matches:
            self.answer_test += int(match[0]) * int(match[1])

        # self.answer_test =""

    @timer
    def solve_one(self):
        matches = self.extract_mul_expressions(self.data)
        for match in matches:
            self.answer_one += int(match[0]) * int(match[1])

    @timer
    def solve_two(self):
        self.answer_two = ""


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
