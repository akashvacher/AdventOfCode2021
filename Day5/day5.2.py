from collections import Counter


def part2():
    lines = open("in.txt").read().splitlines()
    segments = []
    for line in lines:
        a, b = [list(map(int, i.split(","))) for i in line.split(" -> ")]
        if a[0] == b[0] or a[1] == b[1] or abs(a[0] - b[0]) == abs(a[1] - b[1]):
            segments.append((*a, *b))

    # Make a chart to keep track of all dangerous points
    chart = {}
    for segment in segments:
        x1, y1, x2, y2 = segment
        while (x1, y1) != (x2, y2):
            # Mark point (x1, y1) in the chart
            chart[(x1, y1)] = chart.get((x1, y1), 0) + 1

            # Move x1 closer to x2 if possible
            if x1 != x2:
                if abs(x2 - (x1 + 1)) < abs(x2 - (x1 - 1)):
                    x1 += 1
                else:
                    x1 -= 1
            # Move y1 closer to y2 if possible
            if y1 != y2:
                if abs(y2 - (y1 + 1)) < abs(y2 - (y1 - 1)):
                    y1 += 1
                else:
                    y1 -= 1

        # Add point 2 to our chart as well
        chart[(x2, y2)] = chart.get((x2, y2), 0) + 1

    danger_distribution = Counter(chart.values())
    # Ignore all points with danger rating of 1
    del danger_distribution[1]
    # print the number of all the other dangerous points
    print(sum(danger_distribution.values()))


part2()
