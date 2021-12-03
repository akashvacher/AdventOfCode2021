def part2():
    count = 0
    numbers = []
    for line in open("in.txt").read().splitlines():
        numbers.append(int(line))
        if len(numbers) >= 4:
            if numbers[-1] > numbers[-4]:
                count += 1
    print(count)


part2()
