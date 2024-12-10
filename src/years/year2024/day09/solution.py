from src.services.BaseSolution import BaseSolution, timer, SOLUTIONS


# https://adventofcode.com/2024/day/9

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0
        self.answer_one = 0
        self.answer_two = 0
        self.data = None
        self.lines = []

    def setup(self):
        if self.current_solution == SOLUTIONS.TEST:
            self.data = self.input_test_data
        elif self.current_solution == SOLUTIONS.ONE:
            self.data = self.input_data
        elif self.current_solution == SOLUTIONS.TWO:
            self.data = self.input_data
        pass

    def generate_line(self):
        lines = [open(self.input_file, "r", encoding="utf-8").readline().strip()]
        self.lines = [int(x) for x in list(lines[0])]

    def part_one(self):
        strip, blocks, gaps = self.get_strip_blocks_gaps()
        free_space = strip.index(None)
        for i in reversed(range(0, len(strip))):
            if strip[i] is not None:
                strip[free_space] = strip[i]
                strip[i] = None
                while strip[free_space] is not None:
                    free_space += 1
                if i - free_space <= 1:
                    break
        return self.sum_strip(strip)

    def get_strip_blocks_gaps(self):
        position = 0
        strip, blocks, gaps = [], [], []
        is_block = True
        for i in range(len(self.lines)):
            if is_block:
                blocks.append((len(strip), position, self.lines[i]))
                strip.extend([position] * self.lines[i])
                position += 1
            else:
                gaps.append((self.lines[i], len(strip)))
                strip.extend([None] * self.lines[i])
            is_block = not is_block
        return strip, blocks, gaps

    @staticmethod
    def sum_strip(strip):
        result = 0
        for (itx, val) in enumerate(strip):
            if val is not None:
                result += val * itx
            else:
                result += 0
        return result

    def part_two(self):
        strip, blocks, gaps = self.get_strip_blocks_gaps()
        for block in reversed(blocks):
            (position, id, length) = block
            for itx, (gap_length, gap_position) in enumerate(gaps):
                if gap_position > position:
                    break

                if gap_length >= length:
                    for l in range(length):
                        strip[position + l] = None
                        strip[gap_position + l] = id

                    diff = gap_length - length
                    if diff > 0:
                        gaps[itx] = (diff, gap_position + length)
                    else:
                        gaps.pop(itx)
                    break
        return self.sum_strip(strip)

    @timer
    def solve_test(self):
        self.generate_line()
        self.answer_test = self.part_one()

    @timer
    def solve_one(self):
        self.generate_line()
        self.answer_one = self.part_one()

    @timer
    def solve_two(self):
        self.generate_line()
        self.answer_two = self.part_two()


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
