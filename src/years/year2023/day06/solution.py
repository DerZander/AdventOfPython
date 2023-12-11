import math
import re

from src.services.BaseSolution import BaseSolution


# https://adventofcode.com/2023/day/6

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.races = []
        self.answer_test = 0
        self.answer_one = None
        self.answer_two = None

    def solve_test(self):
        with open('input.txt') as f:
            self.data = f.read().replace(' ', '')
        options_per_race = self.get_winning_options()
        self.answer_test = options_per_race[0]

    def number_of_ways_to_win(self, race_duaration, record_distance):
        win_counter = 0
        for hold_duration in range(1, race_duaration):
            speed = hold_duration
            distance = (race_duaration - hold_duration) * speed
            if distance > record_distance:
                win_counter += 1
        return win_counter

    def get_winning_options(self):
        lines = self.data.splitlines()
        race_durations = [int(ms) for ms in re.findall(r'\d+', lines[0])]
        record_distances = [int(mm) for mm in re.findall(r'\d+', lines[1])]

        options_per_race = []
        for race_duration, record_distance in zip(race_durations, record_distances):
            options_per_race.append(self.number_of_ways_to_win(race_duration, record_distance))
        return options_per_race

    def solve_one(self):
        options_per_race = self.get_winning_options()
        self.answer_one = math.prod(options_per_race)

    def solve_two(self):
        with open('input.txt') as f:
            self.data = f.read().replace(' ', '')
        options_per_race = self.get_winning_options()
        self.answer_two = options_per_race[0]


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
