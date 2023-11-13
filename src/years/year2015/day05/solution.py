from src.services.BaseSolution import BaseSolution


class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0
        self.answer_one = 0
        self.answer_two = 0

    def solve_test(self):
        with(open("test_input.txt", "r")) as f:
            self.input_test_data = f.readlines()
        for line in self.input_test_data:
            if self.check_vowels(line) and self.check_double_letters(line) and self.check_special_chars(line):
                self.answer_test += 1

    def solve_one(self):
        with(open("input.txt", "r")) as f:
            self.input_test_data = f.readlines()
        for line in self.input_test_data:
            if self.check_vowels(line) and self.check_double_letters(line) and self.check_special_chars(line):
                self.answer_one += 1

    def solve_two(self):
        with(open("input.txt", "r")) as f:
            self.input_test_data = f.readlines()
        for line in self.input_test_data:
            if self.check_double_pair(line) and self.check_letter_between(line):
                self.answer_two += 1


    def check_special_chars(self, word):
        if not ("ab" in word or "cd" in word or "pq" in word or "xy" in word):
             return True
        return False

    def check_double_letters(self, word):
        for i in range(0, len(word) - 1):
            if word[i] == word[i + 1]:
                return True
        return False

    def check_vowels(self, word):
        vowels = ["a", "e", "i", "o", "u"]
        counter = 0
        for vowel in vowels:
            counter += word.count(vowel)
        print(counter)
        return counter >= 3

    def check_double_pair(self, line):
        for i in range(0, len(line) - 1):
            if line.count(line[i:i+2]) > 1:
                return True
        return False

    def check_letter_between(self, line):
        for i in range(0, len(line) - 2):
            if line[i] == line[i + 2]:
                return True
        return False


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
