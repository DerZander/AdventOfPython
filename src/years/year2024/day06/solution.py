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
            "visited_positions": set()
        }
        self.grid = []
        self.grid_size = None
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
                    # self.guard["visited_positions"] = {}
                    # self.guard["visited_positions"][(self.guard["x"], self.guard["y"])] = 0

                    self.guard["visited_positions"].add((self.guard["x"], self.guard["y"]))
            # self.grid.append(row)
            self.grid.append(line.strip())
        self.grid_size = (len(self.grid[0]), len(self.grid))

    def save_position(self):
        self.guard["visited_positions"].add((self.guard["x"], self.guard["y"]))
        # if self.guard["visited_positions"].get((self.guard["x"], self.guard["y"])) is None:
        #     self.guard["visited_positions"][(self.guard["x"], self.guard["y"])] = 0
        # self.guard["visited_positions"][(self.guard["x"], self.guard["y"])] += 0

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

    def can_move_two(self, specx, specy):
        visited = set()
        dir_index = 0
        cur_loc = (self.guard["x"], self.guard["y"])
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        grid_length, grid_width = self.grid_size
        while 0 <= cur_loc[0] < grid_length and 0 <= cur_loc[1] < grid_width:

            pdir_index = dir_index
            curx, cury = cur_loc

            next_loc = (curx + dirs[dir_index][0], cury + dirs[dir_index][1])
            while 0 <= next_loc[0] < grid_length and 0 <= next_loc[1] < grid_width and (self.grid[next_loc[0]][next_loc[1]] == "#" or next_loc == (specx, specy)):
                dir_index = (dir_index + 1) % 4
                next_loc = (curx + dirs[dir_index][0], cury + dirs[dir_index][1])
            self.guard["visited_positions"].add((cur_loc, pdir_index))
            cur_loc = next_loc
            if (next_loc, dir_index) in self.guard["visited_positions"]:
                return True
        return False

    def find_loop_positions(self):
        result = 0
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j] != ".":
                    b = self.can_move_two(i, j)
                    result += int(b)
        return result

    @timer
    def solve_test(self):
        self.load_map()
        self.move_on_ice_riddle()
        self.answer_test = len(self.guard["visited_positions"])

    @timer  # 4711
    def solve_one(self):
        self.load_map()
        self.move_on_ice_riddle()
        self.answer_one = len(self.guard["visited_positions"])

    @timer  # 1562
    def solve_two(self):
        self.load_map()
        self.answer_two = self.find_loop_positions()


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
