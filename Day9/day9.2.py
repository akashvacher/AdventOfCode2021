from math import prod


def get_neighbour_locations(x, y, grid):
    '''
    This function returns all the valid neighbor cell locations
    for a cell at (x, y) location in the grid
    '''
    R, C = len(grid), len(grid[0])
    # Check for all 4 boundary conditions
    if x != 0:
        yield (x-1, y)
    if y != 0:
        yield (x, y-1)
    if x != R-1:
        yield (x+1, y)
    if y != C-1:
        yield (x, y+1)


def part2():
    grid = open("in.txt").read().strip().splitlines()
    marked = [[False] * len(grid[0]) for _ in range(len(grid))]

    def flood(i, j, grid):
        # grid[i][j] is not marked yet, so let's mark it and count it
        marked[i][j] = True
        count = 1
        for x, y in get_neighbour_locations(i, j, grid):
            # Ignore hard boundaries and explored neighbours
            if grid[x][y] == '9' or marked[x][y]:
                continue
            count += flood(x, y, grid)
        return count

    basin_sizes = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            # Ignore hard boundaries and explored neighbours
            if cell == '9' or marked[i][j]:
                continue
            # We are in an unexplored basin - count and mark all cells within it
            basin_size = flood(i, j, grid)
            basin_sizes.append(basin_size)
    basin_sizes = sorted(basin_sizes, reverse=True)
    print(prod(basin_sizes[:3]))


part2()
