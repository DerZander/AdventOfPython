from src.services.BaseSolution import BaseSolution


# https://adventofcode.com/2023/day/1

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = None
        self.answer_one = None
        self.answer_two = None
        self.numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}

    def replace_char_digits_reversed(self, line):
        line_pointer = len(line)
        while line_pointer != 0:
            word = ""
            for c in reversed(line[line_pointer:]):
                word = c + word
                if word in self.numbers:
                    line = line.replace(word, str(self.numbers.index(word) + 1), 1)
            line_pointer -= 1
        return line

    def replace_char_digits(self, line):
        line_pointer = 0
        while line_pointer != len(line):
            word = ""
            for c in line[line_pointer:]:
                word += c
                if word in self.numbers:
                    pass
            line_pointer += 1
        return line

    def get_first_last_digit(self, line):
        first_digit = 0
        last_digit = 0
        for char in line:
            if char.isdigit():
                first_digit = int(char)
                break
        for char in reversed(line):
            if char.isdigit():
                last_digit = int(char)
                break
        return int(f"{first_digit}{last_digit}")

    def solve_test(self):
        answer = 0
        for line in self.input_test_data.splitlines():
            first_value = self.get_char_digit(line)
            last_value = self.get_char_digit(line, first=False)
            value = int(f"{first_value}{last_value}")
            answer += value
        self.answer_test = answer

    def solve_one(self):
        answer = 0
        for line in self.input_data.splitlines():
            answer += self.get_first_last_digit(line)
        self.answer_one = answer

    def solve_two(self):
        answer = 0
        for line in self.input_data.splitlines():
            first_value = self.get_char_digit(line)
            last_value = self.get_char_digit(line, first=False)
            answer += int(f"{first_value}{last_value}")
        self.answer_two = answer

    def get_char_digit(self, line, first=True):
        word = ""
        if not first:
            line = reversed(line)
        for char in line:
            if char.isdigit():
                return int(char)
            else:
                if first:
                    word += char
                else:
                    word = char + word
                if len(word) >= 3:
                    for number, value in self.numbers.items():
                        if number in word:
                            return value


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
