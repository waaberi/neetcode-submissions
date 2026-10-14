class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) # assert len(grid) >= 1

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        def visit_islands(i: int, j: int, iden: int) -> bool:
            if not 0 <= i < m:
                return False
            if not 0 <= j < n:
                return False
            if grid[i][j] != 1: # 1 is unclaimed territory
                return False

            grid[i][j] = iden

            for d_i, d_j in directions:
                new_i, new_j = i + d_i, j + d_j
                visit_islands(new_i, new_j, iden)

            return True

        new_iden = 2

        counter: dict[int, int] = defaultdict(int) # iden, count

        max_area = 0

        for i in range(m):
            for j in range(n):
                if visit_islands(i, j, new_iden):
                    new_iden += 1 # increment when a visit is successful
                if grid[i][j] != 0: # we know it wont be 1 either
                    counter[grid[i][j]] += 1
                    max_area = max(max_area, counter[grid[i][j]])

        return max_area