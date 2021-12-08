def part1():
    lines = open("in.txt").read().strip().splitlines()
    count = 0
    for line in lines:
        _, right = line.split(" | ")
        right = right.split()
        for i in right:
            if len(i) in {2, 3, 4, 7}:
                count += 1
    print(count)


part1()
