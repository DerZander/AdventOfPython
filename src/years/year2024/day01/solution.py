import numpy

from src.services.BaseSolution import BaseSolution, timer, SOLUTIONS


# https://adventofcode.com/2024/day/1

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0
        self.answer_one = 0
        self.answer_two = 0
        self.data = None

    def setup(self):
        if self.current_solution == SOLUTIONS.TEST:
            self.data = self.input_test_data
        elif self.current_solution == SOLUTIONS.ONE:
            self.data = self.input_data
        elif self.current_solution == SOLUTIONS.TWO:
            self.data = self.input_data
        pass




    @timer
    def solve_test(self):
        self.answer_test = self.compare_lists()#self.calculate_total_distance()

    def get_lists(self):
        first_list, second_list = [], []
        for line in open(self.input_file, "r").readlines():
            cutted_line = line.strip().split("   ")
            first_list.append(int(cutted_line[0]))
            second_list.append(int(cutted_line[1]))
        return first_list, second_list


    def compare_lists(self):
        first_list, second_list = self.get_lists()
        unique, counts = numpy.unique(second_list, return_counts=True)
        second_list_counts = dict(zip(unique, counts))
        sum = 0
        for entry in first_list:
            if entry in second_list_counts:
                sum += entry * second_list_counts.get(entry)
        return sum

    def calculate_total_distance(self):
        first_list, second_list = self.get_lists()
        first_list.sort()
        second_list.sort()
        distance = 0
        for i in range(len(first_list)):
            a = first_list[i]
            b = second_list[i]

            if a > b:
                difference = a - b
            elif b > a:
                difference = b - a
            else:
                difference = 0
            distance += difference
        return distance

    @timer
    def solve_one(self):
        self.answer_one = self.calculate_total_distance()

    @timer
    def solve_two(self):
        self.answer_two = self.compare_lists()


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
