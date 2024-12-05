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
        self.updates = []
        self.correct_updates = []
        self.status = {"correct":0, "wrong":0}


    def setup(self):
        if self.current_solution == SOLUTIONS.TEST:
            self.data = self.input_test_data
        elif self.current_solution == SOLUTIONS.ONE:
            self.status = {"correct": 0, "wrong": 0}
            self.data = self.input_data
        elif self.current_solution == SOLUTIONS.TWO:
            self.status = {"correct": 0, "wrong": 0}
            self.data = self.input_data
        pass

    # def get_rules_and_updates(self):
    #     # setup
    #     self.rules = {}
    #     self.updates = []
    #     self.correct_updates = []
    #
    #     #generate
    #     for line in open(self.input_file, "r").readlines():
    #         line = line.strip()
    #         if "|" in line:
    #             key = int(line.split("|")[0].strip())
    #             if self.rules.get(key) is None:
    #                 self.rules[key] = []
    #             self.rules[key].append(int(line.split("|")[1].strip()))
    #         elif "," in line:
    #             self.updates.append([int(i) for i in line.split(",")])
    #     print(self.rules)
    #     print(self.updates)
    def get_rules_and_updates(self):
        # setup
        self.rules = []
        self.updates = []
        self.correct_updates = []

        #generate
        for line in open(self.input_file, "r").readlines():
            line = line.strip()
            if "|" in line:
                left, right = line.split("|")
                self.rules.append([int(left), int(right)])
            elif "," in line:
                self.updates.append([int(i) for i in line.split(",")])


    def check_update_with_rule(self,  update_set):
        counter = 0
        for update_id, update in enumerate(update_set):
            for rule in self.rules:
                if update in rule:
                    for next_update_id, next_update in enumerate(update_set):
                        if next_update_id > update_id:
                            if next_update in rule:

                                if rule[0] == update:
                                    if update_id > next_update_id:
                                        counter +=1
                                        self.status["wrong"] += 1
                                        return False
                                elif rule[1] == update:
                                    if update_id < next_update_id:
                                        counter += 1
                                        self.status["wrong"] += 1
                                        return False
        self.status["correct"] += 1
        return True

    def get_correctly_orderd_updates(self):
        self.correct_updates = []
        for update_set in self.updates:
            if self.check_update_with_rule(update_set):
                self.correct_updates.append(update_set)


    def sum_middle_pages(self, update_list =None):
        if update_list is None:
            update_list = self.correct_updates
        result = 0
        for update_set in update_list:
            middle_index = len(update_set) // 2
            result += update_set[middle_index]
        return result

    def order_updates(self):
        ordered_updates =[]
        for update_set in self.updates:
            ordered_set = []
            remaining_set = update_set[:]

            while remaining_set:
                for update in remaining_set:
                    can_add = True
                    for rule in self.rules:
                        if update == rule[1] and rule[0] in remaining_set:
                            can_add = False
                            break
                    if can_add:
                        ordered_set.append(update)
                        remaining_set.remove(update)
                        break
            ordered_updates.append(ordered_set)

        sub_len = len(self.correct_updates)
        for i in range(len(ordered_updates) - sub_len + 1):
            if ordered_updates[i:i + sub_len] == self.correct_updates:
                del ordered_updates[i:i + sub_len]
                break
        return ordered_updates




    @timer
    def solve_test(self):
        self.get_rules_and_updates()
        self.get_correctly_orderd_updates()
        ordered_updates = self.order_updates()
        print(ordered_updates)
        print(self.status)
        self.answer_test = self.sum_middle_pages(ordered_updates)
        pass

    @timer
    def solve_one(self):
        self.get_rules_and_updates()
        self.get_correctly_orderd_updates()
        self.answer_one = self.sum_middle_pages()
        pass

    @timer
    def solve_two(self):
        self.get_rules_and_updates()
        self.get_correctly_orderd_updates()
        ordered_updates = self.order_updates()
        print(self.status)
        self.answer_two = self.sum_middle_pages(ordered_updates)
        # 11466 too high


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
