from src.services.BaseSolution import BaseSolution, timer, SOLUTIONS


# https://adventofcode.com/2016/day/2

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = ""
        self.answer_one = ""
        self.answer_two = ""
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
        self.answer_test = self.calculate_code(self.data, part=1)

    @timer
    def solve_one(self):
        self.answer_one = self.calculate_code(self.data, part=1)

    @timer
    def solve_two(self):
        self.answer_two = self.calculate_code(self.data, part=2)

    def calculate_code(self, data, part):
        if part == 1:
            keypad = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ]
            start_pos = (1, 1)  # Starting at '5'
        else:
            keypad = [
                [None, None, '1', None, None],
                [None, '2', '3', '4', None],
                ['5', '6', '7', '8', '9'],
                [None, 'A', 'B', 'C', None],
                [None, None, 'D', None, None]
            ]
            start_pos = (2, 0)  # Starting at '5'

        code = []
        x, y = start_pos

        for line in data.splitlines():
            for move in line:
                if move == 'U' and y > 0 and keypad[y - 1][x] is not None:
                    y -= 1
                elif move == 'D' and y < len(keypad) - 1 and keypad[y + 1][x] is not None:
                    y += 1
                elif move == 'L' and x > 0 and keypad[y][x - 1] is not None:
                    x -= 1
                elif move == 'R' and x < len(keypad[y]) - 1 and keypad[y][x + 1] is not None:
                    x += 1
            code.append(keypad[y][x])

        return ''.join(map(str, code))


if __name__ == "__main__":
    solution = Solution()
    solution.solve()