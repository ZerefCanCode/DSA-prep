'''You are given an N x N maze represented as a matrix:

1 → open cell (rat can move)

0 → blocked cell (rat cannot move)'''

def isSafe(maze, visited, i, j, N):
    return (0 <= i < N and
            0 <= j < N and
            maze[i][j] == 1 and
            not visited[i][j])


def solveAllPaths(maze, i, j, N, visited, path, all_paths):
    # If reached destination
    if i == N-1 and j == N-1:
        all_paths.append(path[:])
        return

    # Mark visited
    visited[i][j] = True

    # Move Down
    if isSafe(maze, visited, i+1, j, N):
        path.append("D")
        solveAllPaths(maze, i+1, j, N, visited, path, all_paths)
        path.pop()

    # Move Right
    if isSafe(maze, visited, i, j+1, N):
        path.append("R")
        solveAllPaths(maze, i, j+1, N, visited, path, all_paths)
        path.pop()

    # Move Up
    if isSafe(maze, visited, i-1, j, N):
        path.append("U")
        solveAllPaths(maze, i-1, j, N, visited, path, all_paths)
        path.pop()

    # Move Left
    if isSafe(maze, visited, i, j-1, N):
        path.append("L")
        solveAllPaths(maze, i, j-1, N, visited, path, all_paths)
        path.pop()

    # Unmark (Backtracking)
    visited[i][j] = False


# Driver
maze = [
    [1,0,0,0],
    [1,1,0,1],
    [0,1,0,0],
    [1,1,1,1]
]

N = len(maze)
visited = [[False]*N for _ in range(N)]
all_paths = []

solveAllPaths(maze, 0, 0, N, visited, [], all_paths)
print("All paths:", all_paths)
