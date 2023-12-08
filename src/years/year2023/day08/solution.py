from src.services.BaseSolution import BaseSolution


# https://adventofcode.com/2023/day/8

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0  # Steps
        self.answer_one = 0  # Steps
        self.answer_two = 0
        self.steps_instructions = []
        self.step_rounds = 0
        self.desert_map = {}
        self.current_destination = "AAA"
        self.solution_part = 1
        self.target_desinations = []

    def setup(self):
        self.steps_instructions = []
        self.step_rounds = 0
        self.desert_map = {}
        self.current_destination = "AAA"
        if self.solution_part == 2:
            self.steps_instructions = []
            self.step_rounds = 0
            self.desert_map = {}
            self.current_destination = []

    def get_data(self, input_data):
        is_map = False
        for line in input_data.splitlines():
            if line == "":
                is_map = True
                continue
            if is_map:
                destination = line.split(" = ")[0]
                mapA = line.split("(")[1].split(",")[0]
                mapB = line.split(", ")[1].split(")")[0]

                self.desert_map[destination] = {"L": mapA, "R": mapB}
            else:
                self.steps_instructions = list(line)

    def solve_test(self):
        self.get_data(self.input_data)
        for destination in self.desert_map:
            if destination[-1] == "A":
                self.current_destination.append(destination)
            if destination[-1] == "Z":
                self.target_desinations.append(destination)

        for i in range(len(self.current_destination)):
            print(i)
            current_destination = self.current_destination[i]
            index = 0
            while self.current_destination[i] not in self.target_desinations:
                print(self.current_destination[i])
                direction = self.steps_instructions[index]
                next_destination = self.desert_map[current_destination][direction]
                self.current_destination[i] = next_destination

                index += 1
                if index > len(self.steps_instructions) - 1:
                    index = 0
                    self.step_rounds += 1
                self.answer_two += 1

    def solve_one(self):
        self.get_data(self.input_data)
        index = 0
        while self.current_destination != "ZZZ":
            direction = self.steps_instructions[index]
            next_destination = self.desert_map[self.current_destination][direction]
            self.current_destination = next_destination

            index += 1
            if index > len(self.steps_instructions) - 1:
                index = 0
                self.step_rounds += 1
            self.answer_one += 1
        self.solution_part = 2

    def solve_two(self):
        self.get_data(self.input_data)
        for destination in self.desert_map:
            if destination[-1] == "A":
                self.current_destination.append(destination)
            if destination[-1] == "Z":
                self.target_desinations.append(destination)

        for i in range(len(self.current_destination)):
            print(i)
            current_destination = self.current_destination[i]
            index = 0
            while self.current_destination[i] not in self.target_desinations:
                print(self.current_destination[i])
                direction = self.steps_instructions[index]
                next_destination = self.desert_map[current_destination][direction]
                self.current_destination[i] = next_destination

                index += 1
                if index > len(self.steps_instructions) - 1:
                    index = 0
                    self.step_rounds += 1
                self.answer_two += 1


if __name__ == "__main__":
    solution = Solution()
    solution.solve()

    # 107316 - to low
    # 21409 - to low
