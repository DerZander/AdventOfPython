from src.services.BaseSolution import BaseSolution


# 3287615-a788c276

# https://adventofcode.com/2023/day/1

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = None
        self.answer_one = None
        self.answer_two = None

    def replace_char_digits(self, line):
        numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        #     "one": 1,
        #     "two": 2,
        #     "three": 3,
        #     "four": 4,
        #     "five": 5,
        #     "six": 6,
        #     "seven": 7,
        #     "eight": 8,
        #     "nine": 9,
        #     "zero": 0
        # ]
        line_pointer = 0
        while line_pointer != len(line):
            word = ""
            print("hier")
            for c in line[line_pointer:]:
                print("word: ", word)
                if word in numbers:
                    print(numbers.index(word))
                    line = line.replace(word, str(numbers.index(word)), 1)
                    break
                word += c
                print(word)
            # if "eight" in line:
            #     print("hier")
            #
            # print(line)
            # for key, value in numbers.items():
            #     print(key)
            #     check_line = line[line_pointer:len(key)]
            #     print("check: ", check_line)
            #     if key in check_line:
            #         line = line.replace(check_line, str(value))
            #         print("hiiiiiiiiiiiiiiiiiier: ", key)
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

    def get_first_digit(self, line):
        number = 0
        for char in line:
            if char.isdigit():
                number = int(char)
                break
        return number

    def get_last_digit(self, line):
        number = 0
        for char in reversed(line):
            if char.isdigit():
                number = int(char)
                break
        return number

    def solve_test(self):
        answer = 0
        for line in self.input_test_data.splitlines():
            new_line = self.replace_char_digits(line)
            value = self.get_first_last_digit(new_line)
            print("Value:", value)
            answer += value
        self.answer_test = answer

    def solve_one(self):
        answer = 0
        for line in self.input_data.splitlines():
            answer += self.get_first_last_digit(line)
        self.answer_one = answer

    def solve_two(self):
        answer = 0
        # for line in self.input_data.splitlines():
        #     new_line = self.replace_char_digits(line)
        #     answer += self.get_first_digit(new_line)
        self.answer_two = answer


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
