from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0]) # assert len(grid) >= 1

        minute = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue: deque[tuple[int, int]] = deque()

        fresh_count = 0

        for i in range(m):
            for j in range(n):
                fruit = grid[i][j]
                if fruit == 1:
                    fresh_count += 1
                elif fruit == 2:
                    queue.append((i, j))

        while queue and fresh_count:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for d_i, d_j in directions:
                    new_i = i + d_i
                    new_j = j + d_j
                    # check if in bounds and fresh
                    if 0 <= new_i < m and 0 <= new_j < n and grid[new_i][new_j] == 1:
                        grid[new_i][new_j] = 2 # mark as rotten
                        fresh_count -= 1
                        queue.append((new_i, new_j))
            minute += 1

        if fresh_count == 0:
            return minute
        
        return -1 # queue ran out but theres still fresh apples.
