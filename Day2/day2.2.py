def part2():
    x, y, aim = 0, 0, 0
    for line in open("in.txt").read().splitlines():
        direction, num = line.split()
        num = int(num)
        if direction == "forward":
            x += num
            y += aim * num
        elif direction == "down":
            aim += num
        elif direction == "up":
            aim -= num
    print(x * y)


part2()
