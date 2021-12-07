def part2():
    positions = list(map(int, open("in.txt").read().strip().split(",")))
    max_x = max(positions)
    ans = None
    for x in range(max_x + 1):
        cost = 0
        for pos in positions:
            n = abs(x - pos)
            cost += (n * (n + 1)) // 2
        ans = cost if ans is None else ans
        ans = min(ans, cost)
    print(ans)


part2()
