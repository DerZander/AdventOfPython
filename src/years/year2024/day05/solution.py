from src.services.BaseSolution import BaseSolution, timer, SOLUTIONS


# https://adventofcode.com/2024/day/5

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0
        self.answer_one = 0
        self.answer_two = 0
        self.data = None
        self.rules = []
        self.sequences = []
        self.wrong_sequences = []


    def setup(self):
        if self.current_solution == SOLUTIONS.TEST:
            self.data = self.input_test_data
        elif self.current_solution == SOLUTIONS.ONE:
            self.data = self.input_data
        elif self.current_solution == SOLUTIONS.TWO:
            self.data = self.input_data
        pass

    def get_sequence_and_rules(self):
        self.rules = []
        self.sequences = []
        self.wrong_sequences = []
        is_rule = True
        file = open(self.input_file, "r")

        line = file.readline()

        while line != "":
            if line == "\n":
                is_rule = False
                line = file.readline()
                continue
            if is_rule:
                rule = (int(line.split("|")[0]), int(line.split("|")[1]))
                self.rules.append(rule)
            else:
                self.sequences.append(list(map(int, line.split(","))))
            line = file.readline()

    def get_middle_sum_of_correct_sequences(self):
        total = 0
        for sequence in self.sequences:
            all_good = True
            for rule in self.rules:
                if rule[0] in sequence and rule[1] in sequence:
                    first_ix = sequence.index(rule[0])
                    second_ix = sequence.index(rule[1])
                    if first_ix > second_ix:
                        all_good = False

            if all_good:
                middle_num = sequence[len(sequence)//2]
                total += middle_num
            else:
                self.wrong_sequences.append(sequence)
        return total

    def correct_wrong_sequences(self):
        changes = True
        while changes:
            changes = False
            for i, sequence in enumerate(self.wrong_sequences):
                for rule in self.rules:
                    first_ix = 0
                    second_ix = 0
                    if rule[0] in sequence and rule[1] in sequence:
                        first_ix = sequence.index(rule[0])
                        second_ix = sequence.index(rule[1])
                        if first_ix > second_ix:
                            self.wrong_sequences[i][first_ix], self.wrong_sequences[i][second_ix] = self.wrong_sequences[i][second_ix], self.wrong_sequences[i][first_ix]
                            changes = True
                            sequence = self.wrong_sequences[i]
        total = 0
        for sequence in self.wrong_sequences:
            middle_num = sequence[len(sequence) // 2]
            total += middle_num
        return total

    @timer
    def solve_test(self):
        self.get_sequence_and_rules()
        self.answer_test = self.get_middle_sum_of_correct_sequences()

    @timer
    def solve_one(self):
        self.get_sequence_and_rules()
        self.answer_one = self.get_middle_sum_of_correct_sequences()

    @timer
    def solve_two(self):
        self.get_sequence_and_rules()
        self.get_middle_sum_of_correct_sequences()
        self.answer_two = self.correct_wrong_sequences()


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
