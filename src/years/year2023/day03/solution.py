from src.services.BaseSolution import BaseSolution


# https://adventofcode.com/2023/day/3

def check_char_is_symbol(char):
    if char == "." or char.isdigit():
        return False
    return True


class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0
        self.answer_one = 0
        self.answer_two = 0
        self.grid = []
        self.part_list = []
        self.coord = [0, 0]

        self.number_string = ""
        self.number_is_connected = False

    def check_connections(self):
        pass

    def get_grid_value(self, x, y):
        return self.grid[y][x]

    def get_grid(self, input_data):
        grid = []
        for line in input_data.splitlines():
            grid.append(list(line))
        self.grid = grid

    def solve_test(self):
        total = 0
        self.get_grid(self.input_test_data)
        l_grid = len(self.grid)
        for y in range(l_grid):
            for x in range(len(self.grid[y])):
                char = self.get_grid_value(x, y)
                if char.isdigit():
                    self.number_string += char
                    if self.check_char_surroundings(x, y):
                        self.number_is_connected = True
                    continue
                else:
                    if self.number_string.isdigit():
                        number = int(self.number_string)
                        self.number_string = ""
                        if self.number_is_connected:
                            total += number
                            self.number_is_connected = False
        self.answer_test = total

    def check_char_surroundings(self, x, y):
        for yy in range(-1, 2):
            for xx in range(-1, 2):
                _x = x + xx
                if _x < 0:
                    _x = 0
                if _x > len(self.grid[y]) - 1:
                    _x = len(self.grid[y]) - 1
                _y = y + yy
                if _y < 0:
                    _y = 0
                if _y > len(self.grid) - 1:
                    _y = len(self.grid) - 1
                char = self.get_grid_value(_x, _y)
                if check_char_is_symbol(char):
                    return True
        return False

    def solve_one(self):  # 546312
        total = 0
        my_lst = []
        self.get_grid(self.input_data)
        l_grid = len(self.grid)
        for y in range(l_grid):
            for x in range(len(self.grid[y])):
                char = self.get_grid_value(x, y)
                if char.isdigit():
                    self.number_string += char
                    if self.check_char_surroundings(x, y):
                        self.number_is_connected = True
                    continue
                else:
                    if self.number_string.isdigit():
                        number = int(self.number_string)
                        self.number_string = ""
                        if self.number_is_connected:
                            total += number
                            my_lst.append(number)
                            self.number_is_connected = False
        self.answer_one = total
        # 831312

    def solve_two(self):
        self.answer_two = ""


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
