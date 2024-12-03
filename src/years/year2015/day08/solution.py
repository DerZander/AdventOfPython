from src.services.BaseSolution import BaseSolution, timer, SOLUTIONS


# https://adventofcode.com/2015/day/8

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

    @timer
    def solve_test(self):
        self.answer_test = self.calculate_memory_difference(self.data)

    @timer
    def solve_one(self):
        self.answer_one = self.calculate_memory_difference(self.data)

    @timer
    def solve_two(self):
        self.answer_two = self.calculate_encoded_difference(self.data)

    def calculate_memory_difference(self, data):
        code_length = 0
        memory_length = 0
        for line in data:
            code_length += len(line)
            memory_length += len(eval(line))
        return code_length - memory_length

    def calculate_encoded_difference(self, data):
        code_length = 0
        encoded_length = 0
        for line in data:
            code_length += len(line)
            encoded_length += len(line.replace("\\", "\\\\").replace("\"", "\\\"")) + 2
        return encoded_length - code_length


if __name__ == "__main__":
    solution = Solution()
    solution.solve()