class BaseSolution:
    def __init__(self):
        self.answer_one = None
        self.answer_two = None
        self.input_data = None
        self.get_input()

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
            print(self.input_data)

    def solve(self):
        self.solve_one()
        self.solve_two()
        self.get_answer_one()
        self.get_answer_two()
