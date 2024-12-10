from src.services.BaseSolution import BaseSolution, timer, SOLUTIONS

# https://adventofcode.com/2024/day/10

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]


class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0
        self.answer_one = 0
        self.answer_two = 0
        self.data = None
        self.map = {}
        self.trailheads = []

    def setup(self):
        if self.current_solution == SOLUTIONS.TEST:
            self.data = self.input_test_data
        elif self.current_solution == SOLUTIONS.ONE:
            self.data = self.input_data
        elif self.current_solution == SOLUTIONS.TWO:
            self.data = self.input_data
        pass

    def generate_map(self):
        self.map = {}
        for y, l in enumerate(open(self.input_file, "r").readlines()):
            for x, c in enumerate(l.strip()):
                self.map[(x, y)] = c

        self.trailheads = []
        for position in self.map:
            if self.map[position] == '0':
                self.trailheads.append(position)

    def find_trails(self, xy, trail):
        if self.map[xy] == '9':
            return [trail]
        else:
            trails = []
            for d in directions:
                n_xy = (xy[0] + d[0], xy[1] + d[1])
                if int(self.map.get(n_xy, 0)) - int(self.map.get(xy)) == 1:
                    trails += self.find_trails(n_xy, trail + [n_xy])
            return trails

    def sum_trailhead_score(self):
        result = 0
        for position in self.trailheads:
            trail_list = []
            for trail in self.find_trails(position, []):
                trail_list.append(trail[-1])
            unique_trail_list = set(trail_list)
            result += len(unique_trail_list)
        return result

    def sum_trailhead_ratings(self):
        result = 0
        for position in self.trailheads:
            trail_list = []
            for trail in self.find_trails(position, []):
                trail_list.append(trail)
            result += len(trail_list)
        return result

    @timer
    def solve_test(self):
        self.generate_map()
        self.answer_test = self.sum_trailhead_ratings()

    @timer
    def solve_one(self):
        self.generate_map()
        self.answer_one = self.sum_trailhead_score()

    @timer
    def solve_two(self):
        self.generate_map()
        self.answer_two = self.sum_trailhead_ratings()


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
