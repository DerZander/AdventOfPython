from src.services.BaseSolution import BaseSolution, timer, SOLUTIONS


# https://adventofcode.com/2024/day/11

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0
        self.answer_one = 0
        self.answer_two = 0
        self.data = None
        self.stones = []

    def setup(self):
        if self.current_solution == SOLUTIONS.TEST:
            self.data = self.input_test_data
        elif self.current_solution == SOLUTIONS.ONE:
            self.data = self.input_data
        elif self.current_solution == SOLUTIONS.TWO:
            self.data = self.input_data
        pass

    def generate_stones(self):
        self.stones = []
        for number in self.data.split(" "):
            self.stones.append(int(number))

    def check_stone_line(self):
        last_added_id = None
        for i, stone in enumerate(self.stones):
            if i == last_added_id:
                continue
            if stone == 0:
                self.stones[i] = 1
            elif (len(str(stone)) % 2) == 0:
                stone_length = len(str(stone))
                half_left, half_right = str(stone)[:stone_length // 2], str(stone)[stone_length // 2:]
                last_added_id = i + 1
                self.stones[i] = int(half_left)
                self.stones.insert(last_added_id, int(half_right))
            else:
                self.stones[i] = stone * 2024

    @timer
    def solve_test(self):
        self.generate_stones()
        for _ in range(25):
            self.check_stone_line()
        self.answer_test = len(self.stones)

    @timer
    def solve_one(self):
        self.generate_stones()
        for _ in range(25):
            self.check_stone_line()
            print(f"{_} / 25 finished")
        self.answer_one = len(self.stones)

    @timer
    def solve_two(self):
        self.generate_stones()
        for _ in range(75):
            self.check_stone_line()
            print(f"{_} / 75 finished | Stones: {len(self.stones)}")
        self.answer_two = len(self.stones)


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
