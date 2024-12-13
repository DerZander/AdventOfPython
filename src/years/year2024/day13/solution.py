from enum import Enum

from src.services.BaseSolution import BaseSolution, timer, SOLUTIONS


# https://adventofcode.com/2024/day/13


## A = 3
## B = 1
class Buttons(Enum):
    A = 3
    B = 1


class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0
        self.answer_one = 0
        self.answer_two = 0
        self.data = None
        self.machines = []
        self.claw = {
            "x": 0,
            "y": 0,
        }
        self.tokens = []
        self.fails = 0

    def setup(self):
        if self.current_solution == SOLUTIONS.TEST:
            self.data = self.input_test_data
        elif self.current_solution == SOLUTIONS.ONE:
            self.data = self.input_data
        elif self.current_solution == SOLUTIONS.TWO:
            self.data = self.input_data
        pass

    def move_claw(self, x, y, tokens):
        self.claw["x"] += x
        self.claw["y"] += y
        self.tokens += tokens

    def generate_machine_list(self):
        self.machines = []
        machine = {}
        for line in open(self.input_file).readlines():
            if len(line) == 1:
                self.machines.append(machine)
                machine = {}
            else:
                x, y = line.split(":")[1].strip().split(", ")
                x = x[2:]
                y = y[2:]
                if "A" in line:
                    machine["A"] = {"x": int(x), "y": int(y)}
                elif "B" in line:
                    machine["B"] = {"x": int(x), "y": int(y)}
                else:
                    machine["price"] = {"x": int(x), "y": int(y)}

    def check_combination_of_machine(self, machine):
        a_counter, b_counter = 0, 0

        for a in range(100):
            for b in range(100):
                claw_x = machine["A"]["x"] * a + machine["B"]["x"] * b
                claw_y = machine["A"]["y"] * a + machine["B"]["y"] * b
                # print(claw_x, claw_y)
                if claw_x == machine["price"]["x"] and claw_y == machine["price"]["y"]:
                    a_counter = a
                    b_counter = b
        tokens = a_counter * 3 + b_counter
        print(tokens)
        return tokens

    def check_combination_of_machine_modified(self, machine):
        a_counter, b_counter = 0, 0

        for a in range(100):
            for b in range(100):
                claw_x = machine["A"]["x"] * a + machine["B"]["x"] * b
                claw_y = machine["A"]["y"] * a + machine["B"]["y"] * b
                # print(claw_x, claw_y)
                if claw_x == machine["price"]["x"] and claw_y == machine["price"]["y"]:
                    a_counter = a
                    b_counter = b
        tokens = a_counter * 3 + b_counter
        print(tokens)
        return tokens

    def modify_prices(self):
        for id, machine in enumerate(self.machines):
            self.machines[id]["price"]["x"] = machine["price"]["x"] * 10000000000000
            self.machines[id]["price"]["y"] = machine["price"]["y"] * 10000000000000

    def get_fewest_token(self, max_steps=100):
        tokens = []
        for machine in self.machines:
            token = self.check_combination_of_machine(machine)
            tokens.append(token)
            if tokens == 0:
                self.fails += 1

        return tokens

    @timer
    def solve_test(self):
        self.generate_machine_list()
        for machine in self.machines:
            tokens = self.check_combination_of_machine(machine)
            self.tokens.append(tokens)
            if tokens == 0:
                self.fails += 1
        self.answer_test = self.tokens

    @timer  # 26005
    def solve_one(self):
        self.generate_machine_list()
        fewest_tokens = self.get_fewest_token()
        for token in fewest_tokens:
            self.answer_one += token

    @timer
    def solve_two(self):
        self.generate_machine_list()
        self.modify_prices()
        fewest_tokens = self.get_fewest_token()
        for token in fewest_tokens:
            self.answer_one += token
        self.answer_two = 0


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
