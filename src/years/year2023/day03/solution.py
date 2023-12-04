from src.services.BaseSolution import BaseSolution


# https://adventofcode.com/2023/day/3

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = None
        self.answer_one = None
        self.answer_two = None
        self.grid = []
        self.part_list = []
        self.coord = [0, 0]

    def check_connections(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                print(self.get_grid_value(x, y))

    def get_grid_value(self, x, y):
        return self.grid[y][x]

    def get_grid(self, input_data):
        for line in input_data.splitlines():
            self.grid.append(list(line))

    def solve_test(self):
        self.get_grid(self.input_test_data)
        self.check_connections()

        self.answer_test = self.grid

    def solve_one(self):
        self.answer_one = ""

    def solve_two(self):
        self.answer_two = ""


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
