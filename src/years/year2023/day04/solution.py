from src.services.BaseSolution import BaseSolution


# https://adventofcode.com/2023/day/4

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0
        self.answer_one = 0
        self.answer_two = 0
        self.deck = []

    def setup(self):
        self.deck = []

    def get_card(self, line):
        line = line.replace("  ", " ")
        line = line.replace("   ", " ")
        card_info, card_body = line.split(": ")
        card_body_winning_numbers, card_body_scratch_numbers = card_body.split(" | ")
        winning_numbers, scratch_numbers = [], []
        for number in card_body_winning_numbers.split(" "):
            winning_numbers.append(int(number))
        for number in card_body_scratch_numbers.split(" "):
            scratch_numbers.append(int(number))
        card = {
            "id": int(card_info.replace("  ", " ").split(" ")[1]),
            "winning_numbers": winning_numbers,
            "scratch_numbers": scratch_numbers,
            "points": 0
        }

        for number in card["scratch_numbers"]:
            if number in card["winning_numbers"]:
                if card["points"] < 2:
                    card["points"] += 1
                else:
                    card["points"] = card["points"]*2
        self.deck.append(card)
        return card

    def solve_test(self):
        for line in self.input_test_data.splitlines():
            card = self.get_card(line)
            self.answer_test += card["points"]

    def solve_one(self):
        for line in self.input_data.splitlines():
            card = self.get_card(line)
            self.answer_one += card["points"]

    def solve_two(self):
        self.answer_two = ""


if __name__ == "__main__":
    solution = Solution()
    solution.solve(0)
