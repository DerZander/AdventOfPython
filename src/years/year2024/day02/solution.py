from src.services.BaseSolution import BaseSolution, timer, SOLUTIONS


# https://adventofcode.com/2024/day/2

class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0
        self.answer_one = 0
        self.answer_two = 0
        self.data = None

    def setup(self):
        if self.current_solution == SOLUTIONS.TEST:
            self.data = self.input_test_data
        elif self.current_solution == SOLUTIONS.ONE:
            self.data = self.input_data
        elif self.current_solution == SOLUTIONS.TWO:
            self.data = self.input_data
        pass


    def get_reports(self):
        reports = []
        for line in open(self.input_file, "r").readlines():
            report = []
            for level in line.strip().split(" "):
                report.append(int(level))
            reports.append(report)
        return reports

    def check_report_is_safe(self, report):
        direction = 0
        for i,level in enumerate(report[:-1]):
            if level > report[i+1]:
                if level - report[i+1] > 3:
                    return False
                if direction == 0 or direction == -1:
                    direction = -1
                else:
                    return False
            if level < report[i+1]:
                if report[i+1] - level > 3:
                    return False
                if direction == 0 or direction == 1:
                    direction = 1
                else:
                    return False
            if level == report[i+1]:
                return False
        return True



    @timer
    def solve_test(self):
        reports = self.get_reports()
        counter = 0
        for report in reports:
            print(report)
            if self.check_report_is_safe(report):
                counter += 1
        self.answer_test =counter

    @timer
    def solve_one(self):
        reports = self.get_reports()
        counter = 0
        for report in reports:
            print(report)
            if self.check_report_is_safe(report):
                counter += 1
        self.answer_one = counter

    @timer
    def solve_two(self):
        self.answer_two = ""


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
