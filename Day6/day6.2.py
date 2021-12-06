from collections import Counter


def tick(nums):
    """
    Simulate one tick of passage of time
    nums is a frequency dict of all fish counted by their timer count
    """
    new_nums = {}
    for k, v in nums.items():
        if k == 0:
            new_nums[6] = new_nums.get(6, 0) + v
            new_nums[8] = new_nums.get(8, 0) + v
            continue
        new_nums[k - 1] = new_nums.get(k - 1, 0) + v
    return new_nums


def part2():
    nums = list(map(int, open("in.txt").read().strip().split(",")))
    nums = Counter(nums)
    for _ in range(256):
        nums = tick(nums)
    print(sum(nums.values()))


part2()
