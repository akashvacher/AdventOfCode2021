def part1():
    x, y = 0, 0
    for line in open("in.txt").read().splitlines():
        direction, num = line.split()
        num = int(num)
        if direction == "forward":
            x += num
        elif direction == "down":
            y += num
        elif direction == "up":
            y -= num
    print(x * y)


part1()
