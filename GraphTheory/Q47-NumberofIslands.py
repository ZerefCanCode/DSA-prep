from collections import deque
from typing import List

class Solution:
    def imBfs(self, r: int, c: int, grid: List[List[str]], vis: List[List[int]]) -> None:
        vis[r][c] = 1 

        q = deque([(r, c)])
        n = len(grid)
        m = len(grid[0])

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while q:
            x, y = q.popleft()

            for dr, dc in directions:
                newRow, newCol = x + dr, y + dc

                if 0 <= newRow < n and 0 <= newCol < m and grid[newRow][newCol] == '1' and not vis[newRow][newCol]:
                    vis[newRow][newCol] = 1
                    q.append((newRow, newCol))

    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        vis = [[0] * col for _ in range(row)] 

        cnt = 0

        for i in range(row):
            for j in range(col):
                if not vis[i][j] and grid[i][j] == '1': 

                    cnt += 1
                    self.imBfs(i, j, grid, vis)

        return cnt
    
S=Solution()
print(S.numIslands([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
))