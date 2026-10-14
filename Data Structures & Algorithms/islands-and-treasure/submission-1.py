from functools import cache
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        
        INF = 2 ** 31 - 1
        queue = deque([(i, j) for i in range(n) for j in range(m) if grid[i][j] == 0])
        while queue:
            i, j = queue.popleft()
            if 0 <= j < m:
                if 0 <= i-1 < n and grid[i-1][j] == INF:
                    grid[i-1][j] = grid[i][j] + 1
                    queue.append((i-1, j))
                if 0 <= i+1 < n and grid[i+1][j] == INF:
                    grid[i+1][j] = grid[i][j] + 1
                    queue.append((i+1, j))
            if 0 <= i < n:
                if 0 <= j-1 < m and grid[i][j-1] == INF:
                    grid[i][j-1] = grid[i][j] + 1
                    queue.append((i, j-1))
                if 0 <= j+1 < m and grid[i][j+1] == INF:
                    grid[i][j+1] = grid[i][j] + 1
                    queue.append((i, j+1))

