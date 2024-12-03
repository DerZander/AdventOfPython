import re

from src.services.BaseSolution import BaseSolution, timer, SOLUTIONS
from src.years.year2024.day03.test import enabled


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



    def extract_mul_expressions(self):
        pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
        matches = re.finditer(pattern, self.data)
        return [{"value":int(match[1])*int(match[2]), "position":match.start()} for match in matches]


    def find_do_range(self):
        pattern_do = r"do\(\)"
        pattern_do_not = r"don't\(\)"
        matches_do = re.finditer(pattern_do, self.data)
        matches_do_not = re.finditer(pattern_do_not, self.data)
        results_do = [(match.start(), match.end()) for match in matches_do]
        results_do_not = [(match.start(), match.end()) for match in matches_do_not]

        ranges = []
        if results_do_not:
            ranges.append((0, results_do_not[0][0]))  # Add range from 0 to the start of the first `don't()`
        for do, dont in zip(results_do, results_do_not[1:]):
            ranges.append((do[1], dont[0]))

        # Handle the case where there is no `don't()` after the last `do()`
        if results_do and (not results_do_not or results_do[-1][1] > results_do_not[-1][0]):
            ranges.append((results_do[-1][1], len(self.data)))

        return ranges

    @timer
    def solve_test(self):
        ranges = self.find_do_range()
        matches = self.extract_mul_expressions()
        for match in matches:
            print(match)
            for r in ranges:
                if r[0] <= match["position"] < r[1]:
                    self.answer_test += match["value"]
                    break

    @timer
    def solve_one(self):
        matches = self.extract_mul_expressions()
        for match in matches:
            self.answer_one += match["value"]

    @timer
    def solve_two(self):
        log_text = self.data
        enabled = True
        for i in range(len(log_text)):
            if log_text[i:].startswith('do()'):
                enabled = True
            if log_text[i:].startswith("don't()"):
                enabled = False
            match = re.match(r'mul\((\d{1,3}),(\d{1,3})\)', log_text[i:])
            if match is not None:
                x, y = int(match.group(1)), int(match.group(2))
                self.answer_two += x * y if enabled else 0


if __name__ == "__main__":
    solution = Solution()
    solution.solve()


#143409234 to high