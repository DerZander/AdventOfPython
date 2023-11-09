from src.services.BaseSolution import BaseSolution


class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = None
        self.answer_one = None
        self.answer_two = None
        self.floor = 0

    def solve_test(self):
        for char in self.input_test_data:
            self.find_floor(char)
        self.answer_test = self.floor
        self.floor = 0

    def solve_one(self):
        for char in self.input_data:
            self.find_floor(char)
        self.answer_one = self.floor

    def find_floor(self, direction):
        if direction == "(":
            self.floor += 1
        else:
            self.floor -= 1

    def solve_two(self):
        self.floor = 0
        position = 0
        for char in self.input_data:
            position += 1
            self.find_floor(char)
            if self.floor < 0 and self.answer_two is None:
                self.answer_two = position


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
