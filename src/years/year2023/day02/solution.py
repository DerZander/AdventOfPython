from prettytable import PrettyTable

from src.services.BaseSolution import BaseSolution


# https://adventofcode.com/2023/day/2

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0
        self.answer_one = 0
        self.answer_two = 0
        self.max_cubes = {"red": 12, "green": 13, "blue": 14}
        self.games = []
        self.table = PrettyTable()
        self.table.field_names = ["Game", "Round", "Red", "Green", "Blue"]

    def setup(self):
        self.games = []

    def load_games(self, lines):
        for line in lines.splitlines():
            game = {
                "id": int(line.split(":")[0].split(" ")[1]),
                "is_possible": True,
                "rounds": [],
                "max_round": {
                    "red": 0,
                    "green": 0,
                    "blue": 0
                },
                "possible_rounds": 0
            }
            round_info = line.split(":")[1]
            rounds = round_info.split(";")
            for gr in rounds:
                game_round = {"is_possible": True, "blue": 0, "green": 0, "red": 0}
                for r in gr.split(","):
                    game_round[r.split(" ")[2]] = int(r.split(" ")[1])
                for color, cubes in game_round.items():
                    if color == "is_possible":
                        continue
                    if cubes > self.max_cubes[color]:
                        game_round["is_possible"] = False
                        game["is_possible"] = False
                game["rounds"].append(game_round)
                if game_round["red"] > game["max_round"]["red"]:
                    game["max_round"]["red"] = game_round["red"]
                if game_round["green"] > game["max_round"]["green"]:
                    game["max_round"]["green"] = game_round["green"]
                if game_round["blue"] > game["max_round"]["blue"]:
                    game["max_round"]["blue"] = game_round["blue"]

                self.table.add_row([game["id"], len(game["rounds"]), game_round["red"], game_round["green"],
                                    game_round["blue"]])
            if game["is_possible"]:
                for r in game["rounds"]:
                    if r["is_possible"]:
                        game["possible_rounds"] += 1

            self.games.append(game)

    def solve_test(self):
        self.load_games(self.input_test_data)
        for game in self.games:
            max_value = game["max_round"]["red"] * game["max_round"]["green"] * game["max_round"]["blue"]
            self.answer_test += max_value

    def solve_one(self):
        self.load_games(self.input_data)
        for game in self.games:
            if game["is_possible"]:
                self.answer_one += game['id']

    def solve_two(self):
        self.load_games(self.input_data)
        for game in self.games:
            max_value = game["max_round"]["red"] * game["max_round"]["green"] * game["max_round"]["blue"]
            self.answer_two += max_value
        # self.answer_two = ""


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
