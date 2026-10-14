class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0]) # assert len(grid) >= 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def visit_islands(i: int, j: int):
            if not 0 <= i < m:
                return False
            if not 0 <= j < n:
                return False
            if grid[i][j] == "0":
                return False

            grid[i][j] = "0" # mark cell as visited
            
            for di, dj in directions:
                new_i, new_j = i + di, j + dj

                visit_islands(new_i, new_j)

            return True

        return sum(visit_islands(i, j) for i in range(m) for j in range(n))
