from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        i did this problem before
        its cancer

        so water goes in all 4 directions but only to cells with equal heights or lower

        if i wanna be fancy i can make 2 functions:
            - goes_to_pacific(i, j)
            - goes_to_atlantic(i, j)

        as far as i can tell these are immutable. u dont need to change anything to make them

        and i can jsut use the cache decorator in python (or for google, lru_cache(maxsize=None))

        i will actually do that as ive done the problem before and i did it in a different, boring way.

        but actually i need to think about something else first

        am i SURE that this can be cached?

        its actually nto so obvious. i can make a counter example where there are cycles

        whenever u got cycles its over

        if you had only 7s then you'd need to track a visited set

        that would not be viable with a cache

        so i will actually give up on that

        bfs seems to work and i dont see any obvious caviats there

        lets see if i can show that bfs will not work

        ok i think bfs works, but i still havent established how i would actually solve this problem with a reasonable time and space complexity

        my current intuition is i maintain 2 bfs's that work across the same grid or 2 different grids it doesnt rly matter.


        pretend we had a grid and it had 2 booleans one is reaches_pacific and the other is reaches_atlantic

        then i have a bfs for both right

        so for pacific i make its queue
        for atlantic i also make its queue

        then if an element with height >= to the element we just popped from the queue is found
        then we mark as visited and we change the specific variable which could be pacific or atlantic doesnt rly matter

        we'll need to track a visited set for this

        but do we need 2 visited sets? one for pacific, one for atlantic

        i think the approach is viable although maybe we could save more space. in the real interview i would ask the interviewer what he thinks, but now i will just go ahead and implement
        """

        m = len(heights)
        n = len(heights[0]) # assert len(heights) >= 1

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        working_grid = [[[False, False] for _ in range(n)] for _ in range(m)]
        # i just relialized maintaining a visited set may be completely useless!
        # reason: the only place where i add something to visited set, i also set it to true.
        # if something is continuously false it will not be a cycle IMO. will double check later
        # i will keep it for now to focus on finishing the solution

        pacific_arr = [(i, 0) for i in range(m)] + [(0, j) for j in range(1, n)]

        for i, j in pacific_arr:
            working_grid[i][j][0] = True

        pacific_queue: deque[tuple[int, int]] = deque(pacific_arr)
        pacific_visited: set[tuple[int, int]] = set(pacific_arr)

        atlantic_arr = [(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(0, n-1)]

        for i, j in atlantic_arr:
            working_grid[i][j][1] = True
            
        atlantic_queue: deque[tuple[int, int]] = deque(atlantic_arr)
        atlantic_visited: set[tuple[int, int]] = set(atlantic_arr)

        def bfs(visited_set, queue, idx):
            while queue:
                i, j = queue.popleft()
                for d_i, d_j in directions:
                    new_i = i + d_i
                    new_j = j + d_j
                    tup = (new_i, new_j)
                    if 0 <= new_i < m and 0 <= new_j < n and tup not in visited_set and heights[new_i][new_j] >= heights[i][j]:
                        visited_set.add(tup)
                        queue.append(tup)
                        working_grid[new_i][new_j][idx] = True


        bfs(pacific_visited, pacific_queue, 0)
        bfs(atlantic_visited, atlantic_queue, 1)

        return [[i, j] for i in range(m) for j in range(n) if all(working_grid[i][j])]
        

