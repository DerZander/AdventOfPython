import hashlib

from src.services.BaseSolution import BaseSolution


# https://adventofcode.com/2015/day/6

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = None
        self.answer_one = None
        self.answer_two = None
        self.input_data = "bgvyzdsv"

    def solve_test(self):
        result = hashlib.md5("abcdef609043".encode()).hexdigest()

        self.answer_test = result

    def solve_one(self):
        for i in range(100000, 1000000):
            hashkey = f"{self.input_data}{i}"
            result = hashlib.md5(hashkey.encode()).hexdigest()
            if result[0] == "0" and result[1] == "0" and result[2] == "0" and result[3] == "0" and result[4] == "0":
                self.answer_one = i

    def solve_two(self):
        for i in range(100000, 10000000):
            hashkey = f"{self.input_data}{i}"
            result = hashlib.md5(hashkey.encode()).hexdigest()
            if result[0] == "0" and result[1] == "0" and result[2] == "0" and result[3] == "0" and result[4] == "0" and result[5] == "0":
                self.answer_two = i


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
