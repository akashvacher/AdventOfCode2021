def tick(nums):
    """
    Simulate one tick of passage of time
    nums is a list of timer counts of all fish
    """
    # Iterate over a copy of nums as it will be modified within the loop
    for i, j in enumerate(nums[:]):
        if j == 0:
            nums[i] = 6
            nums.append(8)
        else:
            nums[i] -= 1
    return nums


def part1():
    nums = list(map(int, open("in.txt").read().strip().split(",")))
    for i in range(80):
        nums = tick(nums)
    print(len(nums))


part1()
