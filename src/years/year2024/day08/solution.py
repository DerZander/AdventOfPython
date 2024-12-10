from src.services.BaseSolution import BaseSolution, timer, SOLUTIONS


# https://adventofcode.com/2024/day/8

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0
        self.answer_one = 0
        self.answer_two = 0
        self.data = None
        self.grid = []
        self.grid_size = {"length": 0, "width": 0}
        self.locations = {}
        self.antinodes = set()

    def setup(self):
        if self.current_solution == SOLUTIONS.TEST:
            self.data = self.input_test_data
        elif self.current_solution == SOLUTIONS.ONE:
            self.data = self.input_data
        elif self.current_solution == SOLUTIONS.TWO:
            self.data = self.input_data
        pass

    def generate_map(self):
        self.antinodes = set()
        self.grid = open(self.input_file, "r").read().strip().split("\n")
        self.grid_size = {"length": len(self.grid), "width": len(self.grid[0])}
        self.locations = {}
        for y in range(self.grid_size["length"]):
            for x in range(self.grid_size["width"]):
                if self.grid[y][x] != ".":
                    if self.grid[y][x] in self.locations:
                        self.locations[self.grid[y][x]].append((y, x))
                    else:
                        self.locations[self.grid[y][x]] = [(y, x)]

    def antinode(self, pr1, pr2, is_second=False):
        x1, y1 = pr1
        x2, y2 = pr2
        newx = x2 + (x2 - x1)
        newy = y2 + (y2 - y1)
        if is_second:
            self.antinodes.add((x2, y2))
            while self.get_inbounds(newx, newy):
                self.antinodes.add((newx, newy))
                newx += (x2 - x1)
                newy += (y2 - y1)
        else:
            if self.get_inbounds(newx, newy):
                self.antinodes.add((newx, newy))

    def get_inbounds(self, x, y):
        return 0 <= x < len(self.grid[0]) and 0 <= y < len(self.grid)

    def calculate_antinodes(self, is_second=False):
        for k in self.locations:
            node_list = self.locations[k]
            L = len(node_list)
            for i in range(L):
                for j in range(i):
                    node1 = node_list[i]
                    node2 = node_list[j]
                    self.antinode(node1, node2, is_second)
                    self.antinode(node2, node1, is_second)

    @timer
    def solve_test(self):
        self.generate_map()
        self.calculate_antinodes()
        self.answer_test = len(self.antinodes)

    @timer
    def solve_one(self):
        self.generate_map()
        self.calculate_antinodes()
        self.answer_one = len(self.antinodes)

    @timer
    def solve_two(self):
        self.generate_map()
        self.calculate_antinodes(is_second=True)
        self.answer_two = len(self.antinodes)


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
