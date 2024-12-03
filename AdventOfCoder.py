import os
import shutil
from datetime import date

import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup


class AdventOfCoder:
    def __init__(self, is_work=False):
        """
        Initializes the AdventOfCoder class.

        :param is_work: Boolean flag to determine which session cookie to use.
        """
        load_dotenv()
        self.is_work = is_work
        self.current_path = os.getcwd()
        self.session = requests.Session()
        self.setup()

    def get_day(self, year=None, day=None):
        """
        Sets up the directory and files for a specific day of Advent of Code.

        :param year: The year of the Advent of Code event.
        :param day: The day of the Advent of Code event.
        """
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
        content = content.replace("# https://adventofcode.com/0000/day/00",
                                  f"# https://adventofcode.com/{year}/day/{day}")
        with(open(f"{path}/solution.py", "w")) as f:
            f.write(content)

        input_data = self.session.get(f"https://adventofcode.com/{year}/day/{day}/input", verify=False)
        with (open(f"{path}/input.txt", "w")) as f:
            f.write(input_data.text)

        description = self.get_task_description(year, day)
        with (open(f"{path}/description.txt", "w")) as f:
            f.write(description)

    def setup(self):
        """
        Sets up the session with the appropriate session cookie.
        """
        if self.is_work:
            self.session.cookies.set("session", os.getenv('SESSION_COOKIE'))
        else:
            self.session.cookies.set("session", os.getenv('SESSION_COOKIE_PRIVATE'))

    def get_input_data(self, year, day):
        """
        Fetches the input data for a specific day of Advent of Code.

        :param year: The year of the Advent of Code event.
        :param day: The day of the Advent of Code event.
        """
        path = f"{os.getcwd()}/src/years/year{year}/day{day:02d}"
        res = self.session.get(f"https://adventofcode.com/{year}/day/{day}/input", verify=False)
        with(open(f"{path}/input.txt", "w")) as f:
            f.write(res.text)

    def get_task_description(self, year, day):
        """
        Fetches the task description for a specific day of Advent of Code.

        :param year: The year of the Advent of Code event.
        :param day: The day of the Advent of Code event.
        :return: The task description as a string.
        """
        url = f"https://adventofcode.com/{year}/day/{day}"
        res = self.session.get(url, verify=False)
        soup = BeautifulSoup(res.text, 'html.parser')
        description = soup.find('article', class_='day-desc').text

        # Add a newline after the second occurrence of "---"
        parts = description.split('---', 2)
        if len(parts) > 2:
            description = '---'.join(parts[:2]) + '---\n' + parts[2]

        return description