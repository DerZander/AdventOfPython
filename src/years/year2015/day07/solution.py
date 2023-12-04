from src.services.BaseSolution import BaseSolution


# https://adventofcode.com/2015/day/7

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = None
        self.answer_one = None
        self.answer_two = None
        self.wires = {}

    def number_to_binary(self, number):
        if type(number) is str:
            number = int(number)
        return bin(number)[2:]

    def binary_to_number(self, binary):
        return int(binary, 2)

    def left_shift(self, number, shift):
        return number << shift

    def right_shift(self, number, shift):
        return number >> shift

    def solve_test(self):
        for line in self.input_test_data.split("\n"):
            print(line)
            wire_id = line.split(" -> ")[-1]
            action = line.split(" -> ")[0]
            bin_action = 0
            value = 0
            if self.wires.get(wire_id) is None:
                self.wires[wire_id] = 0
            if "AND" in action:
                value = int(self.wires.get(action.split(" AND ")[0])) & int(self.wires.get(action.split(" AND ")[1]))
            elif "OR" in action:
                value = int(self.wires.get(action.split(" OR ")[0])) | int(self.wires.get(action.split(" OR ")[1]))
            elif "LSHIFT" in action:
                value = self.wires[action.split(" LSHIFT ")[0]] << int(action.split(" LSHIFT ")[1])
            elif "RSHIFT" in action:
                value = self.wires[action.split(" RSHIFT ")[0]] >> int(action.split(" RSHIFT ")[1])
            elif "NOT" in action:
                pass
            else:
                print(value)
                bin_action = self.number_to_binary(action)
                print(self.binary_to_number("1111111111111111"))
            self.wires[wire_id] = bin_action
        #     print(line)

        self.answer_test = self.wires

    def solve_one(self):
        self.answer_one = ""

    def solve_two(self):
        self.answer_two = ""


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
