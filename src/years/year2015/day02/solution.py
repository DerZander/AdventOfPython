from src.services.BaseSolution import BaseSolution


class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = None
        self.answer_one = None
        self.answer_two = None

    def solve_test(self):
        for line in self.input_test_data.splitlines():
            l, w, h = line.split("x")
            l, w, h = int(l), int(w), int(h)
            wrap_ribbon = 2 * min(l + w, w + h, h + l)

            bow_ribbon = l * w * h
            ribbon_for_line = bow_ribbon + wrap_ribbon
            print(ribbon_for_line)

    def calc(self, line):
        l, w, h = line.split("x")
        l, w, h = int(l), int(w), int(h)
        square = 2 * l * w + 2 * w * h + 2 * h * l
        extra = min(l * w, w * h, h * l)
        return square + extra

    def solve_one(self):
        self.answer_one = 0
        for line in self.input_data.splitlines():
            self.answer_one += self.calc(line)

    def solve_two(self):
        self.answer_two = 0
        for line in self.input_data.splitlines():
            l, w, h = line.split("x")
            l, w, h = int(l), int(w), int(h)
            wrap_ribbon = 2 * min(l + w, w + h, h + l)

            bow_ribbon = l * w * h
            ribbon_for_line = bow_ribbon + wrap_ribbon
            self.answer_two += ribbon_for_line

if __name__ == "__main__":
    solution = Solution()
    solution.solve()