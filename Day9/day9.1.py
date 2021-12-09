
def get_neighbours(x, y, grid):
    '''
    This function returns all the valid neighbor cell values
    for a cell at (x, y) location in the grid
    '''
    R, C = len(grid), len(grid[0])
    # Check for all 4 boundary conditions
    if x != 0:
        yield grid[x-1][y]
    if y != 0:
        yield grid[x][y-1]
    if x != R-1:
        yield grid[x+1][y]
    if y != C-1:
        yield grid[x][y+1]


def part1():
    grid = open("in.txt").read().strip().splitlines()
    count = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if all(cell < i for i in get_neighbours(i, j, grid)):
                count += (1 + int(cell))
    print(count)


part1()
