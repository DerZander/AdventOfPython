from datetime import datetime

from AdventOfCoder import AdventOfCoder

if __name__ == "__main__":
    aoc = AdventOfCoder(is_work=True)
    current_day = datetime.now().date().day
    aoc.get_day(2024, current_day)
    # aoc.get_day(2024, 11)
