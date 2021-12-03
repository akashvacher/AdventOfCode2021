from collections import Counter


def part1():
    lines = open("in.txt").read().splitlines()
    width = len(lines[0])  # Get the bit width for gamma and epsilon
    gamma, epsilon = "", ""
    for i in range(width):
        bits = Counter(line[i] for line in lines)
        if bits["0"] > bits["1"]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)

    print(gamma * epsilon)


part1()
