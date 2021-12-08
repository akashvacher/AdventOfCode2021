from itertools import permutations


def translate_to_num(string, permutation):
    '''
    Assuming that the permutation is correct, return the translation of "string"
    to a decimal number. Otherwise, raise a ValueError
    '''
    A, B, C, D, E, F, G = permutation
    # Assume a 7 segment display with following segments:
    #   AAAA
    # B     C
    # B     C
    #   DDDD
    # E     F
    # E     F
    #   GGGG

    # Try to make sense of what digit does the "string" show on the 7 segment display
    chars = (A, B, C, D, F, G)
    if all(i in string for i in chars) and len(string) == len(chars):
        return 9
    chars = (A, B, C, D, E, F, G)
    if all(i in string for i in chars) and len(string) == len(chars):
        return 8
    chars = (A, C, F)
    if all(i in string for i in chars) and len(string) == len(chars):
        return 7
    chars = (A, B, D, E, F, G)
    if all(i in string for i in chars) and len(string) == len(chars):
        return 6
    chars = (A, B, D, F, G)
    if all(i in string for i in chars) and len(string) == len(chars):
        return 5
    chars = (B, D, C, F)
    if all(i in string for i in chars) and len(string) == len(chars):
        return 4
    chars = (A, C, D, F, G)
    if all(i in string for i in chars) and len(string) == len(chars):
        return 3
    chars = (A, C, D, E, G)
    if all(i in string for i in chars) and len(string) == len(chars):
        return 2
    chars = (C, F)
    if all(i in string for i in chars) and len(string) == len(chars):
        return 1
    chars = (A, C, F, G, E, B)
    if all(i in string for i in chars) and len(string) == len(chars):
        return 0

    # No valid digit could be seen on the 7 segment display for "string"
    raise ValueError


def decode(string_list, permutation):
    num = 0
    for string in string_list:
        num = num*10 + translate_to_num(string, permutation)
    return num


def process(line):
    left, right = [part.split() for part in line.split(" | ")]

    # One particular ordering of "abcdefg" is such that the left and right parts
    # can be decoded back to a multi-digit number without any further wark
    # So, brute force through all 7! permutations until we find it!
    for permutation in permutations('abcdefg'):
        try:
            decode(left, permutation)
        except:
            # left part couldn't be decoded - permutation was incorrect
            continue
        # left part decoded without any issues - permutation is correct!
        # Now, decode the right hand side and return
        return decode(right, permutation)
    raise ValueError("No permutation found!")


def part2():
    lines = open("in.txt").read().strip().splitlines()
    count = 0
    for line in lines:
        count += process(line)
    print(count)


part2()
