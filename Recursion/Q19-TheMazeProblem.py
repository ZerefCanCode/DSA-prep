

def count_paths(grid, i, j):
    # outside grid
    if i < 0 or j < 0:
        return 0
    
    # obstacle
    if grid[i][j] == 1:
        return 0
    
    # reached start
    if i == 0 and j == 0:
        return 1

    # from top + from left
    return count_paths(grid, i-1, j) + count_paths(grid, i, j-1)

grid=[[0, 0, 1],
[0, 0, 0],
[1, 0, 0]]

m = len(grid)
n = len(grid[0])
print(count_paths(grid, m-1, n-1))

#Time complexity is Exponential → O(2^(m+n)).

