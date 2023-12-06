import numpy
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


def check_action(destination, types):
    for index, typ in types.items():
        if typ["start"] <= destination <= typ["end"]:
            typ_destintation = typ["destintation"] + (destination - typ["start"])
            return typ_destintation
    return destination


class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        self.answer_test = None
        self.answer_one = None
        self.answer_two = None
        self.seeds = {}
        self.ranged_seeds = []
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

    def get_ranged_seeds(self, input_data):
        seeds = []
        for line in input_data.splitlines():
            if line == "":
                continue
            if "seeds:" in line:
                for s in line.split(" ")[1:]:
                    seeds.append(int(s))
        x, y = 0, 1
        for i in range(0, int(len(seeds) / 2)):
            for j in range(seeds[x], seeds[x] + seeds[y]):
                print(j)
                self.ranged_seeds.append(j)
            x += 2
            y += 2

    def get_seeds(self, input_data):
        for line in input_data.splitlines():
            if line == "":
                continue
            if "seeds:" in line:
                for seed in line.split(" ")[1:]:
                    self.seeds[int(seed)] = {
                        "soil": 0,
                        "fertilizer": 0,
                        "water": 0,
                        "light": 0,
                        "temperature": 0,
                        "humidity": 0,
                        "location": 0
                    }

    def get_data(self, input_data):
        line_type = 0
        for line in input_data.splitlines():
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
            if line == "" or line_type == 0:
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

    def get_location(self, seed):
        soil = check_action(seed, self.soils)
        ferilizer = check_action(soil, self.ferilizer)
        water = check_action(ferilizer, self.waters)
        light = check_action(water, self.lights)
        temperature = check_action(light, self.temperatures)
        humidity = check_action(temperature, self.humidities)
        return check_action(humidity, self.locations)

    def solve_test(self):
        self.get_ranged_seeds(self.input_test_data)
        self.get_data(self.input_test_data)
        for seed in self.ranged_seeds:
            if self.answer_test is None or self.get_location(seed) < self.answer_test:
                self.answer_test = self.get_location(seed)
        # for seed, data in self.seeds.items():
        #     if self.answer_test is None or data["location"] < self.answer_test:
        #         self.answer_test = data["location"]

    def solve_one(self):  # 265018614
        self.get_seeds(self.input_data)
        self.get_data(self.input_data)

        for seed in self.seeds:
            seed = int(seed)
            soil = check_action(seed, self.soils)
            ferilizer = check_action(soil, self.ferilizer)
            water = check_action(ferilizer, self.waters)
            light = check_action(water, self.lights)
            temperature = check_action(light, self.temperatures)
            humidity = check_action(temperature, self.humidities)
            location = check_action(humidity, self.locations)
            self.seeds[int(seed)] = {
                "soil": soil,
                "fertilizer": ferilizer,
                "water": water,
                "light": light,
                "temperature": temperature,
                "humidity": humidity,
                "location": location
            }

        for seed, data in self.seeds.items():
            if self.answer_one is None or data["location"] < self.answer_one:
                self.answer_one = data["location"]

    def solve_two(self):
        self.get_data(self.input_data)
        seeds = []
        for line in self.input_data.splitlines():
            if line == "":
                continue
            if "seeds:" in line:
                for s in line.split(" ")[1:]:
                    seeds.append(int(s))
        x, y = 0, 1

        seed_list = numpy.arange(seeds[x], seeds[x] + seeds[y])

        for i in range(0, int(len(seeds) / 2)):
            for seed in numpy.arange(seeds[i * 2], seeds[i * 2] + seeds[i + 1 * 2]):
                print(seed)
                if self.answer_two is None or self.get_location(seed) < self.answer_two:
                    self.answer_two = self.get_location(seed)


if __name__ == "__main__":
    solution = Solution()
    solution.solve()
