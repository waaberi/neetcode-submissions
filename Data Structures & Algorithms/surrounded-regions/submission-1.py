from functools import cache

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        better thing to do is to go from the edge and see who's reachable
        anything not reachable will be labelled with an X!
        but i probably need to do 2 passes here. still, I will try.

        First step: From the edges, go change all O's to a #
        Second step: If you're an O, you become an X, but if you're a #, then you become an O
        """

        m = len(board)
        n = len(board[0]) # assert n >= 1
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        stack: list[tuple[int, int]] = []
        for i in range(m):
            if board[i][0] == "O":
                stack.append((i, 0))
            if board[i][n - 1] == "O":
                stack.append((i, n - 1))
        
        for j in range(1, n - 1):
            if board[0][j] == "O":
                stack.append((0, j))
            if board[m - 1][j] == "O":
                stack.append((m - 1, j))

        while stack:
            i, j = stack.pop()
            
            board[i][j] = "#" # mark as visited

            for d_i, d_j in directions:
                new_i, new_j = i + d_i, j + d_j
                if not 0 <= new_i < m:
                    continue
                if not 0 <= new_j < n:
                    continue
                if board[new_i][new_j] != "O":
                    continue
                stack.append((new_i, new_j))


        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"