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
        if year == None:
            year = int(input("Year: "))
            if year < 2015 or year > date.today().year:
                year = 2015
        if day == None:
            day = int(input("Day: "))

        path = f"{os.getcwd()}/src/years/year{year}/day{day:02d}"
        shutil.copytree(f"{os.getcwd()}/src/years/year0000/day00", path, dirs_exist_ok=True)

        res = self.session.get(f"https://adventofcode.com/{year}/day/{day}/input", verify=False)
        with (open(f"{path}/input.txt", "w")) as f:
            f.write(res.text)

    def setup(self):
        self.session.cookies.set("session", os.getenv('SESSION_COOKIE'))
