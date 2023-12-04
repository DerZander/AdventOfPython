from src.services.BaseSolution import BaseSolution


# https://adventofcode.com/2015/day/6

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0
        self.answer_one = 0
        self.answer_two = 0
        self.light_grid = {}
        self.light_grid_two = {}

    def setup(self):
        for i in range(0, 1000):
            for j in range(0, 1000):
                self.light_grid[i, j] = False

    def do_lights(self, action, x1, y1, x2, y2):
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if action == "turn on":
                    self.light_grid[(x, y)] = True
                elif action == "turn off":
                    self.light_grid[(x, y)] = False
                elif action == "toggle":
                    self.light_grid[(x, y)] = not self.light_grid[(x, y)]

    def calculate_lights(self):
        for light in self.light_grid.items():
            print(light)

    def solve_test(self):
        self.answer_test = ""

    def get_test_input(self):
        with open("input.txt", "r") as f:
            self.input_data = f.readlines()

    def solve_one(self):
        with open("input.txt", "r") as f:
            for line in f.readlines():
                line = line.replace("\n", "")
                line_splitted = line.split(" ")
                x1, y1 = line_splitted[-3].split(",")
                x1, y1 = int(x1), int(y1)
                x2, y2 = line_splitted[-1].split(",")
                x2, y2 = int(x2), int(y2)
                if len(line_splitted) > 4:
                    action = f"{line_splitted[0]} {line_splitted[1]}"
                else:
                    action = line_splitted[0]
                self.do_lights(action, x1, y1, x2, y2)
        self.light_grid_two = self.light_grid
        for light in self.light_grid.items():
            if light[1]:
                self.answer_one += 1

    def solve_two(self):
        with open("input.txt", "r") as f:
            total_brightness = 0
            for line in f.readlines():
                line = line.replace("\n", "")
                line_splitted = line.split(" ")
                x1, y1 = line_splitted[-3].split(",")
                x1, y1 = int(x1), int(y1)
                x2, y2 = line_splitted[-1].split(",")
                x2, y2 = int(x2), int(y2)
                if len(line_splitted) > 4:
                    action = f"{line_splitted[0]} {line_splitted[1]}"
                else:
                    action = line_splitted[0]
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        lit = None
                        if action == "turn on":
                            lit = 1
                        elif action == "turn off":
                            lit = -1
                        elif action == "toggle":
                            lit = 2
                        if not self.light_grid[(x, y)] + lit < 0:
                            self.light_grid[(x, y)] += lit
                            total_brightness += lit

        self.answer_two = total_brightness


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
