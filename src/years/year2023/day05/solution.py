from prettytable import PrettyTable

from src.services.BaseSolution import BaseSolution


# https://adventofcode.com/2023/day/5

def map_line_data(line):
    line = line.split(" ")
    return {
        "destintation": int(line[0]),
        "start": int(line[1]),
        "range": int(line[2]),
        "end": int(line[1]) + int(line[2])
    }


def check_soil(seed, types):
    for index, typ in types.items():
        if typ["start"] <= seed <= typ["end"]:
            typ_destintation = typ["destintation"] + (seed - typ["start"])
            return typ_destintation
    return seed


class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = None
        self.answer_one = None
        self.answer_two = None
        self.seeds = {}
        self.soils = {}
        self.ferilizer = {}
        self.waters = {}
        self.lights = {}
        self.temperatures = {}
        self.humidities = {}
        self.locations = {}

    def setup(self):
        self.seeds = {}
        self.soils = {}
        self.ferilizer = {}
        self.waters = {}
        self.lights = {}
        self.temperatures = {}
        self.humidities = {}
        self.locations = {}

    def get_data(self, input_data):
        seeds = []
        line_type = 0
        for line in input_data.splitlines():
            # print(line)
            if line == "":
                continue
            if "seeds:" in line:
                seeds = line.split(" ")[1:]
            if "seed-to-soil" in line:
                line_type = 1
                continue
            if "soil-to-fertilizer" in line:
                line_type = 2
                continue
            if "fertilizer-to-water" in line:
                line_type = 3
                continue
            if "water-to-light" in line:
                line_type = 4
                continue
            if "light-to-temperature" in line:
                line_type = 5
                continue
            if "temperature-to-humidity" in line:
                line_type = 6
                continue
            if "humidity-to-location" in line:
                line_type = 7
                continue

            if line_type == 1:  # "seed-to-soil"
                soil = map_line_data(line)
                self.soils[soil["destintation"]] = soil
            if line_type == 2:  # "soil-to-fertilizer"
                ferilizer = map_line_data(line)
                self.ferilizer[ferilizer["destintation"]] = ferilizer
            if line_type == 3:  # "fertilizer-to-water"
                water = map_line_data(line)
                self.waters[water["destintation"]] = water
            if line_type == 4:  # "water-to-light"
                light = map_line_data(line)
                self.lights[light["destintation"]] = light
            if line_type == 5:  # "light-to-temperature"
                temperature = map_line_data(line)
                self.temperatures[temperature["destintation"]] = temperature
            if line_type == 6:  # "temperature-to-humidity"
                humidity = map_line_data(line)
                self.humidities[humidity["destintation"]] = humidity
            if line_type == 7:  # "humidity-to-location"
                location = map_line_data(line)
                self.locations[location["destintation"]] = location

        for seed in seeds:
            seed = int(seed)
            soil = check_soil(seed, self.soils)
            ferilizer = check_soil(soil, self.ferilizer)
            water = check_soil(ferilizer, self.waters)
            light = check_soil(water, self.lights)
            temperature = check_soil(light, self.temperatures)
            humidity = check_soil(temperature, self.humidities)
            location = check_soil(humidity, self.locations)
            self.seeds[int(seed)] = {
                "soil": soil,
                "fertilizer": ferilizer,
                "water": water,
                "light": light,
                "temperature": temperature,
                "humidity": humidity,
                "location": location
            }

    def show_table(self):
        table = PrettyTable()
        table.field_names = ["Seed", "Soil", "Fertilizer", "Water", "Light", "Temperature", "Humidity", "Location"]
        for seed, data in self.seeds.items():
            table.add_row([
                seed,
                data["soil"],
                data["fertilizer"],
                data["water"],
                data["light"],
                data["temperature"],
                data["humidity"],
                data["location"]
            ])
        print(table)

    def solve_test(self):
        self.get_data(self.input_test_data)
        for seed, data in self.seeds.items():
            if self.answer_test is None:
                self.answer_test = data["location"]
            if data["location"] < self.answer_test:
                self.answer_test = data["location"]
        self.show_table()

    def solve_one(self):
        self.get_data(self.input_data)
        for seed, data in self.seeds.items():
            if self.answer_one is None or data["location"] < self.answer_one:
                self.answer_one = data["location"]

    def solve_two(self):
        self.answer_two = ""


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
