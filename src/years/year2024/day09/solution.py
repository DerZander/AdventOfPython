from src.services.BaseSolution import BaseSolution, timer, SOLUTIONS


# https://adventofcode.com/2024/day/9

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0
        self.answer_one = 0
        self.answer_two = 0
        self.data = None
        self.line = ""
        self.point_counter = 0

    def setup(self):
        if self.current_solution == SOLUTIONS.TEST:
            self.data = self.input_test_data
        elif self.current_solution == SOLUTIONS.ONE:
            self.data = self.input_data
        elif self.current_solution == SOLUTIONS.TWO:
            self.data = self.input_data
        pass

    @staticmethod
    def is_odd(value):
        return value % 2 == 0

    def generate_line(self):
        line = open(self.input_file, "r").readline()
        filesystem_string = ""
        counter = 0
        for i, char in enumerate(line):
            if self.is_odd(i):
                for _ in range(int(char)):
                    filesystem_string += str(counter)
                counter += 1
            else:
                filesystem_string += "." * int(char)

        self.line = filesystem_string

    def find_latest_number(self):
        for id, char in enumerate(reversed(self.line)):
            if char.isdigit():
                index = len(self.line) - id - 1
                self.line = self.line[:index] + self.line[index + 1:]
                self.point_counter += 1
                return index, char
        return None, None

    def swap_chars(self, index):
        line = self.line
        number_id, number = self.find_latest_number()
        line = line[:index] + number + line[index + 1:]
        self.line = line

    def order_line(self):
        for i, char in enumerate(self.line):
            if not char.isdigit():
                self.swap_chars(i)
        return self.line

    def sum_all(self):
        result = 0
        counter = 0
        for i, char in enumerate(self.line):
            if char.isdigit():
                print(f"{counter} * {char} = {counter * int(char)}")
                result += int(char) * counter
                counter += 1
        return counter

    @timer
    def solve_test(self):
        self.generate_line()
        self.order_line()
        self.answer_test = self.sum_all()

    @timer
    def solve_one(self):
        self.answer_one = 0

    @timer
    def solve_two(self):
        self.answer_two = 0


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
