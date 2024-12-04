from collections import defaultdict

from src.services.BaseSolution import BaseSolution, timer, SOLUTIONS


# https://adventofcode.com/2024/day/4

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0
        self.answer_one = 0
        self.answer_two = 0
        self.data = None
        self.grid = defaultdict(str) # {0j:.., (1+0j):.., (1+1j):.., ...}
        self.x_positions = []
        self.a_positions = []

    def setup(self):
        if self.current_solution == SOLUTIONS.TEST:
            self.data = self.input_test_data
        elif self.current_solution == SOLUTIONS.ONE:
            self.data = self.input_data
        elif self.current_solution == SOLUTIONS.TWO:
            self.data = self.input_data
        pass

    def generate_grid(self):
        im = 0 + 1j
        self.grid = defaultdict(str)
        self.x_positions = []
        self.a_positions = []
        for row_id, row in enumerate(open(self.input_file, "r").readlines()):
            for col_id, col in enumerate(row.strip()):
                self.grid[col_id + row_id * im] = col
                if col == "X":  # save X locations
                    self.x_positions.append(col_id + row_id * im)
                if col == "A":
                    self.a_positions.append(col_id + row_id * im)

    def find_mas(self):
        counter = 0
        for xp in self.x_positions:
           for direction in [+1, -1, +1j, -1j, +1 + 1j, -1 + 1j, +1 - 1j, -1 - 1j]:
                if "".join([self.grid[xp + k * direction] for k in range(1, 4)]) == "MAS":
                     counter += 1
        return counter

    def find_xmas(self):
        counter = 0
        for ap in self.a_positions:
            c = [self.grid[ap + p] for p in [-1 + 1j, +1 + 1j, +1 - 1j, -1 - 1j]]
            if "".join(c) in ["MMSS", "MSSM", "SMMS", "SSMM"]:  # avoid "SMSM" and "MSMS", X of MAM and SAS
                counter += 1
        return counter

    @timer
    def solve_test(self):
        self.generate_grid()
        self.answer_test = self.find_xmas()

    @timer
    def solve_one(self):
        self.generate_grid()
        self.answer_one = self.find_mas()

    @timer
    def solve_two(self):
        self.generate_grid()
        self.answer_two = self.find_xmas()


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
