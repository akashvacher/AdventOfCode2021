def score(ch):
    return {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }[ch]


def process(line):
    s = []
    for i in line:
        if i in {'(', '{', '[', '<'}:
            s.append(i)
            continue
        if len(s) == 0:
            # Underflow - example would be when the line is ")[]{}"
            # in this case, the stack is empty, and the score should be counted by
            # the first bad character (in this case, ")")
            return score(i)
        else:
            tail = s.pop()
            if tail+i in ['()', '{}', '[]', '<>']:
                continue
            else:
                return score(i)
    # An incomplete line contributes 0 to the total score
    return 0


def part1():
    lines = open("in.txt").read().strip().splitlines()
    count = 0
    for line in lines:
        ans = process(line.strip())
        count += ans
    print(count)


part1()
