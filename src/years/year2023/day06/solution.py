from src.services.BaseSolution import BaseSolution


# https://adventofcode.com/2023/day/6

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.races = []
        self.answer_test = 0
        self.answer_one = None
        self.answer_two = None

    def setup(self):
        self.races = []

    def move_distance(self, milliseconds, time):
        speed = milliseconds
        rest_time = time - milliseconds
        distance = 0
        if rest_time > 0:
            distance = speed * rest_time
        return distance

    def solve_test(self):
        races_choices = []
        data = self.input_test_data.split()
        time_start = 1
        distance_start = 5
        for i in range(2, 3):
            race = {
                "time": int(data[time_start + i]),
                "distance": int(data[distance_start + i])
            }
            # self.races.append(race)
            race_choices = 0
            for holding_button_millisecond in range(race["time"] + 1):
                print(holding_button_millisecond)
                holding_time = holding_button_millisecond
                distance = self.move_distance(holding_time, race["time"])
                if distance >= race["distance"]:
                    race_choices += 1
            races_choices.append(race_choices)
        answer = 1
        for c in races_choices:
            print(c)
            answer *= c
        self.answer_test = answer

    def solve_one(self):
        self.answer_one = ""

    def solve_two(self):
        self.answer_two = ""


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
