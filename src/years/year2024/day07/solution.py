from src.services.BaseSolution import BaseSolution, timer, SOLUTIONS


# https://adventofcode.com/2024/day/7

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0
        self.answer_one = 0
        self.answer_two = 0
        self.data = None

    def setup(self):
        if self.current_solution == SOLUTIONS.TEST:
            self.data = self.input_test_data
        elif self.current_solution == SOLUTIONS.ONE:
            self.data = self.input_data
        elif self.current_solution == SOLUTIONS.TWO:
            self.data = self.input_data
        pass

    @staticmethod
    def calculate_answer_one(values, key):
        is_ok = False
        for i in range(2 ** (len(values) - 1)):
            result = values[0]
            for j in range(len(values) - 1):
                if (i >> j) & 1 == 1:
                    result *= values[j + 1]
                else:
                    result += values[j + 1]
            if result == key:
                is_ok = True
                break
        if is_ok:
            return key
        else:
            return 0

    @staticmethod
    def calculate_answer_two(values, key):
        is_ok = False
        for i in range(3 ** (len(values) - 1)):
            result = values[0]
            for j in range(len(values) - 1):
                total = (i // 3 ** j) % 3
                if total == 2:
                    result = int(str(result) + str(values[j + 1]))
                elif total == 1:
                    result *= values[j + 1]
                else:
                    result += values[j + 1]
            if result == key:
                is_ok = True
                break
        if is_ok:
            return key
        else:
            return 0

    def calculate_total_calibration(self):
        total = 0
        for line in open(self.input_file).readlines():
            line = list(line.split())
            key, values = int(line[0][:-1]), list(map(int, line[1:]))
            self.answer_one += self.calculate_answer_one(values, key)
            self.answer_two += self.calculate_answer_two(values, key)
        return total

    @timer
    def solve_test(self):
        self.answer_test = self.calculate_total_calibration()

    @timer
    def solve_both(self):
        self.calculate_total_calibration()
        self.solve_one()
        self.solve_two()


if __name__ == "__main__":
    solution = Solution()
    solution.solve_both_answers()
