from src.services.BaseSolution import BaseSolution


# https://adventofcode.com/2015/day/6

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = None
        self.answer_one = None
        self.answer_two = None
        self.grid = {}

    def setup(self):
        self.grid = {}

    def solve_test(self):
        current_position = (0, 0)
        for direction in self.input_test_data:
            dir = self.go(direction)
            current_position = (current_position[0] + dir[0], current_position[1] + dir[1])
            self.grid[current_position] = self.grid.get(current_position, 0) + 1

        self.answer_test = len(self.grid)

    def solve_one(self):
        current_position = (0, 0)
        for direction in self.input_data:
            dir = self.go(direction)
            current_position = (current_position[0] + dir[0], current_position[1] + dir[1])
            self.grid[current_position] = self.grid.get(current_position, 0) + 1
        self.answer_one = len(self.grid)

    def solve_two(self):
        current_position = (0, 0)
        robo_position = (0, 0)
        self.grid[current_position] = self.grid.get(current_position, 0) + 1
        self.grid[robo_position] = self.grid.get(robo_position, 0) + 1
        current_santa = True
        for direction in self.input_data:
            dir = self.go(direction)
            if current_santa:
                current_position = (current_position[0] + dir[0], current_position[1] + dir[1])
                self.grid[current_position] = self.grid.get(current_position, 0) + 1
                current_santa = False
            else:
                robo_position = (robo_position[0] + dir[0], robo_position[1] + dir[1])
                self.grid[robo_position] = self.grid.get(robo_position, 0) + 1
                current_santa = True

        self.answer_two = len(self.grid)

    def go(self, direction):
        dir = {
            '^': (0, 1),
            'v': (0, -1),
            '>': (1, 0),
            '<': (-1, 0)
        }
        return dir[direction]


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
