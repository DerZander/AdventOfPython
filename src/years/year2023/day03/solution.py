import re

from src.services.BaseSolution import BaseSolution


# https://adventofcode.com/2023/day/3


class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = 0
        self.answer_one = 0
        self.answer_two = 0
        self.pattern = r'^[.\d]+$'

    # def solve_test(self):        

    def solve_one(self):  # 546312
        sum = 0
        with open("input.txt") as f:
            lines = f.readlines()
            for line_index, curr_line in enumerate(lines):
                curr_line = ''.join(curr_line)
                digit_start_pos = None
                digit_end_pos = None

                if line_index == 0:
                    prev_line = curr_line
                if line_index >= len(lines) - 1:
                    next_line = curr_line
                else:
                    next_line = lines[line_index + 1]

                for pos, c in enumerate(curr_line):

                    # start of sequence
                    if c.isdigit() and digit_start_pos is None:
                        digit_start_pos = pos
                        digit_end_pos = pos

                    # currently in sequence
                    elif c.isdigit() and digit_start_pos is not None:
                        digit_end_pos = pos

                    # end of sequence
                    elif not c.isdigit() and digit_start_pos is not None:

                        if digit_start_pos > 0:
                            tmp = digit_start_pos - 1
                        else:
                            tmp = 0

                        # now check for symbols in sequence surroundings, same for prev and next sequence
                        if not bool(re.match(self.pattern, curr_line[tmp:digit_end_pos + 2])) or \
                                not bool(re.match(self.pattern, prev_line[tmp:digit_end_pos + 2])) or \
                                not bool(re.match(self.pattern, next_line[tmp:digit_end_pos + 2])):
                            part_number = ''.join(curr_line[digit_start_pos:digit_end_pos + 1])
                            sum += int(part_number)

                        digit_start_pos = None
                        digit_end_pos = None

                prev_line = curr_line
        self.answer_one = sum

    def go_forwards(self, line, start=0):
        part_number = ""
        for c in line[start:]:
            if c.isdigit():
                part_number = part_number + c
            else:
                break
        return part_number

    def go_backwards(self, line, end=0):
        part_number = ""
        for c in reversed(line[:end]):
            if c.isdigit():
                part_number = part_number + c
            else:
                break
        return part_number[::-1]

    def solve_two(self):
        self.pattern = r"\d+"
        lines = self.input_data.splitlines()
        sum = 0
        for line_index, curr_line in enumerate(lines):
            curr_line = "".join(curr_line.strip())

            if line_index == 0:
                prev_line = curr_line
            if line_index >= len(lines) - 1:
                next_line = curr_line
            else:
                next_line = lines[line_index + 1]

            for pos, char in enumerate(curr_line):
                if char == "*":
                    connections = 0
                    if curr_line[pos - 1].isdigit():
                        connections += 1
                    if curr_line[pos + 1].isdigit():
                        connections += 1
                    connections += len(re.findall(self.pattern, prev_line[pos - 1:pos + 2]))
                    connections += len(re.findall(self.pattern, next_line[pos - 1:pos + 2]))

                    if connections != 2:
                        continue
                    part_numbers = list()
                    if curr_line[pos - 1].isdigit():
                        part_numbers.append(self.go_backwards(curr_line, end=pos))
                    if curr_line[pos + 1].isdigit():
                        part_numbers.append(self.go_forwards(curr_line, start=pos + 1))

                    if prev_line[pos].isdigit():
                        part_numbers.append(
                            self.go_backwards(prev_line, end=pos + 1)
                            + self.go_forwards(prev_line, start=pos + 1)
                        )
                    else:
                        if prev_line[pos - 1].isdigit():
                            part_numbers.append(self.go_backwards(prev_line, end=pos))
                        if prev_line[pos + 1].isdigit():
                            part_numbers.append(self.go_forwards(prev_line, start=pos + 1))

                    if next_line[pos].isdigit():
                        part_numbers.append(
                            self.go_backwards(next_line, end=pos + 1)
                            + self.go_forwards(next_line, start=pos + 1)
                        )
                    else:
                        if next_line[pos - 1].isdigit():
                            part_numbers.append(self.go_backwards(next_line, end=pos))
                        if next_line[pos + 1].isdigit():
                            part_numbers.append(self.go_forwards(next_line, start=pos + 1))
                    sum += int(part_numbers[0]) * int(part_numbers[1])
            prev_line = curr_line
        self.answer_two = sum


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
