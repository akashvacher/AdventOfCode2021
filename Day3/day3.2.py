from collections import Counter


def part2():
    all_lines = open("in.txt").read().splitlines()

    # Get oxygen_rating
    lines = all_lines[:]
    i = 0
    while len(lines) > 1:
        bits = Counter(line[i] for line in lines)
        if bits["1"] >= bits["0"]:
            lines = [line for line in lines if line[i] == "1"]
        elif bits["1"] < bits["0"]:
            lines = [line for line in lines if line[i] == "0"]
        i += 1
    # There should only be one line remaining after pruning
    assert len(lines) == 1
    oxygen_rating = int(lines[0], 2)

    # Get co2_rating
    lines = all_lines[:]
    i = 0
    while len(lines) > 1:
        bits = Counter(line[i] for line in lines)
        if bits["1"] >= bits["0"]:
            lines = [line for line in lines if line[i] == "0"]
        elif bits["1"] < bits["0"]:
            lines = [line for line in lines if line[i] == "1"]
        i += 1
    # There should only be one line remaining after pruning
    assert len(lines) == 1
    co2_rating = int(lines[0], 2)

    print(oxygen_rating * co2_rating)


part2()
