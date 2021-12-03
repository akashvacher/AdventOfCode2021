def part1():
    count = 0
    numbers = []
    for line in open("in.txt").read().splitlines():
        numbers.append(int(line))
        if len(numbers) >= 2:
            if numbers[-1] > numbers[-2]:
                count += 1
    print(count)


part1()
