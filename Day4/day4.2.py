def is_complete(board):
    """
    Given a bingo board as a 2D array of integers,
    return if it is now complete
    """
    rows = board
    for row in rows:
        if all(cell < 0 for cell in row):
            return True  # We have a row which has all numbers marked

    width = len(rows[0])
    for i in range(width):
        column = [row[i] for row in rows]
        if all(cell < 0 for cell in column):
            return True  # We have a column which has all numbers marked
    return False


def update_boards(number, boards):
    for board in boards:
        yield mark_number(number, board)


def mark_number(number, board):
    """
    Given a number and a board, mark the number on the board if found
    and return the board
    """
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell == number:
                # Mark the cell by overwriting it with -1 and return the board
                board[r][c] = -1
                return board
    # No cell was marked, return the board as it was
    return board


def get_score(number, board):
    count = 0
    for row in board:
        for cell in row:
            count += cell if cell > 0 else 0
    return number * count


def part2():
    blocks = open("in.txt").read().split("\n\n")
    line = blocks[0]
    numbers = list(map(int, line.strip().split(",")))
    boards = []
    for block in blocks[1:]:
        board = [list(map(int, line.strip().split())) for line in block.splitlines()]
        boards.append(board)

    candidates = boards
    for number in numbers:
        candidates = list(update_boards(number, candidates))
        # Iterate over a copy of candidates as it'll be modified within the loop
        for board in candidates[:]:
            if is_complete(board):
                # if it's the last board, print the score!
                if len(candidates) == 1:
                    print(get_score(number, board))
                    return
                # Remove this board from candidate list
                candidates.remove(board)


part2()
