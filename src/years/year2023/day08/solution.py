from src.services.BaseSolution import BaseSolution, timer


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
        self.current_destinations = {}
        self.solution_part = 1
        self.target_desinations = []
        self.last_total = 0

    def setup(self):
        self.steps_instructions = []
        self.step_rounds = 0
        self.desert_map = {}
        self.current_destination = "AAA"
        self.current_destinations = {}

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
        self.get_data(self.input_test_data)
        for destination in self.desert_map:
            if destination[-1] == "A":
                self.current_destinations[destination] = destination  # {"current_destination": destination, "target": None}
            if destination[-1] == "Z":
                self.target_desinations.append(destination)

        all_at_z = self.check_all_at_z()
        index = 0

        while not all_at_z:
            step = self.steps_instructions[index]

            for key, current_destination in self.current_destinations.items():
                next_destination = self.desert_map[current_destination][step]
                self.current_destinations[key] = next_destination
            index += 1
            if index > len(self.steps_instructions) - 1:
                index = 0
                self.step_rounds += 1
            self.answer_test += 1
            all_at_z = self.check_all_at_z()

    def check_all_at_z(self):
        total = 0
        for key, current_destination in self.current_destinations.items():
            if current_destination in self.target_desinations:
                total += 1
        if total != self.last_total:
            self.last_total = total
            print(self.last_total)
        if total == len(self.current_destinations):
            return True
        return False

    def solve_one(self):
        self.get_data(self.input_data)
        index = 0
        while self.current_destination != "ZZZ":
            step = self.steps_instructions[index]
            next_destination = self.desert_map[self.current_destination][step]
            self.current_destination = next_destination

            index += 1
            if index > len(self.steps_instructions) - 1:
                index = 0
                self.step_rounds += 1
            self.answer_one += 1
        self.solution_part = 2

    @timer
    def solve_two(self):
        self.get_data(self.input_data)
        for destination in self.desert_map:
            if destination[-1] == "A":
                self.current_destinations[destination] = destination
            if destination[-1] == "Z":
                self.target_desinations.append(destination)

        all_at_z = self.check_all_at_z()
        index = 0
        number_of_z = 0
        while not all_at_z:
            step = self.steps_instructions[index]

            for key, current_destination in self.current_destinations.items():
                next_destination = self.desert_map[current_destination][step]
                self.current_destinations[key] = next_destination
            index += 1
            if index > len(self.steps_instructions) - 1:
                index = 0
                self.step_rounds += 1
            self.answer_two += 1
            # print(self.answer_two)
            all_at_z = self.check_all_at_z()


if __name__ == "__main__":
    solution = Solution()
    solution.solve(1)

    # 107322 - to low
    # 107317 - to low
    # 107316 - to low
    # 21409 - to low
