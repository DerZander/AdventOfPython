from enum import Enum

from src.services.BaseSolution import BaseSolution, timer, SOLUTIONS


# https://adventofcode.com/2024/day/6
class Direction(Enum):
    RIGHT = ">"
    DOWN = "v"
    LEFT = "<"
    UP = "^"


class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0
        self.answer_one = 0
        self.answer_two = 0
        self.guard = {
            "x": 0,
            "y": 0,
            "direction": Direction.UP,
            "visited_positions": {}
        }
        self.grid = []
        self.blockers = 0
        self.data = None

    def setup(self):
        if self.current_solution == SOLUTIONS.TEST:
            self.data = self.input_test_data
        elif self.current_solution == SOLUTIONS.ONE:
            self.data = self.input_data
        elif self.current_solution == SOLUTIONS.TWO:
            self.data = self.input_data
        pass

    def load_map(self):
        self.grid = []
        for line_id, line in enumerate(open(self.input_file, "r").readlines()):
            row = []
            for col_id, col in enumerate(line):
                row.append(col)
                if col in ["^", "v", "<", ">"]:
                    self.guard["x"] = col_id
                    self.guard["y"] = line_id
                    self.guard["direction"] = Direction(col)
                    self.guard["visited_positions"] = {}
                    self.guard["visited_positions"][(self.guard["x"], self.guard["y"])] = 0
            self.grid.append(row)

    def save_position(self):
        if self.guard["visited_positions"].get((self.guard["x"], self.guard["y"])) is None:
            self.guard["visited_positions"][(self.guard["x"], self.guard["y"])] = 0
        self.guard["visited_positions"][(self.guard["x"], self.guard["y"])] += 0

        # self.guard["visited_positions"].append((self.guard["x"], self.guard["y"]))

    def check_can_leave(self):
        if self.guard["x"] == 0 and self.guard["direction"] == Direction.LEFT:
            return True
        elif self.guard["x"] == len(self.grid[0]) - 1 and self.guard["direction"] == Direction.RIGHT:
            return True
        elif self.guard["y"] == 0 and self.guard["direction"] == Direction.UP:
            return True
        elif self.guard["y"] == len(self.grid) - 1 and self.guard["direction"] == Direction.DOWN:
            return True
        return False

    def move_on_ice_riddle(self):
        can_leave = False
        while not can_leave:
            if self.guard["direction"] == Direction.RIGHT:
                if self.guard["x"] + 1 < len(self.grid[0]) and self.grid[self.guard["y"]][self.guard["x"] + 1] != "#":
                    self.guard["x"] += 1
                    self.save_position()
                else:
                    self.guard["direction"] = Direction.DOWN
            elif self.guard["direction"] == Direction.DOWN:
                if self.guard["y"] + 1 < len(self.grid) and self.grid[self.guard["y"] + 1][self.guard["x"]] != "#":
                    self.guard["y"] += 1
                    self.save_position()
                else:
                    self.guard["direction"] = Direction.LEFT
            elif self.guard["direction"] == Direction.LEFT:
                if self.guard["x"] - 1 >= 0 and self.grid[self.guard["y"]][self.guard["x"] - 1] != "#":
                    self.guard["x"] -= 1
                    self.save_position()
                else:
                    self.guard["direction"] = Direction.UP
            elif self.guard["direction"] == Direction.UP:
                if self.guard["y"] - 1 >= 0 and self.grid[self.guard["y"] - 1][self.guard["x"]] != "#":
                    self.guard["y"] -= 1
                    self.save_position()
                else:
                    self.guard["direction"] = Direction.RIGHT
            if self.check_can_leave():
                can_leave = True

    def find_loop_positions(self):
        loop_positions = set()
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == "." and (x, y) != (self.guard["x"], self.guard["y"]):
                    original_grid = [row[:] for row in self.grid]
                    self.grid[y][x] = "#"
                    self.guard["visited_positions"] = {}
                    self.move_on_ice_riddle()
                    if len(self.guard["visited_positions"]) < len(original_grid) * len(original_grid[0]):
                        loop_positions.add((x, y))
                    self.grid = original_grid
        return loop_positions

    @timer
    def solve_test(self):
        self.load_map()
        self.move_on_ice_riddle()
        self.answer_test = len(self.guard["visited_positions"])

    @timer
    def solve_one(self):
        self.load_map()
        self.move_on_ice_riddle()
        self.answer_one = len(self.guard["visited_positions"])

    @timer
    def solve_two(self):
        self.load_map()
        loop_positions = self.find_loop_positions()
    #     self.answer_two = len(loop_positions)


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
