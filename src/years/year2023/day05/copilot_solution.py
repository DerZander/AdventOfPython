import itertools


def row2int(row: str) -> list[int]:
    return list(map(int, row.strip().split(' ')))


def rows2list(fd):
    l = []
    for row in fd:
        if not row.strip():
            break
        l.append(row2int(row))
    return l


def do_overlap(x_start, x_len, y_start, y_len):
    return x_start <= y_len and y_start <= x_len


def bubble_wise(l):
    for i in range(0, len(l) - 1, 2):
        yield l[i], l[i+1]


def abs_range(pair):
    return pair[0], sum(pair)


def iter_map(map):
    for x, y, z in map:
        yield x, y, z, y+z


def remember_left_overlap(start, end, source_range_start, remaining_seeds):
    left_i, left_j = min(start, source_range_start), min(end, source_range_start)
    if left_i < left_j:
        print(f'Hangover (left): [{left_i}, {left_j}]')
        remaining_seeds.append((left_i, left_j - 1))


def remember_right_overlap(end, source_range_end, remaining_seeds):
    right_i, right_j = max(end, source_range_end), max(end, source_range_end)
    if right_i < right_j:
        print(f'Hangover (right): [{right_i}, {right_j}]')
        remaining_seeds.append((right_i, right_j - 1))


def transform_intersection(start, end, source_range_start, source_range_end, destination_range_start):
    overlap_i, overlap_j = max(start, source_range_start), min(end, source_range_end)
    if overlap_i < overlap_j:
        offset = destination_range_start - source_range_start
        new_i, new_j = overlap_i + offset, overlap_j+offset
        print(f'Overlap: [{overlap_i}, {overlap_j}] ~~> [{new_i}, {new_j}]')
        return new_i, new_j


def find_locations(seed_ranges, maps):
    # General Idea
    # ------------
    # Iterate over every seed-range "from top to bottom".
    # Check for every map (seed-to-soil, soil-to-fertilizer, ...) if we have to
    # convert numbers from a source category into numbers in a destination category.
    # There are only two cases (for every map):
    #   1. There is a line to describes how to convert a source num to a destination num
    #   2. Source numbers aren't mapped
    #
    # In the first case, the source range needs to be converted into a
    # destination range based in the destination-range-start.
    #
    # In the second case, nothing needs to be converted, because the same source
    # maps to the same destination (e.g. seed 10 maps to soil 10).
    #
    # This basically means, that is is enough to perform four checks for every line
    # in every map ("from top to bottom"):
    #   1. Get the range of source numbers that are smaller then the source-range-start ("overlap to the left")
    #   2. Get the range of source numbers that are greater then the source-range-end ("overlap to the right")
    #   3. Get the range of source numbers that are mapped and transform them based on the destination-range-start
    #   4. Leave the source range as it is, if there is no mapping
    for pair in bubble_wise(seed_ranges):
        remaining_seeds = [abs_range(pair)]
        temp = []
        for mp in maps:
            while len(remaining_seeds) > 0:
                (start, end), found_any = remaining_seeds.pop(), False
                print('---')
                for sd, ss, _, se in iter_map(mp):
                    if do_overlap(start, end, ss, se):
                        found_any = True

                        # Does the seed range overlap on the left?
                        # [1,2,3,4,5]
                        #       [4,5,6,7,8]
                        # [1,2,3]               <-- this remains
                        remember_left_overlap(start, end, ss, remaining_seeds)

                        # Does the seed range overlap on the right?
                        #       [4,5,6,7,8]
                        # [1,2,3,4,5]
                        #           [6,7,8]     <-- this remains
                        remember_right_overlap(end, se, remaining_seeds)

                        # Interection of both ranges ("a perfect overlap")
                        # [1,2,3,4,5]
                        #       [4,5,6,7,8]
                        #       [4,5]           <-- this overlaps
                        new_i, new_j = transform_intersection(start, end, ss, se, sd)
                        temp.append((new_i, new_j))
                    else:
                        # [1,2,3,4,5]
                        #             [6,7,8,9,10]
                        print(f'No Overlap: [{start}, {end}] vs. [{ss}, {se}]')
                        continue
                if not found_any:
                    temp.append((start, end))

            remaining_seeds, temp = temp, []

        yield remaining_seeds


def parse_almanac(path: str):
    with open(path) as fd:
        for i, line in enumerate(fd):
            if i == 0:
                seeds = row2int(line.removeprefix('seeds:'))
            elif line.startswith('seed-to-soil'):
                seed_to_soil = rows2list(fd)
            elif line.startswith('soil-to-fertilizer'):
                soil_to_fertilizer = rows2list(fd)
            elif line.startswith('fertilizer-to-water'):
                fertilizer_to_water = rows2list(fd)
            elif line.startswith('water-to-light'):
                water_to_light = rows2list(fd)
            elif line.startswith('light-to-temperature'):
                light_to_temperature = rows2list(fd)
            elif line.startswith('temperature-to-humidity'):
                temperature_to_humidity = rows2list(fd)
            elif line.startswith('humidity-to-location'):
                humidity_to_location = rows2list(fd)
            else:
                pass

        return seeds, [
            seed_to_soil,
            soil_to_fertilizer,
            fertilizer_to_water,
            water_to_light,
            light_to_temperature,
            temperature_to_humidity,
            humidity_to_location
        ]


if __name__ == '__main__':
    seed_ranges, maps = parse_almanac('./input.txt')
    # seed_ranges, maps = parse_almanac('./map.txt.orig')

    locations = itertools.chain.from_iterable(find_locations(seed_ranges, maps))
    locations_sorted = sorted(locations, key=lambda x: x[0])
    smallest_loc = locations_sorted[0][0]

    print('28580589 and got', smallest_loc, )
    assert 28580589 == smallest_loc, "WRONG!!!! :("