import os
import shutil
from datetime import date

import requests
from dotenv import load_dotenv


class AdventOfCoder:
    def __init__(self):
        load_dotenv()
        self.current_path = os.getcwd()
        self.session = requests.Session()
        self.setup()

    def get_day(self, year=None, day=None):
        if year is None:
            year = int(input("Year: "))
            if year < 2015 or year > date.today().year:
                year = 2015
        if day is None:
            day = int(input("Day: "))

        path = f"{os.getcwd()}/src/years/year{year}/day{day:02d}"
        shutil.copytree(f"{os.getcwd()}/src/years/year0000/day00", path, dirs_exist_ok=True)
        with (open(f"{path}/solution.py", "r")) as f:
            content = f.read()
        content = content.replace("# https://adventofcode.com/0000/day/00", f"# https://adventofcode.com/{year}/day/{day}")
        with(open(f"{path}/solution.py", "w")) as f:
            f.write(content)

        res = self.session.get(f"https://adventofcode.com/{year}/day/{day}/input", verify=False)
        with (open(f"{path}/input.txt", "w")) as f:
            f.write(res.text)

    def setup(self):
        self.session.cookies.set("session", os.getenv('SESSION_COOKIE'))
