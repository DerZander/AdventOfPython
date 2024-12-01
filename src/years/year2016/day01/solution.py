from src.services.BaseSolution import BaseSolution, timer, SOLUTIONS


# https://adventofcode.com/2016/day/1

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

    @timer
    def solve_test(self):
        self.answer_test = self.calculate_first_revisited_distance(self.data)

    @timer
    def solve_one(self):
        self.answer_one = self.calculate_distance(self.data)

    @timer
    def solve_two(self):
        self.answer_two = self.calculate_first_revisited_distance(self.data)

    def calculate_distance(self, data):
        directions = data.split(", ")
        x, y = 0, 0
        direction = 0  # 0: North, 1: East, 2: South, 3: West

        for move in directions:
            turn = move[0]
            steps = int(move[1:])

            if turn == 'R':
                direction = (direction + 1) % 4
            elif turn == 'L':
                direction = (direction - 1) % 4

            if direction == 0:
                y += steps
            elif direction == 1:
                x += steps
            elif direction == 2:
                y -= steps
            elif direction == 3:
                x -= steps

        return abs(x) + abs(y)

    def calculate_first_revisited_distance(self, data):
        directions = data.split(", ")
        x, y = 0, 0
        direction = 0  # 0: North, 1: East, 2: South, 3: West
        visited = set()
        visited.add((x, y))

        for move in directions:
            if not move:
                continue

            turn = move[0]
            steps = int(move[1:])

            if turn == 'R':
                direction = (direction + 1) % 4
            elif turn == 'L':
                direction = (direction - 1) % 4

            for _ in range(steps):
                if direction == 0:
                    y += 1
                elif direction == 1:
                    x += 1
                elif direction == 2:
                    y -= 1
                elif direction == 3:
                    x -= 1

                if (x, y) in visited:
                    return abs(x) + abs(y)
                visited.add((x, y))

        return None


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
