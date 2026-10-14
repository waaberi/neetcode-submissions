from functools import cache
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])

        def in_bounds(i, j):
            return 0 <= i < n and 0 <= j < m

        INF = 2 ** 31 - 1
        queue = deque([(i, j) for i in range(n) for j in range(m) if grid[i][j] == 0])
        while queue:
            i, j = queue.popleft()
            if in_bounds(i-1, j) and grid[i-1][j] == INF:
                grid[i-1][j] = grid[i][j] + 1
                queue.append((i-1, j))
            if in_bounds(i+1, j) and grid[i+1][j] == INF:
                grid[i+1][j] = grid[i][j] + 1
                queue.append((i+1, j))
            if in_bounds(i, j-1) and grid[i][j-1] == INF:
                grid[i][j-1] = grid[i][j] + 1
                queue.append((i, j-1))
            if in_bounds(i, j+1) and grid[i][j+1] == INF:
                grid[i][j+1] = grid[i][j] + 1
                queue.append((i, j+1))

