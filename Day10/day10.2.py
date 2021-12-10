from statistics import median


def score(ch):
    return {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }[ch]


def process(line):
    stack = []
    for i in line:
        if i in {'(', '{', '[', '<'}:
            stack.append(i)
            continue
        if len(stack) == 0:
            # Underflow - example would be when the line is ")[]{}"
            # in this case, the stack is empty - the line is corrupt
            return None
        tail = stack.pop()
        if tail+i in ['()', '{}', '[]', '<>']:
            continue
        else:
            # Corrupt line detected
            return None
    chars_to_add = reversed(''.join(stack).replace('<', '>').replace(
        '(', ')').replace('[', ']').replace('{', '}'))
    line_score = 0
    for i in chars_to_add:
        line_score = line_score*5 + score(i)
    return line_score


def part2():
    lines = open("in.txt").read().strip().splitlines()
    scores = []
    for line in lines:
        ans = process(line)
        if ans:
            scores.append(ans)
    print(median(scores))


part2()
