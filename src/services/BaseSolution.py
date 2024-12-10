from enum import Enum


def timer(func):
    def wrap_func(*args, **kwargs):
        import time
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
        return result

    return wrap_func


class SOLUTIONS(Enum):
    TEST = 0
    ONE = 1
    TWO = 2


class BaseSolution:
    def __init__(self):
        self.answer_test = None
        self.input_test_data = None
        self.answer_one = None
        self.answer_two = None
        self.input_data = None
        self.data = None
        self.input_file = "test_input.txt"
        self.current_solution = SOLUTIONS.TEST
        self.get_test_input()
        self.get_input()

    def get_test_input(self):
        with(open("test_input.txt", "r")) as f:
            self.input_test_data = f.read()

    def get_input(self):
        with(open("input.txt", "r")) as f:
            self.input_data = f.read()

    def solve_test(self):
        pass

    def get_test_answer(self):
        print(f"Test answer: {self.answer_test}")

    def get_answer_one(self):
        print(f"Solution one: {self.answer_one}")

    def get_answer_two(self):
        print(f"Solution two: {self.answer_two}")

    @timer
    def solve_one(self):
        pass

    @timer
    def solve_two(self):
        pass

    @timer
    def solve_both(self):
        pass

    def print_answers(self):
        with(open("answers.txt", "w")) as f:
            f.write(f"Test answer: {self.answer_test}\n")
            f.write(f"Solution one: {self.answer_one}\n")
            f.write(f"Solution two: {self.answer_two}\n")

    def run_test(self):
        self.solve_test()
        self.get_test_answer()

    def solve(self, skip=None):
        if skip is None or not skip >= 0:
            self.current_solution = SOLUTIONS.TEST
            self.setup()
            self.run_test()
        self.input_file = "input.txt"
        if skip is None or not skip >= 1:
            self.current_solution = SOLUTIONS.ONE
            self.setup()
            self.solve_one()
            self.get_answer_one()
        if skip is None or not skip >= 2:
            self.current_solution = SOLUTIONS.TWO
            self.setup()
            self.solve_two()
            self.get_answer_two()
        self.print_answers()

    def solve_both_answers(self):
        self.current_solution = SOLUTIONS.ONE
        self.input_file = "input.txt"
        self.setup()
        self.solve_both()
        self.get_answer_one()
        self.get_answer_two()
        self.print_answers()

    def setup(self):
        if self.current_solution == SOLUTIONS.TEST:
            self.data = self.input_test_data
        elif self.current_solution == SOLUTIONS.ONE or self.current_solution == SOLUTIONS.TWO:
            self.data = self.input_data
        pass
