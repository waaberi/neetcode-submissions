from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        problem: return minimum number of minutes until none of the fruits are fresh
        i really think this is a bfs problem

        but at the same time i cant help but think that the framing of it as a bfs problem is weird


        i guess the state i gotta bfs on is candidates?


        so for example the queue starts with the rotten grids

        then every minute i will add all valid candidates to the queue to process them, and i will mark them as rotten

        and i keep this up

        but before sticking to bfs, i must ask myself this

        why wouldnt bfs work?

        issue with bfs is that it wont occur day by day

        here the depth is the amount of days

        bfs is perfect for this, dfs is non-obvious

        therefore, i will use bfs

        i just realized, i need to store the day as well
        
        otherwise i will have  no awareness of it

        ACTUALLY, there is this trick ive seen before and i will use it

        the trick is to have 2 loops, one is the typical while queue, but the other is the for _ in range(len(queue)) which will be frozen at the length of the queue for a given day.

        i will utilize this trikc as it will save a lot of space.
        """
        m = len(grid)
        n = len(grid[0]) # assert len(grid) >= 1

        day = 0
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
            day += 1

        if fresh_count == 0:
            return day
        else:
            return -1
