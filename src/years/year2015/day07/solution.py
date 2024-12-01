from src.services.BaseSolution import BaseSolution

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_one = None
        self.answer_two = None
        self.wires = {}

    def get_value(self, wire):
        if wire.isdigit():
            return int(wire)
        if wire not in self.wires:
            return None
        if isinstance(self.wires[wire], int):
            return self.wires[wire]
        parts = self.wires[wire].split()
        if len(parts) == 1:
            value = self.get_value(parts[0])
        elif len(parts) == 2:
            value = ~self.get_value(parts[1]) & 0xFFFF
        elif len(parts) == 3:
            left = self.get_value(parts[0])
            right = self.get_value(parts[2])
            if parts[1] == "AND":
                value = left & right
            elif parts[1] == "OR":
                value = left | right
            elif parts[1] == "LSHIFT":
                value = left << int(parts[2])
            elif parts[1] == "RSHIFT":
                value = left >> int(parts[2])
        self.wires[wire] = value
        return value

    def solve(self):
        for line in self.input_data.splitlines():
            parts = line.split(" -> ")
            self.wires[parts[1]] = parts[0]

        self.answer_one = self.get_value("a")

        # Reset wires and override b with the value of a
        self.wires = {}
        for line in self.input_data.splitlines():
            parts = line.split(" -> ")
            self.wires[parts[1]] = parts[0]
        self.wires["b"] = str(self.answer_one)

        self.answer_two = self.get_value("a")

if __name__ == "__main__":
    solution = Solution()
    solution.solve()
    print(f"Answer One: {solution.answer_one}")
    print(f"Answer Two: {solution.answer_two}")