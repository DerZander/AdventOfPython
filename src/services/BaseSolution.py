class BaseSolution:
    def __init__(self):
        self.answer_test = None
        self.input_test_data = None
        self.answer_one = None
        self.answer_two = None
        self.input_data = None
        self.get_test_input()
        self.get_input()

    def get_test_input(self):
        with(open("test_input.txt", "r")) as f:
            self.input_test_data = f.read()

    def solve_test(self):
        pass

    def get_test_answer(self):
        print(f"Test answer: {self.answer_test}")

    def get_answer_one(self):
        print(f"Solution one: {self.answer_one}")

    def get_answer_two(self):
        print(f"Solution two: {self.answer_two}")

    def solve_one(self):
        pass

    def solve_two(self):
        pass

    def get_input(self):
        with(open("input.txt", "r")) as f:
            self.input_data = f.read()

    def print_answers(self):
        with(open("answers.txt", "w")) as f:
            f.write(f"Test answer: {self.answer_test}\n")
            f.write(f"Solution one: {self.answer_one}\n")
            f.write(f"Solution two: {self.answer_two}\n")

    def solve(self, skip=None):
        if not skip >= 0:
            self.solve_test()
            self.get_test_answer()
        if not skip >= 1:
            self.setup()
            self.solve_one()
            self.get_answer_one()
        if not skip >= 2:
            self.setup()
            self.solve_two()
            self.get_answer_two()
        self.print_answers()

    def setup(self):
        pass
